from math import ceil 

def solution(n, words):
    answer = []

    turn_cnt, round_cnt = 0, 0
    
    stack = []
    for i, word in enumerate(words, start=1):
        if not stack:
            stack.append(word)
            continue
        
        if word in stack or stack[-1][-1] != word[0]:
            turn_cnt = i%n
            if turn_cnt == 0:
                turn_cnt = n
            round_cnt = ceil(i/n)
            break
        else:
            stack.append(word)
    
    answer = [turn_cnt, round_cnt]
    
    return answer