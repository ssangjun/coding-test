from collections import deque

def solution(priorities, location):
    answer = 0
    n = len(priorities)
    
    pri_q = deque(priorities)
    idx_q = deque([i for i in range(n)])
    
    pri_s = []
    idx_s = []
    
    i = 0
    while len(idx_s) != n:
        p = pri_q.popleft()
        
        if not pri_q or p >= max(pri_q):
            pri_s.append(p)
            idx_s.append(i)
            pri_q.append(0)
        else:
            pri_q.append(p)
        
        i = (i+1)%n
        
    return idx_s.index(location)+1

