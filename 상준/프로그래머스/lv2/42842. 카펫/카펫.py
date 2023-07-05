def solution(brown, yellow):
    i, j = 0, 0
    for i in range(yellow+3):
        for j in range(i+1):
            
            if (i-2)*(j-2) == yellow and i*j == yellow+brown:
                return i, j
