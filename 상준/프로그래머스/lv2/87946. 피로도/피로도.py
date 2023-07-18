from itertools import permutations

def count_clear(k, dungeons):
    for i, dungeon in enumerate(dungeons, start = 1):
        if dungeon[0] > k:
            i -= 1
            break
        k -= dungeon[1]
    return i
        
def solution(k, dungeons):
    answer = -1
    
    max_val = 0
    
    for simul in list(permutations(dungeons, len(dungeons))):
        temp = count_clear(k, simul)
        max_val = max(max_val, temp)
    
    return max_val