def move(s):
    s = list(s)
    arr = s[1:]
    arr.append(s[0])
    return arr

def check(s):
    stack = []
    for elem in s:
        if not stack:
            stack.append(elem)
            continue
            
        if stack[-1]=="[" and elem=="]":
            stack.pop()
        elif stack[-1]=="{" and elem=="}":
            stack.pop()
        elif stack[-1]=="(" and elem==")":
            stack.pop()
        else:
            stack.append(elem)
            
    if stack:
        return False
    else: 
        return True
        
def solution(s):    
    cnt = 0
    size = len(s)
    
    for _ in range(size):
        s = move(s)

        if check(s):
            cnt += 1
    
    return cnt