from collections import deque

def in_range(x, y, n, m):
    return x>=0 and x<n and y>=0 and y<m

def can_go(x, y, n, m, varr, marr):
    if not in_range(x, y, n, m):
        return False
    if varr[x][y]:
        return False
    if marr[x][y] == "X":
        return False
    return True

q = deque()

def move(x, y, step, varr):
    varr[x][y] = True
    q.append((x, y, step))

def bfs(sx, sy, n, m, varr, marr):
    sum_val = 0
    dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
    
    move(sx, sy, marr[sx][sy], varr)
    
    while q:
        x, y, step = q.popleft()
        sum_val += int(step)
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy

            if can_go(nx, ny, n, m, varr, marr):
                move(nx, ny, marr[nx][ny], varr)
                                           
    return sum_val

def solution(maps):
    answer = []
    
    n, m = len(maps), len(maps[0])
    
    visited = [[False]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):          
            if can_go(i, j, n, m, visited, maps):
                answer.append(bfs(i, j, n, m, visited, maps))
    
    if answer==[]:
        answer = [-1]
    else:
        answer.sort()
        
    return answer