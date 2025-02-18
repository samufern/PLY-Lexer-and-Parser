from excepciones import *

simbolos = {}
registros = {}

class FuncionesSemantico:
    def tipo_valor(self, var):
        if var in simbolos:
            var_valor = simbolos[var]["valor"]
            var_tipo = simbolos[var]["tipo"]
        else:
            var_valor = var
            var_tipo = self.tipo_variable(var)
        return var_valor, var_tipo


    def comprobar_tipos(self, p):
        var1 = p[1]
        var2 = p[3]
        operador = p[2]
        valor_var1 , tipo_var1 = self.tipo_valor(var1)
        valor_var2, tipo_var2 = self.tipo_valor(var2)
        if operador in ["+", "-", "<", ">", "<=", ">="]:
            if tipo_var1 in ["int", "float", "character"] and tipo_var2 in ["int", "float", "character"]:
                if tipo_var1 == tipo_var2:
                    return True
                else:
                    if tipo_var1 == "character":
                        return self.comprobar_character(p, tipo_var2, valor_var1, var1)
                    if tipo_var2 == "character":
                        return self.comprobar_character(p, tipo_var1, valor_var2, var2)
                    if tipo_var1 == "int" and tipo_var2 == "float":
                        return self.int_to_float(p, valor_var1, var1)
                    if tipo_var1 == "float" and tipo_var2 == "int":
                        return self.int_to_float(p, valor_var2, var2)

        if operador in ["*", "/"]:
            if tipo_var1 in ["int", "float"] and tipo_var2 in ["int", "float"]:
                if tipo_var1 == tipo_var2:
                    return True
                else:
                    if tipo_var1 == "int" and tipo_var2 == "float":
                        return self.int_to_float(p, valor_var1, var1)
                    if tipo_var1 == "float" and tipo_var2 == "int":
                        return self.int_to_float(p, valor_var2, var2)
        if operador == "==":
            if tipo_var1 in ["int", "float", "character", "boolean"] and tipo_var2 in ["int", "float", "character", "boolean"]:
                if tipo_var1 == tipo_var2:
                    return True
                else:
                    if tipo_var1 == "character":
                        return self.comprobar_character(p, tipo_var2, valor_var1, var1)
                    if tipo_var2 == "character":
                        return self.comprobar_character(p, tipo_var1, valor_var2, var2)
                    if tipo_var1 == "int" and tipo_var2 == "float":
                        return self.int_to_float(p, valor_var1, var1)
                    if tipo_var1 == "float" and tipo_var2 == "int":
                        return self.int_to_float(p, valor_var2, var2)
        if operador in ["&&", "||"]:
            if tipo_var1 == "boolean" and tipo_var2 == "boolean":
                return True
        return False

    def int_to_float(self, p, valor_var1, var1):
        if var1 in simbolos:
            simbolos[var1]["tipo"] = "float"
            simbolos[var1]["valor"] = float(valor_var1)
            return True
        else:
            p[1] = float(p[1])
            return True

    def comprobar_character(self, p, tipo_varB, valor_varA, varA):
        if varA in simbolos:
            simbolos[varA]["tipo"] = tipo_varB
            simbolos[varA]["valor"] = ord(valor_varA)
            return True
        else:
            p[1] = ord(valor_varA)
            if tipo_varB == "float":
                p[1] = float(ord(valor_varA))
            return True

    def tipo_variable(self, variable):
        if type(variable) != list and variable in simbolos:
            tipo = simbolos[variable]["tipo"]
            return tipo
        if type(variable) == int:
            tipo = "int"
            return tipo
        elif variable in ["tr", "fl"]:
            tipo = "boolean"
            return tipo
        elif type(variable) == str and variable not in ["tr", "fl"]:
            if "." in variable:
                valor_lista = variable.split(".")
                if valor_lista[0] in simbolos:
                    simbolo = simbolos[valor_lista[0]]
                    if len(valor_lista) == 2:
                        for i in range(len(simbolo["valor"])):
                            if simbolo["valor"][i]["nombre"] == valor_lista[1]:
                                valor = simbolo["valor"][i]["valor"]
                                tipo = self.tipo_variable(valor)
                                return tipo
                    if len(valor_lista) == 3:
                        for i in range(len(simbolo["valor"])):
                            if simbolo["valor"][i]["nombre"] in valor_lista:
                                for ii in range(len(simbolo["valor"][i]["valor"])):
                                    if simbolo["valor"][i]["valor"][ii]["nombre"] in valor_lista:
                                        valor = simbolo["valor"][i]["valor"][ii]["valor"]
                                        tipo = self.tipo_variable(valor)
                                        return tipo

            else:
                tipo = "character"
                return tipo
        elif type(variable) == float:
            tipo = "float"
            return tipo
        elif type(variable) == list:
            estructura_objeto = []
            for i in range(len(variable)):
                nombre_elemento = variable[i]["nombre"]
                valor_elemento = variable[i]["valor"]
                tipo_elemento = self.tipo_variable(valor_elemento)
                estructura_objeto.append({"nombre":nombre_elemento, "tipo":tipo_elemento})
            for clave, valor in registros.items():
                if len(valor) > 1:
                    for item in valor:
                        if item["tipo"] == estructura_objeto:
                            tipo = item["tipo"]
                            return tipo
                elif estructura_objeto == valor:
                    tipo = clave
                    return tipo
                else:
                    for i in range(len(valor)):
                        if estructura_objeto == valor[i]["tipo"]:
                            tipo = valor[i]["tipo"]
                            return tipo



    def logica_declaraciones(self, p):
        if len(p) == 2:
            p[0] = p[1]
            simbolos.setdefault(p[1], {"tipo":"null", "valor":"null"})
        if len(p) == 4:
            p[0] = p[1], p[3]
            valor = p[3]
            tipo = self.tipo_variable(valor)
            if type(p[3]) == str and "." in p[3]:
                variable = p[3]
                valor_lista = variable.split(".")
                if valor_lista[0] in simbolos:
                    simbolo = simbolos[valor_lista[0]]
                    if len(valor_lista) == 2:
                        for i in range(len(simbolo["valor"])):
                            if simbolo["valor"][i]["nombre"] == valor_lista[1]:
                                valor = simbolo["valor"][i]["valor"]
                                tipo = self.tipo_variable(valor)
                    if len(valor_lista) == 3:
                        for i in range(len(simbolo["valor"])):
                            if simbolo["valor"][i]["nombre"] in valor_lista:
                                for ii in range(len(simbolo["valor"][i]["valor"])):
                                    if simbolo["valor"][i]["valor"][ii]["nombre"] in valor_lista:
                                        valor = simbolo["valor"][i]["valor"][ii]["valor"]
                                        tipo = self.tipo_variable(valor)
            if ":" in p:
                tipo = p[3]
                valor = "null"
            if p[1] in simbolos:
                raise KeyAlreadyExistsError(p[1])
            simbolos.setdefault(p[1], {"tipo":tipo, "valor":valor})
        if len(p) == 6:
            if p[3] not in registros:
                raise TypeDoesNotExistError(p[3])
            if p[1] in simbolos:
                raise KeyAlreadyExistsError(p[1])
            for i in range(len(p[5])):
                variable = p[5][i]
                tipo_declarado = registros[p[3]][i]["tipo"]
                tipo_variable = self.tipo_variable(variable["valor"])
                if tipo_variable != tipo_declarado:
                    raise TypeNotEqual(p[3])
            simbolos.setdefault(p[1],{"tipo":p[3],"valor":p[5]})



    def logica_asignaciones(self, p):
        if type(p[3]) == list:
            if p[1] not in simbolos:
                raise VariableDoesNotExistError(p[1])
            variable = simbolos[p[1]]
            if variable["tipo"] == "null":
                variable["tipo"] = self.tipo_variable(p[3])
                variable["valor"] = p[3]
            tipo = variable["tipo"]
            if tipo not in registros:
                raise TypeDoesNotExistError(tipo)
            variable["valor"] = p[3]
            for i in range(len(p[3])):
                var = p[3][i]
                if self.tipo_variable(var["valor"]) != registros[tipo][i]["tipo"]:
                    raise TypeNotEqual(tipo)
        else:
            if p[1] not in simbolos:
                if "." in p[1]:
                    valor_lista = p[1].split(".")
                    variable = valor_lista[0]
                    propiedad = valor_lista[1]
                    if variable in simbolos:
                        simbolo = simbolos[valor_lista[0]]
                        for i in range(1, len(simbolo)):
                            propiedad_buscada = simbolo[i]["tipo"]
                            if propiedad_buscada == propiedad:
                                tipo_nuevo = self.tipo_variable(p[3])
                                tipo_antiguo = self.tipo_variable(simbolo[i]["valor"])
                                if tipo_antiguo == tipo_nuevo:
                                    simbolo[i]["valor"] = p[3]
                                else:
                                    raise TypeNotEqual(p[1])
                else:
                    raise VariableDoesNotExistError(p[1])
            else:
                variable = simbolos[p[1]]
                if variable["tipo"] == "null":
                    variable["tipo"] = self.tipo_variable(p[3])
                    variable["valor"] = p[3]
                else:
                    tipo_reasignacion = self.tipo_variable(p[3])
                    if tipo_reasignacion == variable["tipo"]:
                        variable["tipo"] = tipo_reasignacion
                        variable["valor"] = p[3]
                    else:
                        raise TypeNotEqual(p[1])


    def logica_expresiones(self, p):
        if len(p) == 2:
            p[0] = p[1]
        if len(p) == 4:
            tipos_comprobados = self.comprobar_tipos(p)
            var_1_valor, var_1_tipo = self.tipo_valor(p[1])
            var_2_valor, var_2_tipo = self.tipo_valor(p[3])
            if var_1_valor == "null" or var_2_valor == "null":
                raise OperationNotPossibleNull()
            if p[2] == "+" and tipos_comprobados is True:
                p[0] = var_1_valor + var_2_valor
            if p[2] == "-" and tipos_comprobados is True:
                p[0] = var_1_valor - var_2_valor
            if p[2] == "*" and tipos_comprobados is True:
                p[0] = var_1_valor * var_2_valor
            if p[2] == "/" and tipos_comprobados is True:
                p[0] = var_1_valor / var_2_valor
            if p[2] == "<" and tipos_comprobados is True:
                resultado = var_1_valor < var_2_valor
                resultado_traducido = self.traducir_resultado(resultado)
                p[0] = resultado_traducido
            if p[2] == ">" and tipos_comprobados is True:
                resultado = var_1_valor > var_2_valor
                resultado_traducido = self.traducir_resultado(resultado)
                p[0] = resultado_traducido
            if p[2] == "<=" and tipos_comprobados is True:
                resultado = var_1_valor <= var_2_valor
                resultado_traducido = self.traducir_resultado(resultado)
                p[0] = resultado_traducido
            if p[2] == ">=" and tipos_comprobados is True:
                resultado = var_1_valor >= var_2_valor
                resultado_traducido = self.traducir_resultado(resultado)
                p[0] = resultado_traducido
            if p[2] == "==" and tipos_comprobados is True:
                if p[1] in simbolos:
                    valor = simbolos[p[1]]["valor"]
                    if valor == p[3]:
                        p[0] = "tr"
                    else:
                        p[0] = "fl"
            if p[2] == "&&" and tipos_comprobados is True:
                if var_1_valor == "tr" and var_2_valor == "tr":
                    p[0] = "tr"
                else:
                    p[0] = "fl"
            if p[2] == "||" and tipos_comprobados is True:
                if var_1_valor == "tr" or var_2_valor == "tr":
                    p[0] = "tr"
                else:
                    p[0] = "fl"
        # self.print_pila(p)

    def traducir_resultado(self, resultado):
        if resultado == True:
            resultado_traducido = "tr"
            return resultado_traducido
        if resultado == False:
            resultado_traducido = "fl"
            return resultado_traducido

    def construir_nombre(self, p):
        nombre_funcion = p[2]
        nombre_funcion += "," + str(len(p[4])) + ","
        nombre_funcion += "("
        for i in range(len(p[4])):
            argumento = p[4][i]
            if argumento:
                if i == len(p[4]) - 1:
                    nombre_funcion += argumento["tipo"]
                else:
                    nombre_funcion += argumento["tipo"] + ","
        nombre_funcion += ")"

        return nombre_funcion

    def logica_llamadas(self, p):
        nombre_funcion = self.reconstruir_nombre(p)
        for i in range(len(p[3])):
            variable = p[3][i]
            tipo = self.tipo_variable(variable)
            if tipo:
                tipo_declarado = registros[nombre_funcion]["valor"][i]["tipo"]
                if tipo != tipo_declarado:
                    raise TypeNotEqual(registros[p[1]])
        if nombre_funcion not in registros:
            raise FunctionNotDeclared(p[1])

    def reconstruir_nombre(self, p):
        nombre_funcion = p[1]
        nombre_funcion += "," + str(len(p[3])) + ","
        nombre_funcion += "("
        for i in range(len(p[3])):
            variable = p[3][i]
            tipo = self.tipo_variable(variable)
            if tipo:
                if i == len(p[3]) - 1:
                    nombre_funcion += tipo
                else:
                    nombre_funcion += tipo + ","
        nombre_funcion += ")"
        return nombre_funcion

    def logica_funciones(self, p):
        nombre_funcion = self.construir_nombre(p)
        if p[7] != p[9]:
            raise TypeNotEqual(p[2])
        registros.setdefault(nombre_funcion, {"tipo":p[7], "valor":p[4]})

    def logica_return(self, p):
        if len(p) == 5:
            tipo = self.tipo_variable(p[3])
            p[0] = tipo
        if len(p) == 4:
            tipo = self.tipo_variable(p[2])
            p[0] = tipo

    def logica_type(self, p):
        if "type" in p:
            registros.setdefault(p[2], p[4])

    def logica_condicionales(self, p):
        if self.tipo_variable(p[2]) != "boolean":
            raise TypeNotBoolean(p[2])


    def print_pila(self,pila):
        lista_pila = []
        for item in pila:
            lista_pila.append(item)
        print(lista_pila)
