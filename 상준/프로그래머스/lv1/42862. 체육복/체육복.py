def solution(n, lost, reserve):
    
    lost.sort()
    reserve.sort()
    
    cnt = n-len(lost)
    
    for r in reserve[:]:
        if r in lost:
            cnt += 1
            lost.remove(r)
            reserve.remove(r)
            
    for r in reserve:
        if r-1 in lost:
            cnt += 1
            lost.remove(r-1)
            continue
        
        if r+1 in lost:
            cnt += 1
            lost.remove(r+1)
            continue        

    return cnt