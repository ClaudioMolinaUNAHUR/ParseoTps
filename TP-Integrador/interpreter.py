class SymbolTable:
    """
    Manages scopes and symbols (variables, functions).
    """

    def __init__(self):
        self.scopes = [{}]  # Start with a global scope.

    def enter_scope(self):
        """Enters a new scope (e.g., when calling a function or entering a loop)."""
        self.scopes.append({})

    def exit_scope(self):
        """Exits the current scope."""
        if len(self.scopes) > 1:
            self.scopes.pop()

    def set(self, name, value):
        """Sets a variable in the current (innermost) scope."""
        self.scopes[-1][name] = value

    def get(self, name):
        """Gets a variable, searching from the innermost scope to the outermost."""
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise NameError(f"Name '{name}' is not defined.")

    def update(self, name, value):
        """Updates an existing variable in the nearest scope where it is found."""
        for scope in reversed(self.scopes):
            if name in scope:
                scope[name] = value
                return
        raise NameError(f"Cannot assign to name '{name}' because it is not defined.")


class Interpreter:
    """
    The interpreter traverses the AST produced by the parser and executes it.
    It uses a SymbolTable to manage variables and function scopes.
    The execution logic is delegated to the `execute` method of each AST node.
    """

    def __init__(self):
        self.symbol_table = SymbolTable()

    def execute(self, node):
        """Public method to start interpretation."""
        if node:
            return node.execute(self.symbol_table)
        return None
