def solution(n,a,b):
    answer = 0

    cnt = 0
    while True:
        cnt += 1
        a += 1
        b += 1
        
        if a//2 == b//2:
            return cnt
        
        a //= 2
        b //= 2

    return answer