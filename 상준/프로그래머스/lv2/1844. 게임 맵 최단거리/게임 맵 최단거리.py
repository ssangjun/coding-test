from collections import deque

def in_range(x, y, n, m):
    return x>=0 and x<n and y>=0 and y<m

def can_go(x, y, n, m, varr, marr):
    if not in_range(x, y, n, m):
        return False
    if varr[x][y]:
        return False
    if marr[x][y] == 0:
        return False
    return True

q = deque()

def move(x, y, step, varr, marr, sarr):
    q.append((x, y, step))
    varr[x][y] = True
    sarr[x][y] = step

def bfs(n, m, varr, marr, sarr):
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]
    
    move(0, 0, 1, varr, marr, sarr)
    
    while q:
        cx, cy, step = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = cx+dx, cy+dy
            
            if can_go(nx, ny, n, m, varr, marr):
                move(nx, ny, step+1, varr, marr, sarr)
    
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    steps = [[-1 for _ in range(m)] for _ in range(n)]
    
    bfs(n, m, visited, maps, steps)
        
    return steps[n-1][m-1]