"""
Este módulo define las clases para representar el Árbol de Sintaxis Abstracta (AST).
Cada clase corresponde a un tipo de construcción en el lenguaje (una variable, una operación, etc.).
El método `execute` en cada nodo es responsable de la interpretación de ese nodo.
"""


# https://ericknavarro.github.io/2020/03/15/26-Interprete-sencillo-utilizando-PLY/
class Node:
    """Clase base para todos los nodos del AST."""

    def execute(self, symbol_table):
        raise NotImplementedError(
            f"Método execute no implementado para {self.__class__.__name__}"
        )

    def __repr__(self):
        return f"<{self.__class__.__name__}>"


class RootNode(Node):
    def __init__(self, statement_list):
        self.statement_list = statement_list

    def execute(self, symbol_table):
        for statement in self.statement_list:
            statement.execute(symbol_table)

    def __repr__(self):
        return f"RootNode({self.statement_list!r})"


class VarNode(Node):
    def __init__(self, var_type, name, value_expr):
        self.var_type = var_type
        self.name = name
        self.value_expr = value_expr

    def execute(self, symbol_table):
        value = self.value_expr.execute(symbol_table)
        symbol_table.agregar(self.name, value)

    def __repr__(self):
        return f"VarNode(type={self.var_type!r}, name={self.name!r}, value={self.value_expr!r})"


class AssignNode(Node):
    def __init__(self, name, value_expr):
        self.name = name
        self.value_expr = value_expr

    def execute(self, symbol_table):
        value = self.value_expr.execute(symbol_table)
        symbol_table.actualizar(self.name, value)

    def __repr__(self):
        return f"AssignNode(name={self.name!r}, value={self.value_expr!r})"


class BinaryOpNode(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def execute(self, symbol_table):
        left_val = self.left.execute(symbol_table)
        right_val = self.right.execute(symbol_table)

        if self.op == "+":
            if isinstance(left_val, str) or isinstance(right_val, str):
                return str(left_val) + str(right_val)
            return left_val + right_val
        elif self.op == "-":
            return left_val - right_val
        elif self.op == "*":
            return left_val * right_val
        elif self.op == "/":
            return left_val / right_val
        elif self.op == ">":
            return left_val > right_val
        elif self.op == "<":
            return left_val < right_val
        elif self.op == ">=":
            return left_val >= right_val
        elif self.op == "<=":
            return left_val <= right_val
        elif self.op == "==":
            return left_val == right_val
        elif self.op == "!=":
            return left_val != right_val
        elif self.op == "&":
            return left_val and right_val
        elif self.op == "|":
            return left_val or right_val
        raise TypeError(f"Operador binario no soportado: {self.op}")

    def __repr__(self):
        return f"BinaryOpNode({self.left!r} {self.op} {self.right!r})"


class UnaryOpNode(Node):
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

    def execute(self, symbol_table):
        value = self.expr.execute(symbol_table)
        if self.op == "!":
            return not value
        raise TypeError(f"Operador unario no soportado: {self.op}")

    def __repr__(self):
        return f"UnaryOpNode(op={self.op!r}, expr={self.expr!r})"


class PrimitiveNode(Node):
    def __init__(self, value):
        self.value = value

    def execute(self, symbol_table):
        return self.value

    def __repr__(self):
        return f"PrimitiveNode({self.value!r})"


class IdNode(Node):
    def __init__(self, name):
        self.name = name

    def execute(self, symbol_table):
        return symbol_table.obtener(self.name)

    def __repr__(self):
        return f"IdNode({self.name!r})"


class ListNode(Node):
    def __init__(self, items):
        self.items = items

    def execute(self, symbol_table):
        return [item.execute(symbol_table) for item in self.items]

    def __repr__(self):
        return f"ListNode({self.items!r})"


class ConsoleNode(Node):
    def __init__(self, args):
        self.args = args

    def execute(self, symbol_table):
        evaluated_args = [arg.execute(symbol_table) for arg in self.args]
        print(*evaluated_args)

    def __repr__(self):
        return f"ConsoleNode({self.args!r})"


class FunctionNode(Node):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

    def execute(self, symbol_table):
        symbol_table.agregar(self.name, self)

    def execute_body(self, args, symbol_table):
        symbol_table.enter_scope()
        try:
            for i, param_def in enumerate(self.params):
                param_name = param_def.name
                symbol_table.agregar(param_name, args[i])
            for statement in self.body:
                statement.execute(symbol_table)
        finally:
            symbol_table.exit_scope()

    def __repr__(self):
        return f"FunctionNode(name={self.name!r}, params={self.params!r}, body={self.body!r})"


class FunctionReturnNode(FunctionNode):
    def __init__(self, name, params, return_type, body, return_expr):
        super().__init__(name, params, body)
        self.return_type = return_type
        self.return_expr = return_expr

    def execute_body(self, args, symbol_table):
        symbol_table.enter_scope()
        return_value = None
        try:
            for i, param_def in enumerate(self.params):
                param_name = param_def.name
                symbol_table.agregar(param_name, args[i])

            for statement in self.body:
                statement.execute(symbol_table)

            return_value = self.return_expr.execute(symbol_table)
        finally:
            symbol_table.exit_scope()
        return return_value

    def __repr__(self):
        return f"FunctionReturnNode(name={self.name!r}, params={self.params!r}, return_type={self.return_type!r}, body={self.body!r}, return_expr={self.return_expr!r})"


class ParamNode(Node):
    def __init__(self, param_type, name, default_value=None):
        self.param_type = param_type
        self.name = name
        self.default_value = default_value

    def execute(self, symbol_table):
        # Los parámetros no se ejecutan directamente, son utilizados por los nodos de función
        pass

    def __repr__(self):
        return f"ParamNode(type={self.param_type!r}, name={self.name!r}, default={self.default_value!r})"


class CallFuncNode(Node):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def execute(self, symbol_table):
        func_def = symbol_table.obtener(self.name)
        evaluated_args = [arg.execute(symbol_table) for arg in self.args]
        return func_def.execute_body(evaluated_args, symbol_table)

    def __repr__(self):
        return f"CallFuncNode(name={self.name!r}, args={self.args!r})"


class ConditionalNode(Node):
    def __init__(self, condition, if_block, else_block=None):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block

    def execute(self, symbol_table):
        if self.condition.execute(symbol_table):
            self.if_block.execute(symbol_table)
        elif self.else_block:
            self.else_block.execute(symbol_table)

    def __repr__(self):
        return f"ConditionalNode(condition={self.condition!r}, if_block={self.if_block!r}, else_block={self.else_block!r})"


class LoopNode(Node):
    def __init__(self, var_name, range_node, body):
        self.var_name = var_name
        self.range_node = range_node
        self.body = body

    def execute(self, symbol_table):
        start, end, step = self.range_node.execute(symbol_table)
        for i in range(int(start), int(end), int(step)):
            symbol_table.enter_scope()
            symbol_table.agregar(self.var_name, i)
            self.body.execute(symbol_table)
            symbol_table.exit_scope()

    def __repr__(self):
        return f"LoopNode(var={self.var_name!r}, range={self.range_node!r}, body={self.body!r})"


class RangeNode(Node):
    def __init__(self, start, end=None, step=None):
        self.start = start
        self.end = end
        self.step = step

    def execute(self, symbol_table):
        start_val = self.start.execute(symbol_table)
        step_val = self.step.execute(symbol_table) if self.step else 1
        if self.end is None:
            return 0, start_val, step_val
        end_val = self.end.execute(symbol_table)
        return start_val, end_val, step_val

    def __repr__(self):
        return f"RangeNode(start={self.start!r}, end={self.end!r}, step={self.step!r})"


class ReadListItemNode(Node):
    def __init__(self, list_node, index_expr):
        self.list_node = list_node
        self.index_expr = index_expr

    def execute(self, symbol_table):
        the_list = self.list_node.execute(symbol_table)
        index = self.index_expr.execute(symbol_table)
        return the_list[index]

    def __repr__(self):
        return f"ReadListItemNode(list={self.list_node!r}, index={self.index_expr!r})"


class ListAssignNode(Node):
    def __init__(self, list_node, index_expr, value_expr):
        self.list_node = list_node
        self.index_expr = index_expr
        self.value_expr = value_expr

    def execute(self, symbol_table):
        the_list = self.list_node.execute(symbol_table)
        index = self.index_expr.execute(symbol_table)
        value = self.value_expr.execute(symbol_table)
        the_list[index] = value

    def __repr__(self):
        return f"ListAssignNode(list={self.list_node!r}, index={self.index_expr!r}, value={self.value_expr!r})"


class AddListItemNode(Node):
    def __init__(self, list_expr, value_expr):
        self.list_expr = list_expr
        self.value_expr = value_expr

    def execute(self, symbol_table):
        the_list = self.list_expr.execute(symbol_table)
        value = self.value_expr.execute(symbol_table)
        the_list.append(value)

    def __repr__(self):
        return f"AddListItemNode(list={self.list_expr!r}, value={self.value_expr!r})"


class RemoveListItemNode(Node):
    def __init__(self, list_expr):
        self.list_expr = list_expr

    def execute(self, symbol_table):
        the_list = self.list_expr.execute(symbol_table)
        if len(the_list) > 0:
            the_list.pop()

    def __repr__(self):
        return f"RemoveListItemNode(list={self.list_expr!r})"


class LenListItemNode(Node):
    def __init__(self, list_node):
        self.list_node = list_node

    def execute(self, symbol_table):
        list_val = self.list_node.execute(symbol_table)
        return len(list_val)

    def __repr__(self):
        return f"LenListItemNode({self.list_node!r})"


class HasListItemNode(Node):
    def __init__(self, list_expr, value_expr):
        self.list_expr = list_expr
        self.value_expr = value_expr

    def execute(self, symbol_table):
        the_list = self.list_expr.execute(symbol_table)
        value = self.value_expr.execute(symbol_table)
        return value in the_list

    def __repr__(self):
        return f"HasListItemNode(list={self.list_expr!r}, value={self.value_expr!r})"
