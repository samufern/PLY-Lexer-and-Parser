import funciones_semantico
codigo_intermedio_lista = []
codigo_intermedio_lista_if = []
codigo_intermedio_lista_label1 = []
codigo_intermedio_lista_label2 = []
codigo_intermedio_dic = {}
class CodigoIntermedio:
    def __init__(self):
        self.t = 1
        self.label = 1
    def codigo_intermedio_expresiones(self, p):
        nombre_variable_temporal = "t"+str(self.t)
        operador = p[2]
        op1 = p[1]
        op2 = p[3]
        cuarteto = [operador, op1, op2, nombre_variable_temporal]
        codigo_intermedio_lista.append(cuarteto)
        codigo_intermedio_dic.update({nombre_variable_temporal:p[0]})
        self.t += 1

    def codigo_intermedio_asignaciones(self, p):
        operador = p[2]
        variable = p[1]
        valor = p[3]
        cuarteto = [operador, valor, ' ', variable]
        codigo_intermedio_lista.append(cuarteto)

    def codigo_intermedio_ifs(self, p):
        label = "L" + str(self.label)
        gotoc = ['gotoc','t1' ,label, '']
        l1 = ['label' , label, '', '']
        self.label += 1
        goto = ['goto', label, '', '']
        codigo_intermedio_lista.append(gotoc)
        codigo_intermedio_lista.append(goto)
        codigo_intermedio_lista.append(l1)
        # self.print_pila(p)

    def codigo_intermedio_else(self, p):
        label_value = self.label - 2
        label = "L" + str(label_value)
        goto = ['goto', label, '', '']
        label = "L" + str(self.label)
        l2 = ['label', label, '', '']
        codigo_intermedio_lista.append(goto)
        codigo_intermedio_lista.append(l2)

    def codigo_intermedio_label0_if(self, p):
        label_value = self.label - 2
        label = "L" + str(label_value)
        l0 = ['label', label, '', '']
        codigo_intermedio_lista.append(l0)
        self.label += 1

    def codigo_intermedio_label0_else(self, p):
        label_value = self.label - 2
        label = "L" + str(label_value)
        l0 = ['label', label, '', '']
        codigo_intermedio_lista.append(l0)
        self.label += 2

    def codigo_intermedio_ifs(self, p):
        # self.print_pila(p)
        label0 = ("label", "L0", '','')
        label1 = ("label", "L1", '', '')
        label2 = ("label", "L2", '', '')
        gotoc = ('gotoc', 't1', 'L1', '')
        gotol2 = ('goto', 'L2', '' ,'')
        gotol0 =  ('goto', 'L0', '' ,'')
        if "if" in p:
            codigo_intermedio_lista_if.append(gotoc)
            codigo_intermedio_lista_if.append(gotol2)
            codigo_intermedio_lista_label1.append(label1)
            codigo_intermedio_lista_label1.append(gotol0)
        if "else" in p:
            codigo_intermedio_lista_label2.append(label2)
            codigo_intermedio_lista_label2.append(label0)



    def procesar_datos(self):
        for key, value in codigo_intermedio_dic.items():
            for i in range(len(codigo_intermedio_lista)):
                if value == codigo_intermedio_lista[i][1] and value not in ["tr", "fl"]:
                    codigo_intermedio_lista[i][1] = key
                if value == codigo_intermedio_lista[i][2] and value not in ["tr", "fl"]:
                    codigo_intermedio_lista[i][2] = key
                if codigo_intermedio_lista[i][0] == "gotoc":
                    codigo_intermedio_lista[i][1] = codigo_intermedio_lista[i-1][3]
        print(codigo_intermedio_lista_if)
        print(codigo_intermedio_lista_label1)
        print(codigo_intermedio_lista_label2)
        with open('codigo_intermedio.out', 'w') as file:
            for item in codigo_intermedio_lista:
                file.write(str(tuple(item))+'\n')

    def print_pila(self,pila):
        lista_pila = []
        for item in pila:
            lista_pila.append(item)
        print(lista_pila)