def seperator(string, n):
    stack = []
    
    temp = ""
    for i, s in enumerate(string, start=1):
        temp += s
        if i%n==0:
            stack.append(temp)
            temp = ""
    if temp:
        stack.append(temp)
                 
    return stack
            
def count_duplication(arr):
    i = 0
    cnt = 1
    stack = []
    for i, elem in enumerate(arr):
        if not stack:
            stack.append(elem)
            continue
            
        if stack[-1] == elem:
            cnt += 1
        else:
            if cnt > 1:
                stack.append(str(cnt))
            stack.append(elem)
            cnt = 1
            
    if cnt > 1:
        stack.append(str(cnt))
    
    return_stack = ""
    for s in stack:
        return_stack += s
        
    return return_stack

def solution(string):
    
    size = ((len(string)+1)//2)+1
    min_val = float('inf')
    
    for i in range(1, size):
        arr = count_duplication(seperator(string, i))
        min_val = min(min_val, len(arr))
        
    return min_val