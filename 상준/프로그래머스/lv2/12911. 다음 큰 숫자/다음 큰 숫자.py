def decimal_to_binary(num):
    stack = []
    
    while True:
        if num < 1:
            break
        
        a = num%2
        
        stack.append(a)
        
        num //= 2
    
    stack.reverse()
    
    return stack

def solution(n):
    answer = 0
    cnt = decimal_to_binary(n).count(1)
    
    while True:
        n += 1
        
        if cnt == decimal_to_binary(n).count(1):
            break
            
    return n