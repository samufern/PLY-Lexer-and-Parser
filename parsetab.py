
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'left+-.left*/leftDISYUNCIONCONJUNCIONrightUMINUS!nonassoc<>MENORIGMAYORIGIGUALBOOLEAN CARACTER CHARACTER COM_MULTI COM_SIMPLE CONJUNCION DISYUNCION ELSE ENTERO FL FLOAT FUNCTION IDENTIFIER IF IGUAL INT LET MAYORIG MENORIG NULL REAL RETURN STRING TR TYPE WHILEarchivo : lineas\n                   | lambdalambda : lineas : linea_normal ";"\n                  | linea_especial\n                  | linea_normal ";" lineas\n                  | linea_especial lineaslinea_normal : llamada_funcion\n                        | asignacion\n                        | declaracionlinea_especial : COM_MULTI\n                          | COM_SIMPLE\n                          | funcion\n                          | condicionalexpresion : expresion "+" expresion\n                     | expresion "-" expresion\n                     | expresion "*" expresion\n                     | expresion "/" expresion\n                     | expresion "<" expresion\n                     | expresion ">" expresion\n                     | expresion MAYORIG expresion\n                     | expresion MENORIG expresion\n                     | expresion IGUAL expresion\n                     | expresion DISYUNCION expresion\n                     | expresion CONJUNCION expresionexpresion : "-" expresion %prec UMINUSexpresion : "!" expresionexpresion : "(" expresion ")" expresion : ENTERO\n                     | REAL\n                     | TR\n                     | FL\n                     | NULL\n                     | CARACTER\n                     | IDENTIFIER\n                     | propiedad\n                     | llamada_funcion\n                     | objeto_expresionpropiedad : IDENTIFIER "[" STRING "]"\n                     | IDENTIFIER "." propiedad\n                     | IDENTIFIER "." IDENTIFIER\n                     | IDENTIFIER "[" STRING "]" "." IDENTIFIERasignacion : IDENTIFIER "=" expresion\n                      | propiedad "=" expresiondeclaracion : LET lista_declaraciones\n                       | TYPE IDENTIFIER "=" objeto_tipolista_declaraciones : contenido_declaracion\n                               | contenido_declaracion "," lista_declaracionescontenido_declaracion : IDENTIFIER\n                                 | IDENTIFIER ":" IDENTIFIER\n                                 | IDENTIFIER ":" IDENTIFIER "=" expresion\n                                 | IDENTIFIER "=" expresioncondicional : IF condiciones contenido_if\n                       | IF condiciones contenido_if_else contenido_else\n                       | WHILE condiciones_while contenido_whilecondiciones : "(" expresion ")"condiciones_while : "(" expresion ")"contenido_while : "{" lineas_cond "}"contenido_if : "{" lineas_cond "}"contenido_if_else : "{" lineas_cond "}"contenido_else : ELSE "{" lineas_cond "}"lineas_cond : linea_cond\n                       | linea_cond lineas_condlinea_cond : linea_normal_cond ";"\n                      | linea_especial_condlinea_normal_cond : llamada_funcion\n                             | asignacion\n                             | declaracionlinea_especial_cond : COM_MULTI\n                               | COM_SIMPLE\n                               | condicionalfuncion : FUNCTION IDENTIFIER "(" argumentos ")" ":" tipo "{" contenido_funcion "}"contenido_funcion : lineas_fun RETURN expresion ";"\n                             | RETURN expresion ";"lineas_fun : linea_normal_fun ";"\n                       | linea_especial_fun\n                       | linea_normal_fun ";" lineas_fun\n                       | linea_especial_fun lineas_funlinea_normal_fun : llamada_funcion\n                             | asignacion\n                             | declaracionlinea_especial_fun : COM_MULTI\n                               | COM_SIMPLE\n                               | condicionalargumentos : argumento\n                      | argumento "," argumentos\n                      | lambdaargumento : IDENTIFIER ":" tipollamada_funcion : IDENTIFIER "(" parametros_funcion ")"parametros_funcion : expresion\n                              | expresion "," parametros_funcion\n                              | lambdaobjeto_expresion : "{" pares_expresion "}"pares_expresion : par_expresion "," pares_expresion\n                           | par_expresionpar_expresion : clave_expresion ":" expresionclave_expresion : IDENTIFIER\n                           | STRINGobjeto_tipo : "{" pares_tipo "}"pares_tipo : par_tipo "," pares_tipo\n                      | par_tipopar_tipo : clave_tipo ":" tipoclave_tipo : IDENTIFIER\n                      | STRINGtipo : INT\n                | FLOAT\n                | BOOLEAN\n                | CHARACTER\n                | IDENTIFIER\n                | objeto_tipo'
    
_lr_action_items = {'$end':([0,1,2,3,5,9,10,11,12,20,21,36,64,68,102,144,147,168,181,],[-3,0,-1,-2,-5,-11,-12,-13,-14,-4,-7,-6,-53,-55,-54,-59,-58,-61,-72,]),'COM_MULTI':([0,5,9,10,11,12,20,64,66,68,69,102,105,107,111,112,113,143,144,146,147,168,169,174,178,179,180,181,184,],[9,9,-11,-12,-13,-14,9,-53,111,-55,111,-54,111,-65,-69,-70,-71,111,-59,-64,-58,-61,178,178,-82,-83,-84,-72,178,]),'COM_SIMPLE':([0,5,9,10,11,12,20,64,66,68,69,102,105,107,111,112,113,143,144,146,147,168,169,174,178,179,180,181,184,],[10,10,-11,-12,-13,-14,10,-53,112,-55,112,-54,112,-65,-69,-70,-71,112,-59,-64,-58,-61,179,179,-82,-83,-84,-72,179,]),'IDENTIFIER':([0,5,9,10,11,12,15,16,17,20,22,23,25,26,33,35,38,42,43,53,59,60,61,63,64,66,68,69,73,74,75,76,77,78,79,80,81,82,83,84,97,102,105,107,111,112,113,131,132,133,134,140,142,143,144,146,147,153,154,162,168,169,172,174,178,179,180,181,182,184,],[13,13,-11,-12,-13,-14,29,30,31,13,37,37,56,37,37,37,37,37,37,90,29,94,37,98,-53,13,-55,13,37,37,37,37,37,37,37,37,37,37,37,37,138,-54,13,-65,-69,-70,-71,90,37,150,37,155,98,13,-59,-64,-58,138,155,155,-61,13,37,13,-82,-83,-84,-72,37,13,]),'LET':([0,5,9,10,11,12,20,64,66,68,69,102,105,107,111,112,113,143,144,146,147,168,169,174,178,179,180,181,184,],[15,15,-11,-12,-13,-14,15,-53,15,-55,15,-54,15,-65,-69,-70,-71,15,-59,-64,-58,-61,15,15,-82,-83,-84,-72,15,]),'TYPE':([0,5,9,10,11,12,20,64,66,68,69,102,105,107,111,112,113,143,144,146,147,168,169,174,178,179,180,181,184,],[16,16,-11,-12,-13,-14,16,-53,16,-55,16,-54,16,-65,-69,-70,-71,16,-59,-64,-58,-61,16,16,-82,-83,-84,-72,16,]),'FUNCTION':([0,5,9,10,11,12,20,64,68,102,144,147,168,181,],[17,17,-11,-12,-13,-14,17,-53,-55,-54,-59,-58,-61,-72,]),'IF':([0,5,9,10,11,12,20,64,66,68,69,102,105,107,111,112,113,143,144,146,147,168,169,174,178,179,180,181,184,],[18,18,-11,-12,-13,-14,18,-53,18,-55,18,-54,18,-65,-69,-70,-71,18,-59,-64,-58,-61,18,18,-82,-83,-84,-72,18,]),'WHILE':([0,5,9,10,11,12,20,64,66,68,69,102,105,107,111,112,113,143,144,146,147,168,169,174,178,179,180,181,184,],[19,19,-11,-12,-13,-14,19,-53,19,-55,19,-54,19,-65,-69,-70,-71,19,-59,-64,-58,-61,19,19,-82,-83,-84,-72,19,]),';':([4,6,7,8,27,28,29,37,44,45,46,47,48,49,50,51,52,54,56,57,58,72,85,86,92,93,94,95,96,106,108,109,110,117,119,120,121,122,123,124,125,126,127,128,129,130,150,151,152,173,175,176,177,183,186,],[20,-8,-9,-10,-45,-47,-49,-35,-29,-30,-31,-32,-33,-34,-36,-37,-38,-43,-41,-40,-44,-89,-26,-27,-39,-48,-50,-52,-46,146,-66,-67,-68,-28,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-93,-42,-51,-99,184,-79,-80,-81,187,189,]),'(':([13,18,19,22,23,26,31,33,35,37,38,42,43,61,73,74,75,76,77,78,79,80,81,82,83,84,132,134,172,182,],[22,33,35,38,38,38,63,38,38,22,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'=':([13,14,29,30,56,57,92,94,150,],[23,26,61,62,-41,-40,-39,134,-42,]),'[':([13,37,56,],[24,24,24,]),'.':([13,37,56,92,],[25,25,25,133,]),'-':([22,23,26,33,35,37,38,40,42,43,44,45,46,47,48,49,50,51,52,54,56,57,58,61,67,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,92,95,117,119,120,121,122,123,124,125,126,127,128,129,130,132,134,149,150,151,172,182,183,186,],[42,42,42,42,42,-35,42,75,42,42,-29,-30,-31,-32,-33,-34,-36,-37,-38,75,-41,-40,75,42,75,75,75,-89,42,42,42,42,42,42,42,42,42,42,42,42,-26,-27,-39,75,-28,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-93,42,42,75,-42,75,42,42,75,75,]),'!':([22,23,26,33,35,38,42,43,61,73,74,75,76,77,78,79,80,81,82,83,84,132,134,172,182,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'ENTERO':([22,23,26,33,35,38,42,43,61,73,74,75,76,77,78,79,80,81,82,83,84,132,134,172,182,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'REAL':([22,23,26,33,35,38,42,43,61,73,74,75,76,77,78,79,80,81,82,83,84,132,134,172,182,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'TR':([22,23,26,33,35,38,42,43,61,73,74,75,76,77,78,79,80,81,82,83,84,132,134,172,182,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'FL':([22,23,26,33,35,38,42,43,61,73,74,75,76,77,78,79,80,81,82,83,84,132,134,172,182,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'NULL':([22,23,26,33,35,38,42,43,61,73,74,75,76,77,78,79,80,81,82,83,84,132,134,172,182,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'CARACTER':([22,23,26,33,35,38,42,43,61,73,74,75,76,77,78,79,80,81,82,83,84,132,134,172,182,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),')':([22,37,39,40,41,44,45,46,47,48,49,50,51,52,56,57,63,67,70,71,72,73,85,86,92,99,100,101,117,118,119,120,121,122,123,124,125,126,127,128,129,130,142,150,152,155,156,157,158,159,160,161,163,],[-3,-35,72,-90,-92,-29,-30,-31,-32,-33,-34,-36,-37,-38,-41,-40,-3,114,116,117,-89,-3,-26,-27,-39,141,-85,-87,-28,-91,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-93,-3,-42,-99,-109,-88,-105,-106,-107,-108,-110,-86,]),'{':([22,23,26,32,33,34,35,38,42,43,61,62,73,74,75,76,77,78,79,80,81,82,83,84,103,114,116,132,134,140,152,154,155,157,158,159,160,161,162,167,172,182,],[53,53,53,66,53,69,53,53,53,53,53,97,53,53,53,53,53,53,53,53,53,53,53,53,143,-56,-57,53,53,97,-99,97,-109,-105,-106,-107,-108,-110,97,169,53,53,]),'STRING':([24,53,97,131,153,],[55,91,139,91,139,]),',':([28,29,37,40,44,45,46,47,48,49,50,51,52,56,57,72,85,86,88,92,94,95,100,117,119,120,121,122,123,124,125,126,127,128,129,130,136,149,150,151,152,155,156,157,158,159,160,161,166,],[59,-49,-35,73,-29,-30,-31,-32,-33,-34,-36,-37,-38,-41,-40,-89,-26,-27,131,-39,-50,-52,142,-28,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-93,153,-96,-42,-51,-99,-109,-88,-105,-106,-107,-108,-110,-102,]),':':([29,89,90,91,98,137,138,139,141,],[60,132,-97,-98,140,154,-103,-104,162,]),'+':([37,40,44,45,46,47,48,49,50,51,52,54,56,57,58,67,70,71,72,85,86,92,95,117,119,120,121,122,123,124,125,126,127,128,129,130,149,150,151,183,186,],[-35,74,-29,-30,-31,-32,-33,-34,-36,-37,-38,74,-41,-40,74,74,74,74,-89,-26,-27,-39,74,-28,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-93,74,-42,74,74,74,]),'*':([37,40,44,45,46,47,48,49,50,51,52,54,56,57,58,67,70,71,72,85,86,92,95,117,119,120,121,122,123,124,125,126,127,128,129,130,149,150,151,183,186,],[-35,76,-29,-30,-31,-32,-33,-34,-36,-37,-38,76,-41,-40,76,76,76,76,-89,-26,-27,-39,76,-28,76,76,-17,-18,-19,-20,-21,-22,-23,-24,-25,-93,76,-42,76,76,76,]),'/':([37,40,44,45,46,47,48,49,50,51,52,54,56,57,58,67,70,71,72,85,86,92,95,117,119,120,121,122,123,124,125,126,127,128,129,130,149,150,151,183,186,],[-35,77,-29,-30,-31,-32,-33,-34,-36,-37,-38,77,-41,-40,77,77,77,77,-89,-26,-27,-39,77,-28,77,77,-17,-18,-19,-20,-21,-22,-23,-24,-25,-93,77,-42,77,77,77,]),'<':([37,40,44,45,46,47,48,49,50,51,52,54,56,57,58,67,70,71,72,85,86,92,95,117,119,120,121,122,123,124,125,126,127,128,129,130,149,150,151,183,186,],[-35,78,-29,-30,-31,-32,-33,-34,-36,-37,-38,78,-41,-40,78,78,78,78,-89,78,78,-39,78,-28,78,78,78,78,None,None,None,None,None,78,78,-93,78,-42,78,78,78,]),'>':([37,40,44,45,46,47,48,49,50,51,52,54,56,57,58,67,70,71,72,85,86,92,95,117,119,120,121,122,123,124,125,126,127,128,129,130,149,150,151,183,186,],[-35,79,-29,-30,-31,-32,-33,-34,-36,-37,-38,79,-41,-40,79,79,79,79,-89,79,79,-39,79,-28,79,79,79,79,None,None,None,None,None,79,79,-93,79,-42,79,79,79,]),'MAYORIG':([37,40,44,45,46,47,48,49,50,51,52,54,56,57,58,67,70,71,72,85,86,92,95,117,119,120,121,122,123,124,125,126,127,128,129,130,149,150,151,183,186,],[-35,80,-29,-30,-31,-32,-33,-34,-36,-37,-38,80,-41,-40,80,80,80,80,-89,80,80,-39,80,-28,80,80,80,80,None,None,None,None,None,80,80,-93,80,-42,80,80,80,]),'MENORIG':([37,40,44,45,46,47,48,49,50,51,52,54,56,57,58,67,70,71,72,85,86,92,95,117,119,120,121,122,123,124,125,126,127,128,129,130,149,150,151,183,186,],[-35,81,-29,-30,-31,-32,-33,-34,-36,-37,-38,81,-41,-40,81,81,81,81,-89,81,81,-39,81,-28,81,81,81,81,None,None,None,None,None,81,81,-93,81,-42,81,81,81,]),'IGUAL':([37,40,44,45,46,47,48,49,50,51,52,54,56,57,58,67,70,71,72,85,86,92,95,117,119,120,121,122,123,124,125,126,127,128,129,130,149,150,151,183,186,],[-35,82,-29,-30,-31,-32,-33,-34,-36,-37,-38,82,-41,-40,82,82,82,82,-89,82,82,-39,82,-28,82,82,82,82,None,None,None,None,None,82,82,-93,82,-42,82,82,82,]),'DISYUNCION':([37,40,44,45,46,47,48,49,50,51,52,54,56,57,58,67,70,71,72,85,86,92,95,117,119,120,121,122,123,124,125,126,127,128,129,130,149,150,151,183,186,],[-35,83,-29,-30,-31,-32,-33,-34,-36,-37,-38,83,-41,-40,83,83,83,83,-89,-26,-27,-39,83,-28,83,83,83,83,-19,-20,-21,-22,-23,-24,-25,-93,83,-42,83,83,83,]),'CONJUNCION':([37,40,44,45,46,47,48,49,50,51,52,54,56,57,58,67,70,71,72,85,86,92,95,117,119,120,121,122,123,124,125,126,127,128,129,130,149,150,151,183,186,],[-35,84,-29,-30,-31,-32,-33,-34,-36,-37,-38,84,-41,-40,84,84,84,84,-89,-26,-27,-39,84,-28,84,84,84,84,-19,-20,-21,-22,-23,-24,-25,-93,84,-42,84,84,84,]),'}':([37,44,45,46,47,48,49,50,51,52,56,57,64,68,72,85,86,87,88,92,102,104,105,107,111,112,113,115,117,119,120,121,122,123,124,125,126,127,128,129,130,135,136,144,145,146,147,148,149,150,152,155,157,158,159,160,161,164,165,166,168,170,187,189,],[-35,-29,-30,-31,-32,-33,-34,-36,-37,-38,-41,-40,-53,-55,-89,-26,-27,130,-95,-39,-54,144,-62,-65,-69,-70,-71,147,-28,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-93,152,-101,-59,-63,-64,-58,-94,-96,-42,-99,-109,-105,-106,-107,-108,-110,168,-100,-102,-61,181,-74,-73,]),']':([55,],[92,]),'RETURN':([64,68,102,144,147,168,169,171,174,178,179,180,184,185,188,],[-53,-55,-54,-59,-58,-61,172,182,-76,-82,-83,-84,-75,-78,-77,]),'ELSE':([65,144,],[103,-60,]),'INT':([140,154,162,],[157,157,157,]),'FLOAT':([140,154,162,],[158,158,158,]),'BOOLEAN':([140,154,162,],[159,159,159,]),'CHARACTER':([140,154,162,],[160,160,160,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'archivo':([0,],[1,]),'lineas':([0,5,20,],[2,21,36,]),'lambda':([0,22,63,73,142,],[3,41,101,41,101,]),'linea_normal':([0,5,20,],[4,4,4,]),'linea_especial':([0,5,20,],[5,5,5,]),'llamada_funcion':([0,5,20,22,23,26,33,35,38,42,43,61,66,69,73,74,75,76,77,78,79,80,81,82,83,84,105,132,134,143,169,172,174,182,184,],[6,6,6,51,51,51,51,51,51,51,51,51,108,108,51,51,51,51,51,51,51,51,51,51,51,51,108,51,51,108,175,51,175,51,175,]),'asignacion':([0,5,20,66,69,105,143,169,174,184,],[7,7,7,109,109,109,109,176,176,176,]),'declaracion':([0,5,20,66,69,105,143,169,174,184,],[8,8,8,110,110,110,110,177,177,177,]),'funcion':([0,5,20,],[11,11,11,]),'condicional':([0,5,20,66,69,105,143,169,174,184,],[12,12,12,113,113,113,113,180,180,180,]),'propiedad':([0,5,20,22,23,25,26,33,35,38,42,43,61,66,69,73,74,75,76,77,78,79,80,81,82,83,84,105,132,134,143,169,172,174,182,184,],[14,14,14,50,50,57,50,50,50,50,50,50,50,14,14,50,50,50,50,50,50,50,50,50,50,50,50,14,50,50,14,14,50,14,50,14,]),'lista_declaraciones':([15,59,],[27,93,]),'contenido_declaracion':([15,59,],[28,28,]),'condiciones':([18,],[32,]),'condiciones_while':([19,],[34,]),'parametros_funcion':([22,73,],[39,118,]),'expresion':([22,23,26,33,35,38,42,43,61,73,74,75,76,77,78,79,80,81,82,83,84,132,134,172,182,],[40,54,58,67,70,71,85,86,95,40,119,120,121,122,123,124,125,126,127,128,129,149,151,183,186,]),'objeto_expresion':([22,23,26,33,35,38,42,43,61,73,74,75,76,77,78,79,80,81,82,83,84,132,134,172,182,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'contenido_if':([32,],[64,]),'contenido_if_else':([32,],[65,]),'contenido_while':([34,],[68,]),'pares_expresion':([53,131,],[87,148,]),'par_expresion':([53,131,],[88,88,]),'clave_expresion':([53,131,],[89,89,]),'objeto_tipo':([62,140,154,162,],[96,161,161,161,]),'argumentos':([63,142,],[99,163,]),'argumento':([63,142,],[100,100,]),'contenido_else':([65,],[102,]),'lineas_cond':([66,69,105,143,],[104,115,145,164,]),'linea_cond':([66,69,105,143,],[105,105,105,105,]),'linea_normal_cond':([66,69,105,143,],[106,106,106,106,]),'linea_especial_cond':([66,69,105,143,],[107,107,107,107,]),'pares_tipo':([97,153,],[135,165,]),'par_tipo':([97,153,],[136,136,]),'clave_tipo':([97,153,],[137,137,]),'tipo':([140,154,162,],[156,166,167,]),'contenido_funcion':([169,],[170,]),'lineas_fun':([169,174,184,],[171,185,188,]),'linea_normal_fun':([169,174,184,],[173,173,173,]),'linea_especial_fun':([169,174,184,],[174,174,174,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> archivo","S'",1,None,None,None),
  ('archivo -> lineas','archivo',1,'p_archivo','sintactico.py',24),
  ('archivo -> lambda','archivo',1,'p_archivo','sintactico.py',25),
  ('lambda -> <empty>','lambda',0,'p_lambda','sintactico.py',28),
  ('lineas -> linea_normal ;','lineas',2,'p_lineas','sintactico.py',31),
  ('lineas -> linea_especial','lineas',1,'p_lineas','sintactico.py',32),
  ('lineas -> linea_normal ; lineas','lineas',3,'p_lineas','sintactico.py',33),
  ('lineas -> linea_especial lineas','lineas',2,'p_lineas','sintactico.py',34),
  ('linea_normal -> llamada_funcion','linea_normal',1,'p_linea_normal','sintactico.py',37),
  ('linea_normal -> asignacion','linea_normal',1,'p_linea_normal','sintactico.py',38),
  ('linea_normal -> declaracion','linea_normal',1,'p_linea_normal','sintactico.py',39),
  ('linea_especial -> COM_MULTI','linea_especial',1,'p_linea_especial','sintactico.py',42),
  ('linea_especial -> COM_SIMPLE','linea_especial',1,'p_linea_especial','sintactico.py',43),
  ('linea_especial -> funcion','linea_especial',1,'p_linea_especial','sintactico.py',44),
  ('linea_especial -> condicional','linea_especial',1,'p_linea_especial','sintactico.py',45),
  ('expresion -> expresion + expresion','expresion',3,'p_expresion_binop','sintactico.py',48),
  ('expresion -> expresion - expresion','expresion',3,'p_expresion_binop','sintactico.py',49),
  ('expresion -> expresion * expresion','expresion',3,'p_expresion_binop','sintactico.py',50),
  ('expresion -> expresion / expresion','expresion',3,'p_expresion_binop','sintactico.py',51),
  ('expresion -> expresion < expresion','expresion',3,'p_expresion_binop','sintactico.py',52),
  ('expresion -> expresion > expresion','expresion',3,'p_expresion_binop','sintactico.py',53),
  ('expresion -> expresion MAYORIG expresion','expresion',3,'p_expresion_binop','sintactico.py',54),
  ('expresion -> expresion MENORIG expresion','expresion',3,'p_expresion_binop','sintactico.py',55),
  ('expresion -> expresion IGUAL expresion','expresion',3,'p_expresion_binop','sintactico.py',56),
  ('expresion -> expresion DISYUNCION expresion','expresion',3,'p_expresion_binop','sintactico.py',57),
  ('expresion -> expresion CONJUNCION expresion','expresion',3,'p_expresion_binop','sintactico.py',58),
  ('expresion -> - expresion','expresion',2,'p_expresion_uminus','sintactico.py',66),
  ('expresion -> ! expresion','expresion',2,'p_expresion_not','sintactico.py',71),
  ('expresion -> ( expresion )','expresion',3,'p_expresion_grupo','sintactico.py',79),
  ('expresion -> ENTERO','expresion',1,'p_expresion_parametro','sintactico.py',83),
  ('expresion -> REAL','expresion',1,'p_expresion_parametro','sintactico.py',84),
  ('expresion -> TR','expresion',1,'p_expresion_parametro','sintactico.py',85),
  ('expresion -> FL','expresion',1,'p_expresion_parametro','sintactico.py',86),
  ('expresion -> NULL','expresion',1,'p_expresion_parametro','sintactico.py',87),
  ('expresion -> CARACTER','expresion',1,'p_expresion_parametro','sintactico.py',88),
  ('expresion -> IDENTIFIER','expresion',1,'p_expresion_parametro','sintactico.py',89),
  ('expresion -> propiedad','expresion',1,'p_expresion_parametro','sintactico.py',90),
  ('expresion -> llamada_funcion','expresion',1,'p_expresion_parametro','sintactico.py',91),
  ('expresion -> objeto_expresion','expresion',1,'p_expresion_parametro','sintactico.py',92),
  ('propiedad -> IDENTIFIER [ STRING ]','propiedad',4,'p_propiedad_exp','sintactico.py',98),
  ('propiedad -> IDENTIFIER . propiedad','propiedad',3,'p_propiedad_exp','sintactico.py',99),
  ('propiedad -> IDENTIFIER . IDENTIFIER','propiedad',3,'p_propiedad_exp','sintactico.py',100),
  ('propiedad -> IDENTIFIER [ STRING ] . IDENTIFIER','propiedad',6,'p_propiedad_exp','sintactico.py',101),
  ('asignacion -> IDENTIFIER = expresion','asignacion',3,'p_asignacion','sintactico.py',109),
  ('asignacion -> propiedad = expresion','asignacion',3,'p_asignacion','sintactico.py',110),
  ('declaracion -> LET lista_declaraciones','declaracion',2,'p_declaracion','sintactico.py',118),
  ('declaracion -> TYPE IDENTIFIER = objeto_tipo','declaracion',4,'p_declaracion','sintactico.py',119),
  ('lista_declaraciones -> contenido_declaracion','lista_declaraciones',1,'p_lista_declaraciones','sintactico.py',127),
  ('lista_declaraciones -> contenido_declaracion , lista_declaraciones','lista_declaraciones',3,'p_lista_declaraciones','sintactico.py',128),
  ('contenido_declaracion -> IDENTIFIER','contenido_declaracion',1,'p_contenido_declaracion','sintactico.py',132),
  ('contenido_declaracion -> IDENTIFIER : IDENTIFIER','contenido_declaracion',3,'p_contenido_declaracion','sintactico.py',133),
  ('contenido_declaracion -> IDENTIFIER : IDENTIFIER = expresion','contenido_declaracion',5,'p_contenido_declaracion','sintactico.py',134),
  ('contenido_declaracion -> IDENTIFIER = expresion','contenido_declaracion',3,'p_contenido_declaracion','sintactico.py',135),
  ('condicional -> IF condiciones contenido_if','condicional',3,'p_condicional','sintactico.py',141),
  ('condicional -> IF condiciones contenido_if_else contenido_else','condicional',4,'p_condicional','sintactico.py',142),
  ('condicional -> WHILE condiciones_while contenido_while','condicional',3,'p_condicional','sintactico.py',143),
  ('condiciones -> ( expresion )','condiciones',3,'p_condiciones','sintactico.py',148),
  ('condiciones_while -> ( expresion )','condiciones_while',3,'p_condiciones_while','sintactico.py',154),
  ('contenido_while -> { lineas_cond }','contenido_while',3,'p_contenido_while','sintactico.py',159),
  ('contenido_if -> { lineas_cond }','contenido_if',3,'p_contenido_if','sintactico.py',162),
  ('contenido_if_else -> { lineas_cond }','contenido_if_else',3,'p_contenido_if_else','sintactico.py',166),
  ('contenido_else -> ELSE { lineas_cond }','contenido_else',4,'p_contenido_else','sintactico.py',170),
  ('lineas_cond -> linea_cond','lineas_cond',1,'p_lineas_cond','sintactico.py',175),
  ('lineas_cond -> linea_cond lineas_cond','lineas_cond',2,'p_lineas_cond','sintactico.py',176),
  ('linea_cond -> linea_normal_cond ;','linea_cond',2,'p_linea_cond','sintactico.py',180),
  ('linea_cond -> linea_especial_cond','linea_cond',1,'p_linea_cond','sintactico.py',181),
  ('linea_normal_cond -> llamada_funcion','linea_normal_cond',1,'p_linea_normal_cond','sintactico.py',185),
  ('linea_normal_cond -> asignacion','linea_normal_cond',1,'p_linea_normal_cond','sintactico.py',186),
  ('linea_normal_cond -> declaracion','linea_normal_cond',1,'p_linea_normal_cond','sintactico.py',187),
  ('linea_especial_cond -> COM_MULTI','linea_especial_cond',1,'p_linea_especial_cond','sintactico.py',191),
  ('linea_especial_cond -> COM_SIMPLE','linea_especial_cond',1,'p_linea_especial_cond','sintactico.py',192),
  ('linea_especial_cond -> condicional','linea_especial_cond',1,'p_linea_especial_cond','sintactico.py',193),
  ('funcion -> FUNCTION IDENTIFIER ( argumentos ) : tipo { contenido_funcion }','funcion',10,'p_funcion','sintactico.py',199),
  ('contenido_funcion -> lineas_fun RETURN expresion ;','contenido_funcion',4,'p_contenido_funcion','sintactico.py',207),
  ('contenido_funcion -> RETURN expresion ;','contenido_funcion',3,'p_contenido_funcion','sintactico.py',208),
  ('lineas_fun -> linea_normal_fun ;','lineas_fun',2,'p_lineas_fun','sintactico.py',214),
  ('lineas_fun -> linea_especial_fun','lineas_fun',1,'p_lineas_fun','sintactico.py',215),
  ('lineas_fun -> linea_normal_fun ; lineas_fun','lineas_fun',3,'p_lineas_fun','sintactico.py',216),
  ('lineas_fun -> linea_especial_fun lineas_fun','lineas_fun',2,'p_lineas_fun','sintactico.py',217),
  ('linea_normal_fun -> llamada_funcion','linea_normal_fun',1,'p_linea_normal_fun','sintactico.py',220),
  ('linea_normal_fun -> asignacion','linea_normal_fun',1,'p_linea_normal_fun','sintactico.py',221),
  ('linea_normal_fun -> declaracion','linea_normal_fun',1,'p_linea_normal_fun','sintactico.py',222),
  ('linea_especial_fun -> COM_MULTI','linea_especial_fun',1,'p_linea_especial_fun','sintactico.py',225),
  ('linea_especial_fun -> COM_SIMPLE','linea_especial_fun',1,'p_linea_especial_fun','sintactico.py',226),
  ('linea_especial_fun -> condicional','linea_especial_fun',1,'p_linea_especial_fun','sintactico.py',227),
  ('argumentos -> argumento','argumentos',1,'p_argumentos','sintactico.py',232),
  ('argumentos -> argumento , argumentos','argumentos',3,'p_argumentos','sintactico.py',233),
  ('argumentos -> lambda','argumentos',1,'p_argumentos','sintactico.py',234),
  ('argumento -> IDENTIFIER : tipo','argumento',3,'p_argumento','sintactico.py',242),
  ('llamada_funcion -> IDENTIFIER ( parametros_funcion )','llamada_funcion',4,'p_llamada_funcion','sintactico.py',247),
  ('parametros_funcion -> expresion','parametros_funcion',1,'p_parametros_funcion','sintactico.py',253),
  ('parametros_funcion -> expresion , parametros_funcion','parametros_funcion',3,'p_parametros_funcion','sintactico.py',254),
  ('parametros_funcion -> lambda','parametros_funcion',1,'p_parametros_funcion','sintactico.py',255),
  ('objeto_expresion -> { pares_expresion }','objeto_expresion',3,'p_objeto_expresion','sintactico.py',263),
  ('pares_expresion -> par_expresion , pares_expresion','pares_expresion',3,'p_pares_expresion','sintactico.py',267),
  ('pares_expresion -> par_expresion','pares_expresion',1,'p_pares_expresion','sintactico.py',268),
  ('par_expresion -> clave_expresion : expresion','par_expresion',3,'p_par_expresion','sintactico.py',275),
  ('clave_expresion -> IDENTIFIER','clave_expresion',1,'p_clave_expresion','sintactico.py',279),
  ('clave_expresion -> STRING','clave_expresion',1,'p_clave_expresion','sintactico.py',280),
  ('objeto_tipo -> { pares_tipo }','objeto_tipo',3,'p_objeto_tipo','sintactico.py',284),
  ('pares_tipo -> par_tipo , pares_tipo','pares_tipo',3,'p_pares_tipo','sintactico.py',288),
  ('pares_tipo -> par_tipo','pares_tipo',1,'p_pares_tipo','sintactico.py',289),
  ('par_tipo -> clave_tipo : tipo','par_tipo',3,'p_par_tipo','sintactico.py',296),
  ('clave_tipo -> IDENTIFIER','clave_tipo',1,'p_clave_tipo','sintactico.py',300),
  ('clave_tipo -> STRING','clave_tipo',1,'p_clave_tipo','sintactico.py',301),
  ('tipo -> INT','tipo',1,'p_tipo','sintactico.py',305),
  ('tipo -> FLOAT','tipo',1,'p_tipo','sintactico.py',306),
  ('tipo -> BOOLEAN','tipo',1,'p_tipo','sintactico.py',307),
  ('tipo -> CHARACTER','tipo',1,'p_tipo','sintactico.py',308),
  ('tipo -> IDENTIFIER','tipo',1,'p_tipo','sintactico.py',309),
  ('tipo -> objeto_tipo','tipo',1,'p_tipo','sintactico.py',310),
]
