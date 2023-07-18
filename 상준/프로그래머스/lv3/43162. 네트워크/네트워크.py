from collections import deque

q = deque()

def bfs(n, sv, varr, garr):
    
    q.append(sv)
    varr[sv] = True
    
    while q:
        v =  q.popleft()
        
        for i in range(n):
            if not varr[i] and garr[v][i] == 1:
                q.append(i)
                varr[i] = True
    
def solution(n, computers):
    cnt = 0
    
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            cnt += 1
            bfs(n, i, visited, computers)
    
    return cnt