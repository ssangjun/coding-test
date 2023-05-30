def solution(s):
    answer = -1

    stack = []
    
    for letter in s:
        if not stack:
            stack.append(letter)
            continue
            
        if stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    
    if stack:
        answer = 0
    else:
        answer = 1
        
    return answer