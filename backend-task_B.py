var_number = int(input())

postfixExpressionList = input("postfix expression: ").split(' ')

tests_number = int(input())
var_values = []
for i in range(tests_number):
    var_values.append(input("{} var_values: ".format(i)).split(' '))

print(postfixExpressionList)


#IMPORTANT: this task doesn't solved to the end due to runtime error during some tests
def fromPostfixEval(postfix_array, values):
    vars_index = 0
    operands_stack = []
    for item in postfix_array:
        if item.isdigit() or item.isalpha() or (item[0] == '-' and item[1].isdigit()):
            try:
                operands_stack.append(int(item))
                print(operands_stack)
            except ValueError:
                item = values[vars_index]
                operands_stack.append(int(item))
                vars_index += 1
                print(operands_stack)
        else:
            operand1 = operands_stack.pop()
            operand2 = operands_stack.pop()

            result = doMath(operands_stack, item, operand1, operand2)
            operands_stack.append(result)
            print(operands_stack)
    return operands_stack.pop()


def doMath(operands_stack, op, op1, op2):
    if op == "*":
        return op2 * op1
    elif op == "/":
        return op2 / op1 if op1 != 0 else -1
    elif op == "+":
        return op2 + op1
    elif op == "-":
        return op2 - op1
    elif op == ">":
        return op2 > op1
    elif op == "<":
        return op2 < op1
    elif op == "<=":
        return op2 <= op1
    elif op == ">=":
        return op2 >= op1
    elif op == "==":
        return op2 == op1
    elif op == "!=":
        return op2 != op1
    elif op == "?":
        return op2 if operands_stack.pop() else op1


for i in range(tests_number):
    print(fromPostfixEval(postfixExpressionList, var_values[i]))

