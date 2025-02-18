import ply.lex as lex
from ply.lex import TOKEN
import sys

# Definiciones de las expresiones regulares
regex_int = r'[-]?([1-9][0-9]*|0)'
regex_hex = r'[-]?0[xX][0-9a-fA-F]+'
regex_oct = r'0[0-7]+'
regex_bin = r'[-]?0[bB][01]+'
regex_float = r'[-]?([0-9]*[.][0-9]+|[0-9]+[.])'
regex_cien = r'[-]?([0-9]+[eE][-]?[0-9]+|[.][0-9]+[eE][-]?[0-9]+)'

# Combinación de expresiones regulares para enteros y reales
regex_enteros = r'|'.join([regex_hex, regex_bin, regex_oct, regex_int])
regex_reales = r'|'.join([regex_cien, regex_float])

# Expresiones regulares para caracteres y cadenas de texto
regex_caracter = r"'(\\['\\]|[^\n'\\])'"
regex_string = r'"([^"\n\\]|\\[nrt"\\])*"'

class ClaseLexico:
    # Definición de las palabras reservadas
    reserved = ("TR", "FL", "LET", "INT", "FLOAT", "CHARACTER", "WHILE",
                "BOOLEAN", "FUNCTION", "RETURN", "TYPE", "IF", "ELSE", "NULL")

    reserved_map = {r.lower(): r for r in reserved}
    
    #Literales
    literals = ["'", "+", "-", "*", "/", "<", ">", "=", ";", 
                "{", "}", ":", ",", ".", "(", ")", "[", "]", "!"]

    # Lista completa de tokens
    tokens = (
        'COM_SIMPLE', 'COM_MULTI', 'ENTERO', 'REAL', 'CONJUNCION', 'DISYUNCION',
        'IGUAL', 'MAYORIG', 'MENORIG', 'CARACTER', 'IDENTIFIER', 'STRING'
     ) + reserved

    # Definición de tokens
    t_MAYORIG = r'>='
    t_MENORIG = r'<='
    t_IGUAL = r'=='
    t_CONJUNCION = r'&&'
    # t_DISYUNCION = r'[\x7C]{2}'

    # Ignorar espacios y tabs
    t_ignore = ' \t'

    def t_DISYUNCION(self, t):
        r'[\x7C]{2}'
        return t


    # Reglas para manejar comentarios
    def t_COM_SIMPLE(self, t):
        r'\/\/[^\n]*'
        pass

    def t_COM_MULTI(self, t):
        r'\/\*[^*]*\*+(?:[^/*][^*]*\*+)*\/'
        pass
    
    # Regla para números reales
    @TOKEN(regex_reales)
    def t_REAL(self, t):
        t.value = float(t.value)
        return t

    # Regla para números enteros
    @TOKEN(regex_enteros)
    def t_ENTERO(self, token):
        if "x" in token.value or "X" in token.value:
            token.value = int(token.value, 16)
        elif "b" in token.value or "B" in token.value:
            token.value = int(token.value, 2)
        elif "o" in token.value or "O" in token.value:
            token.value = int(token.value, 8)
        else:
            token.value = int(token.value)

        return token

    # Regla para caracteres
    @TOKEN(regex_caracter)
    def t_CARACTER(self, t):
        t.value = t.value[1:-1]
        if len(t.value) > 1 and t.value.startswith('\\'):
            escape_dict = {'n': '\n', 't': '\t', '\\': '\\', "'": "'"}
            t.value = escape_dict.get(t.value[1], t.value[1])
        return t

    # Regla para identificadores y palabras reservadas
    def t_IDENTIFIER(self, t):
        r'[\x41-\x5A|\x61-\x7A|\x80-\xFE][\x41-\x5A|\x61-\x7A|\x80-\xFE|\x30-\x39_]*'
        t.type = self.reserved_map.get(t.value, 'IDENTIFIER') # Verifica palabras reservadas
        return t

    # Regla para cadenas
    @TOKEN(regex_string)
    def t_STRING(self, t):
        t.value = t.value[1:-1].encode().decode('unicode_escape')
        return t

    # Manejo de errores léxicos
    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}, position {t.lexer.lexpos}")
        t.lexer.skip(1)

    # Manejo de nuevas líneas
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def probar_lexer(self):
        file = open(sys.argv[1])
        self.lexer.input(file.read())
        with open(file.name + '.token', 'w') as token_file:
            for token in self.lexer:
                token_file.write(f'{token.type} {token.value}\n')

    # Construcción del lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
