from itertools import permutations

def list_to_int(arr):
    string = ""
    for l in arr:
        string += l
    return int(string)

def calc(num1, num2, sign):
    if sign == "+":
        return num1+num2
    if sign == "-":
        return num1-num2
    if sign == "*":
        return num1*num2
    
def calc_with_operator(operands, operators, prior_opr):
    operators.reverse()
    operators.append("")
    operators.reverse()

    stack = []
    num_stack = []
    opr_stack = []
    
    for operand, operator in zip(operands, operators):
        if not num_stack:
            num_stack.append(operand)
            continue
            
        if operator == prior_opr:
            num_stack.append(calc(num_stack.pop(), operand, operator))
            continue
        else:
            num_stack.append(operand)
            opr_stack.append(operator)
    
    return num_stack, opr_stack
    
def seperator(expression):
    signs = ["+", "-", "*"]
    
    number = []
    num_stack = []
    opr_stack = []
    for e in expression:
        if e in signs:
            num_stack.append(list_to_int(number))
            opr_stack.append(e)
            number = []
        else:
            number.append(e)
    num_stack.append(list_to_int(number))
    
    return num_stack, opr_stack

def calc_with_priority(operands, operators, priority):
    tmp_operands = [operand for operand in operands]
    tmp_operators = [operator for operator in operators]

    for p in priority:
        tmp_operands, tmp_operators = calc_with_operator(tmp_operands, tmp_operators, p)
        
    return int(tmp_operands[0])
    
        

def solution(expression):
    operands, operators = seperator(expression)
    
    priorities = list(permutations(list(set(operators))))
    print(priorities)
    
    max_val = 0
    for priority in priorities:
        max_val = max(max_val, abs(calc_with_priority(operands, operators, priority)))
    
    return max_val