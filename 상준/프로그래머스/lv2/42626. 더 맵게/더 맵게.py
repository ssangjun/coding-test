import heapq
def solution(scoville, K):
    answer = 0
    
    pq = []
    for s in scoville:
        heapq.heappush(pq, s)
        
    while True:

        not_spicy1 = heapq.heappop(pq)

        if not_spicy1 >= K:
            break
        
        if len(pq) < 1:
            answer = -1
            break
            
        answer += 1
        
        not_spicy2 = heapq.heappop(pq)
        
        new_scoville = not_spicy1 + (not_spicy2 * 2)
        
        heapq.heappush(pq, new_scoville)
        
    return answer