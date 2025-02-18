
class TypeDoesNotExistError(Exception):
    def __init__(self, key, message="El tipo no ha sido declarado"):
        self.key = key
        self.message = message
        super().__init__(self.message)

class TypeNotEqual(Exception):
    def __init__(self, key, message="El tipo del parametro no coincide con el declarado"):
        self.key = key
        self.message = message
        super().__init__(self.message)

class TypeNotBoolean(Exception):
    def __init__(self, key, message="El tipo del parametro no es booleano"):
        self.key = key
        self.message = message
        super().__init__(self.message)

class VariableDoesNotExistError(Exception):
    def __init__(self, key, message="La variable no ha sido declarada"):
        self.key = key
        self.message = message
        super().__init__(self.message)

class FunctionNotDeclared(Exception):
    def __init__(self, key, message="La funcion no existe"):
        self.key = key
        self.message = message
        super().__init__(self.message)

class KeyAlreadyExistsError(Exception):
    def __init__(self, key, message="La variable ya ha sido declarada"):
        self.key = key
        self.message = message
        super().__init__(self.message)

class OperationNotPossibleNull(Exception):
    def __init__(self, message="No se puede operar con variables nulas"):
        self.message = message
        super().__init__(self.message)

class ObjectNotDecalred(Exception):
    def __init__(self, message="Objeto no declarado"):
        self.message = message
        super().__init__(self.message)