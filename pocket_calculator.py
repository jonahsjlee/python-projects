current_val = 0
recent_op = ""
recent_arg = 0
series_of_ops = "0"

def parenthesis(expr):
    return "(" + expr + ")"

def get_value():
    global current_val
    return current_val

def clear(x=0):
    global recent_op
    global recent_arg
    global current_val
    global series_of_ops
    recent_op = ""
    recent_arg = 0
    current_val = x
    series_of_ops = str(x)
    return current_val

def step(operator="", argument=""):
    global series_of_ops
    global recent_op
    recent_op = operator
    global recent_arg
    recent_arg = argument
    global current_val

    if operator == "+":
        series_of_ops = parenthesis(series_of_ops) + operator + str(argument)
        current_val += argument
    elif operator == "-":
        series_of_ops = parenthesis(series_of_ops) + operator + str(argument)
        current_val -= argument
    elif operator == "//":
        series_of_ops = parenthesis(series_of_ops) + operator + str(argument)
        current_val //= argument
    elif operator == "*":
        series_of_ops = parenthesis(series_of_ops) + operator + str(argument)
        current_val *= argument
    return current_val

def repeat():
    return step(recent_op, recent_arg)

def get_expr():
    return series_of_ops