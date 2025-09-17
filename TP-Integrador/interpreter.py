class SymbolTable:
    """
    Manages scopes and symbols (variables, functions).
    """
    def __init__(self):
        # The symbol table is a stack of dictionaries, where each dictionary represents a scope.
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
    def __init__(self):
        self.symbol_table = SymbolTable()

    def execute(self, node):
        """Public method to start interpretation."""
        return self._visit(node)

    def _visit(self, node):
        """Main dispatch method that calls the appropriate visitor function."""
        if not isinstance(node, tuple):
            # Handle lists of statements
            if isinstance(node, list):
                result = None
                for statement in node:
                    result = self._visit(statement)
                return result
            return node

        node_type = node[0]
        method_name = f'_visit_{node_type}'
        method = getattr(self, method_name, self._generic_visit)
        return method(node)

    def _generic_visit(self, node):
        raise NotImplementedError(f"No _visit_{node[0]} method implemented")

    def _visit_program(self, node):
        # ('program', statements)
        self._visit(node[1])

    def _visit_var(self, node):
        # ('var', type_info, name, value_expr)
        _, _, var_name, value_expr = node
        value = self._visit(value_expr)
        self.symbol_table.set(var_name, value)

    def _visit_assign(self, node):
        # ('assign', name, value_expr)
        _, var_name, value_expr = node
        value = self._visit(value_expr)
        self.symbol_table.update(var_name, value)

    def _visit_binary_op(self, node):
        # ('binary_op', left, op, right)
        _, left_node, op, right_node = node
        left_val = self._visit(left_node)
        right_val = self._visit(right_node)

        # Type coercion for string concatenation
        if op == '+':
            if isinstance(left_val, str) or isinstance(right_val, str):
                return str(left_val) + str(right_val)
        
        if op == '+': 
            if left_val is None or right_val is None:
                raise TypeError("Operands for '+' cannot be None")
            return left_val + right_val
        if op == '-': 
            if left_val is None or right_val is None:
                raise TypeError("Operands for '-' cannot be None")
            return left_val - right_val
        if op == '*': 
            if left_val is None or right_val is None:
                raise TypeError("Operands for '*' cannot be None")
            return left_val * right_val
        if op == '/': 
            if left_val is None or right_val is None:
                raise TypeError("Operands for '/' cannot be None")
            return left_val / right_val
        if op == '>': 
            if left_val is None or right_val is None:
                raise TypeError("Operands for '>' cannot be None")
            return left_val > right_val
        if op == '<': 
            if left_val is None or right_val is None:
                raise TypeError("Operands for '<' cannot be None")
            return left_val < right_val
        if op == '>=': 
            if left_val is None or right_val is None:
                raise TypeError("Operands for '>=' cannot be None")
            return left_val >= right_val
        if op == '<=': 
            if left_val is None or right_val is None:
                raise TypeError("Operands for '<=' cannot be None")
            return left_val <= right_val
        if op == '==': return left_val == right_val
        if op == '!=': return left_val != right_val
        if op == '&': return left_val and right_val
        if op == '|': return left_val or right_val
        raise TypeError(f"Unsupported operand types for {op}: {type(left_val)} and {type(right_val)}")

    def _visit_unary_op(self, node):
        # ('unary_op', op, expr)
        _, op, expr_node = node
        value = self._visit(expr_node)
        if op == '!':
            return not value
        raise TypeError(f"Unsupported unary operator: {op}")

    def _visit_boolean(self, node):
        # ('boolean', value)
        return node[1]

    def _visit_primitive(self, node):
        # ('primitive', value)
        # This now only handles numbers and strings
        return node[1]

    def _visit_id(self, node):
        # ('id', name)
        return self.symbol_table.get(node[1])

    def _visit_list(self, node):
        # ('list', [items])
        _, items = node
        return [self._visit(item) for item in items]

    def _visit_console(self, node):
        # ('console', [args])
        _, args = node
        evaluated_args = [self._visit(arg) for arg in args]
        print(*evaluated_args)

    def _visit_function(self, node):
        # ('function', name, params, body)
        self.symbol_table.set(node[1], node)

    def _visit_function_return(self, node):
        # ('function_return', name, params, return_type, body, return_expr)
        self.symbol_table.set(node[1], node)

    def _visit_call_func(self, node):
        # ('call_func', name, args)
        _, func_name, arg_nodes = node
        func_def = self.symbol_table.get(func_name)
        
        evaluated_args = [self._visit(arg) for arg in arg_nodes]

        self.symbol_table.enter_scope()
        return_value = None
        try:
            param_defs = func_def[2]
            for i, param_def in enumerate(param_defs):
                param_name = param_def[2]
                self.symbol_table.set(param_name, evaluated_args[i])

            if func_def[0] == 'function':
                self._visit(func_def[3]) # body
            else: # function_return
                self._visit(func_def[4]) # body
                return_value = self._visit(func_def[5]) # return_expr
        finally:
            self.symbol_table.exit_scope()
            
        return return_value

    def _visit_add(self, node):
        # ('add', list_expr, value_expr)
        _, list_expr, value_expr = node
        the_list = self._visit(list_expr)
        value = self._visit(value_expr)
        if not isinstance(the_list, list):
            raise TypeError("First argument to 'add' must be a list.")
        the_list.append(value)

    def _visit_remove_list_item(self, node):
        # ('remove_list_item', list_expr)
        _, list_expr = node
        the_list = self._visit(list_expr)
        if not isinstance(the_list, list):
            raise TypeError("Argument to 'remove' must be a list.")
        if len(the_list) > 0:
            the_list.pop() # Removes the last item

    def _visit_loop(self, node):
        # ('loop', var_name, range_node, body)
        _, var_name, range_node, body = node
        
        range_args = range_node[1:]
        start = self._visit(range_args[0])
        end = self._visit(range_args[1]) if len(range_args) > 1 else start
        if len(range_args) == 1: start = 0
        
        if start is None or end is None:
            raise ValueError("Start and end values for the loop range cannot be None.")
        for i in range(int(start), int(end)):
            self.symbol_table.enter_scope()
            self.symbol_table.set(var_name, i)
            self._visit(body)
            self.symbol_table.exit_scope()

    def _visit_conditional(self, node):
        # ('conditional', condition, if_block, else_block=None)
        if len(node) == 4:
            _, condition, if_block, else_block = node
        else:
            _, condition, if_block = node
            else_block = None

        if self._visit(condition):
            self._visit(if_block)
        elif else_block:
            self._visit(else_block)

    def _visit_read_list_item(self, node):
        # ('read_list_item', list_node, index_expr)
        _, list_node, index_expr = node
        the_list = self._visit(list_node)
        index = self._visit(index_expr)
        if the_list is None:
            raise TypeError("Cannot access an item from a NoneType object.")
        return the_list[index]

    def _visit_list_assign(self, node):
        # ('list_assign', list_node, index_expr, value_expr)
        _, list_node, index_expr, value_expr = node
        the_list = self._visit(list_node)
        index = self._visit(index_expr)
        value = self._visit(value_expr)
        if the_list is None:
            raise TypeError("Cannot assign to an index of a NoneType object.")
        the_list[index] = value

    def _visit_len_list_item(self, node):
        # ('len_list_item', list_node)
        list_val = self._visit(node[1])
        if list_val is None:
            raise TypeError("Cannot get the length of a NoneType object.")
        return len(list_val)