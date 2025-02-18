import sys
import ply.yacc as yacc
from lexico import ClaseLexico
import json
from funciones_semantico import FuncionesSemantico
import funciones_semantico
from codigo_intermedio import CodigoIntermedio
from codigo_intermedio import codigo_intermedio_lista, codigo_intermedio_lista_if, codigo_intermedio_lista_label1, codigo_intermedio_lista_label2

codigo_intermedio_clase = CodigoIntermedio()
class ClaseSintactico(object):

    tokens = ClaseLexico.tokens

    precedence = (
        ('left', '+', '-', "."),
        ('left', '*', '/'),
        ('left', 'DISYUNCION', 'CONJUNCION'),
        ('right', 'UMINUS', "!"),
        ('nonassoc', '<', '>', 'MENORIG', 'MAYORIG', 'IGUAL'),
    )

    # REGLAS DE PRODUCCION
    def p_archivo(self, p):
        '''archivo : lineas
                   | lambda'''

    def p_lambda(self, p):
        '''lambda : '''

    def p_lineas(self, p):
        '''lineas : linea_normal ";"
                  | linea_especial
                  | linea_normal ";" lineas
                  | linea_especial lineas'''

    def p_linea_normal(self, p):
        '''linea_normal : llamada_funcion
                        | asignacion
                        | declaracion'''

    def p_linea_especial(self, p):
        '''linea_especial : COM_MULTI
                          | COM_SIMPLE
                          | funcion
                          | condicional'''

    def p_expresion_binop(self, p):
        '''expresion : expresion "+" expresion
                     | expresion "-" expresion
                     | expresion "*" expresion
                     | expresion "/" expresion
                     | expresion "<" expresion
                     | expresion ">" expresion
                     | expresion MAYORIG expresion
                     | expresion MENORIG expresion
                     | expresion IGUAL expresion
                     | expresion DISYUNCION expresion
                     | expresion CONJUNCION expresion'''

        funciones = FuncionesSemantico()
        funciones.logica_expresiones(p)
        codigo_intermedio_clase.codigo_intermedio_expresiones(p)


    def p_expresion_uminus(self,p):
        '''expresion : "-" expresion %prec UMINUS'''

        p[0] = -p[2]

    def p_expresion_not(self,p):
        '''expresion : "!" expresion'''

        if p[2] == "tr":
            p[0] = "fl"
        if p[2] == "fl":
            p[0] = "tr"

    def p_expresion_grupo(self, p):
        '''expresion : "(" expresion ")" '''
        p[0] = p[2]

    def p_expresion_parametro(self, p):
        '''expresion : ENTERO
                     | REAL
                     | TR
                     | FL
                     | NULL
                     | CARACTER
                     | IDENTIFIER
                     | propiedad
                     | llamada_funcion
                     | objeto_expresion'''
        p[0] = p[1]



    def p_propiedad_exp(self, p):
        '''propiedad : IDENTIFIER "[" STRING "]"
                     | IDENTIFIER "." propiedad
                     | IDENTIFIER "." IDENTIFIER
                     | IDENTIFIER "[" STRING "]" "." IDENTIFIER'''
        if len(p) == 4 or len(p) == 5:
            p[0] = p[1] + "." + p[3]
        if len(p) == 7:
            p[0] = p[1] + "." + p[3] + "." + p[6]


    def p_asignacion(self,p):
        '''asignacion : IDENTIFIER "=" expresion
                      | propiedad "=" expresion'''
        funciones = FuncionesSemantico()
        funciones.logica_asignaciones(p)
        codigo_intermedio_clase.codigo_intermedio_asignaciones(p)



    def p_declaracion(self, p):
        '''declaracion : LET lista_declaraciones
                       | TYPE IDENTIFIER "=" objeto_tipo'''

        funciones = FuncionesSemantico()
        funciones.logica_type(p)



    def p_lista_declaraciones(self, p):
        '''lista_declaraciones : contenido_declaracion
                               | contenido_declaracion "," lista_declaraciones'''


    def p_contenido_declaracion(self, p):
        '''contenido_declaracion : IDENTIFIER
                                 | IDENTIFIER ":" IDENTIFIER
                                 | IDENTIFIER ":" IDENTIFIER "=" expresion
                                 | IDENTIFIER "=" expresion'''
        funciones = FuncionesSemantico()
        funciones.logica_declaraciones(p)


    def p_condicional(self,p):
        '''condicional : IF condiciones contenido_if
                       | IF condiciones contenido_if_else contenido_else
                       | WHILE condiciones_while contenido_while'''

    def p_condiciones(self, p):
        '''condiciones : "(" expresion ")"'''
        funciones = FuncionesSemantico()
        funciones.logica_condicionales(p)
        codigo_intermedio_clase.codigo_intermedio_ifs(p)

    def p_condiciones_while(self, p):
        '''condiciones_while : "(" expresion ")"'''
        funciones = FuncionesSemantico()
        funciones.logica_condicionales(p)

    def p_contenido_while(self, p):
        '''contenido_while : "{" lineas_cond "}"'''

    def p_contenido_if(self, p):
        '''contenido_if : "{" lineas_cond "}"'''
        codigo_intermedio_clase.codigo_intermedio_label0_if(p)

    def p_contenido_if_else(self, p):
        '''contenido_if_else : "{" lineas_cond "}"'''
        codigo_intermedio_clase.codigo_intermedio_else(p)

    def p_contenido_else(self, p):
        '''contenido_else : ELSE "{" lineas_cond "}"'''
        codigo_intermedio_clase.codigo_intermedio_label0_else(p)

    def p_lineas_cond(self, p):
        '''lineas_cond : linea_cond
                       | linea_cond lineas_cond'''


    def p_linea_cond(self,p):
        '''linea_cond : linea_normal_cond ";"
                      | linea_especial_cond'''


    def p_linea_normal_cond(self, p):
        '''linea_normal_cond : llamada_funcion
                             | asignacion
                             | declaracion'''


    def p_linea_especial_cond(self, p):
        '''linea_especial_cond : COM_MULTI
                               | COM_SIMPLE
                               | condicional'''

    def p_funcion(self, p):
        '''funcion : FUNCTION IDENTIFIER "(" argumentos ")" ":" tipo "{" contenido_funcion "}"'''
        funciones = FuncionesSemantico()
        funciones.logica_funciones(p)
        # self.print_pila(p)

        codigo_intermedio.codigo_intermedio_ifs(p)



    def p_contenido_funcion(self, p):
        '''contenido_funcion : lineas_fun RETURN expresion ";"
                             | RETURN expresion ";"'''
        funciones = FuncionesSemantico()
        funciones.logica_return(p)
        # self.print_pila(p)

    def p_lineas_fun(self, p):
        '''lineas_fun : linea_normal_fun ";"
                       | linea_especial_fun
                       | linea_normal_fun ";" lineas_fun
                       | linea_especial_fun lineas_fun'''

    def p_linea_normal_fun(self, p):
        '''linea_normal_fun : llamada_funcion
                             | asignacion
                             | declaracion'''

    def p_linea_especial_fun(self, p):
        '''linea_especial_fun : COM_MULTI
                               | COM_SIMPLE
                               | condicional'''



    def p_argumentos(self, p):
        '''argumentos : argumento
                      | argumento "," argumentos
                      | lambda'''
        if len(p) == 2:
            p[0] = [p[1]]
        if len(p) == 4:
            p[0] = [p[1]] + p[3]


    def p_argumento(self, p):
        '''argumento : IDENTIFIER ":" tipo'''
        p[0] = {"nombre":p[1], "tipo":p[3]}


    def p_llamada_funcion(self,p):
        '''llamada_funcion : IDENTIFIER "(" parametros_funcion ")"'''
        funciones = FuncionesSemantico()
        funciones.logica_llamadas(p)


    def p_parametros_funcion(self,p):
        '''parametros_funcion : expresion
                              | expresion "," parametros_funcion
                              | lambda'''
        if len(p) == 2:
            p[0] = [p[1]]
        if len(p) == 4:
            p[0] = [p[1]] + p[3]


    def p_objeto_expresion(self, p):
        '''objeto_expresion : "{" pares_expresion "}"'''
        p[0] = p[2]

    def p_pares_expresion(self, p):
        '''pares_expresion : par_expresion "," pares_expresion
                           | par_expresion'''
        if len(p) < 3:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]

    def p_par_expresion(self, p):
        '''par_expresion : clave_expresion ":" expresion'''
        p[0] = {"nombre":p[1],"valor":p[3]}

    def p_clave_expresion(self, p):
        '''clave_expresion : IDENTIFIER
                           | STRING'''
        p[0] = p[1]

    def p_objeto_tipo(self, p):
        '''objeto_tipo : "{" pares_tipo "}"'''
        p[0] = p[2]

    def p_pares_tipo(self, p):
        '''pares_tipo : par_tipo "," pares_tipo
                      | par_tipo'''
        if len(p) < 3:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]

    def p_par_tipo(self, p):
        '''par_tipo : clave_tipo ":" tipo'''
        p[0] = {"nombre":p[1],"tipo":p[3]}

    def p_clave_tipo(self, p):
        '''clave_tipo : IDENTIFIER
                      | STRING'''
        p[0] = p[1]

    def p_tipo(self, p):
        '''tipo : INT
                | FLOAT
                | BOOLEAN
                | CHARACTER
                | IDENTIFIER
                | objeto_tipo'''
        p[0] = p[1]


    def p_error(self,t):
        if t:
            print("Error con", t.value, "| Linea:", t.lineno, "| Pos:", t.lexpos)
        else:
            print("Error EOF")



    def print_pila(self,pila):
        lista_pila = []
        for item in pila:
            lista_pila.append(item)
        print(lista_pila)

    def build(self):
        self.parser = yacc.yacc(module=self)



    def probar_parser(self):
        file = open(sys.argv[1])
        content = file.read()
        self.parser.parse(content)
        codigo_intermedio_clase.procesar_datos()
        print("Simbolos: ", funciones_semantico.simbolos)
        print("Registros: ", funciones_semantico.registros)