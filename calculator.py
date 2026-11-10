"""A simple command-line calculator.

Type math expressions like:  2 + 3 * 4,  (10 - 2) ** 2,  sqrt(16),  sin(pi / 2)
Type 'ans' to reuse the last result, 'help' for help, 'quit' to exit.
"""

import ast
import math
import operator

# Allowed operators
BINARY_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
UNARY_OPS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

# Allowed functions and constants
FUNCTIONS = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "log10": math.log10,
    "abs": abs,
    "round": round,
    "factorial": math.factorial,
}
CONSTANTS = {"pi": math.pi, "e": math.e}


def evaluate(node, variables):
    """Recursively evaluate a parsed expression safely (no eval())."""
    if isinstance(node, ast.Expression):
        return evaluate(node.body, variables)

    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in BINARY_OPS:
        left = evaluate(node.left, variables)
        right = evaluate(node.right, variables)
        return BINARY_OPS[type(node.op)](left, right)

    if isinstance(node, ast.UnaryOp) and type(node.op) in UNARY_OPS:
        return UNARY_OPS[type(node.op)](evaluate(node.operand, variables))

    if isinstance(node, ast.Name):
        if node.id in variables:
            return variables[node.id]
        raise ValueError(f"Unknown name: {node.id}")

    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
        func = FUNCTIONS.get(node.func.id)
        if func is None:
            raise ValueError(f"Unknown function: {node.func.id}")
        args = [evaluate(arg, variables) for arg in node.args]
        return func(*args)

    raise ValueError("Unsupported expression")


def calculate(expression, variables=None):
    variables = {**CONSTANTS, **(variables or {})}
    tree = ast.parse(expression, mode="eval")
    return evaluate(tree, variables)


def format_result(value):
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    if isinstance(value, float):
        return f"{value:.10g}"
    return str(value)


def main():
    print("Python Calculator  (type 'help' for help, 'quit' to exit)")
    last = 0

    while True:
        try:
            text = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not text:
            continue
        if text.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break
        if text.lower() == "help":
            print(__doc__)
            print("Functions:", ", ".join(FUNCTIONS))
            print("Constants:", ", ".join(CONSTANTS))
            continue

        try:
            last = calculate(text, {"ans": last})
            print("=", format_result(last))
        except ZeroDivisionError:
            print("Error: division by zero")
        except (ValueError, SyntaxError, TypeError, OverflowError) as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    main()
