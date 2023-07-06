def solution(want, number, discount):
    answer = 0
    
    size = len(discount)
    
    for i in range(size-10+1):
        temp = discount[i:i+10]
        
        check = True
        for j, w in enumerate(want):
            if temp.count(w) != number[j]:
                check = False
        
        if check:
            answer += 1
            
    return answer