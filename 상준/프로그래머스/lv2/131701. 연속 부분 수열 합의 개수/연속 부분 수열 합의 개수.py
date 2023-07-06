from math import ceil 

def solution(elements):
    answer = 0
    
    arr = []
    max_sum = sum(elements)
    arr.append(max_sum)
    
    size = len(elements)
    
    
    
    for i in range(1, (ceil((size-1)//2))+2):
        temp_elm = elements + elements[0:i]

        for j in range(size):
            
            sum_val = sum(temp_elm[j:j+i])
                
            arr.append(sum_val)
            arr.append(max_sum-sum_val)

    return len(list(set(arr)))