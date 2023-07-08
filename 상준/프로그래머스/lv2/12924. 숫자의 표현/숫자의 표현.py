def solution(n):
    
    arr = [i for i in range(1, n+1)]
    
    cnt = 1
    s, e = 0, 0
    sum_val = arr[0]
    
    while True:
        if s >= n-1 and e >= n-1:
            break
            
        if sum_val == n:
            print(s, e)
            cnt += 1
            e += 1
            sum_val += arr[e]
            continue
        
        if sum_val > n:
            sum_val -= arr[s]
            s += 1
            continue
        
        if sum_val < n:
            e += 1
            sum_val += arr[e]
            continue
            
    return cnt