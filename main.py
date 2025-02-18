from lexico import ClaseLexico
from sintactico import ClaseSintactico
import sys

opcion = sys.argv[2]

lex = ClaseLexico()
lex.build()
sint = ClaseSintactico()
sint.build()

if opcion == "-lex":
    lex.probar_lexer()
elif opcion == "-par":
    sint.probar_parser()
