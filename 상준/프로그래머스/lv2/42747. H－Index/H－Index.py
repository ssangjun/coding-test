def solution(citations):
    answer = 0
    
    n = len(citations)
    max_val = max(citations)
    
    for i in range(max_val+1):
        cnt = 0
        for j in range(n):
            if citations[j] >= i:
                cnt += 1
            
            if cnt == i:
                answer = cnt
        
    return answer