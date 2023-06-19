from collections import Counter

def solution(k, tangerine):
    tang_cnt = Counter(tangerine)
    
    tang_cnt_values = list(tang_cnt.values())
    tang_cnt_values.sort(reverse=True)
    
    cnt_val = 0
    sum_val = 0
    for cnt in tang_cnt_values:
        if sum_val < k:
            sum_val += cnt
            cnt_val +=1
        else:
            break
            
    return cnt_val