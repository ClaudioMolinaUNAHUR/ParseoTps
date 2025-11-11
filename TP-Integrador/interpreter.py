class SymbolTable:
    """
    Esta clase representa la tabla de simbolos
    """

    def __init__(self):
        self.scopes = [{}]  # Comienza con un ámbito global.

    def enter_scope(self):
        """Entra en un nuevo ámbito (por ejemplo, al llamar a una función o entrar en un bucle)."""
        self.scopes.append({})

    def exit_scope(self):
        """Sale del ámbito actual."""
        if len(self.scopes) > 1:
            self.scopes.pop()

    def agregar(self, name, value):
        """Establece una variable en el ámbito actual (el más interno)."""
        self.scopes[-1][name] = value

    def obtener(self, name):
        """Obtiene una variable, buscando desde el ámbito más interno hasta el más externo."""
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise NameError(f"Name '{name}' is not defined.")

    def actualizar(self, name, value):
        """Actualiza una variable existente en el ámbito más cercano donde se encuentra."""
        for scope in reversed(self.scopes):
            if name in scope:
                scope[name] = value
                return
        raise NameError(f"Cannot assign to name '{name}' because it is not defined.")


class Interpreter:
    """
    El intérprete recorre el AST producido por el analizador sintáctico y lo ejecuta.
    Utiliza una SymbolTable para gestionar las variables y los ámbitos de las funciones.
    La lógica de ejecución se delega en el método `execute` de cada nodo del AST.
    """

    def __init__(self):
        self.symbol_table = SymbolTable()

    def execute(self, node):
        """Método público para iniciar la interpretación."""
        if node:
            return node.execute(self.symbol_table)
        return None
