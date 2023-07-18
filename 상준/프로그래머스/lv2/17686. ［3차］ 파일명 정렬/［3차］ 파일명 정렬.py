def seperator(file_name):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    head = ""
    head_done = False
    
    number = ""
    number_done = False
    
    tail = ""

    for i, l in enumerate(file_name):
        if not head_done and not l in nums:
            head += l.lower()
            continue
        
        head_done = True
        
        if not number_done and l in nums:
            number += l
            continue
        
        number_done = True
        
        tail += l
        
    return (file_name, head, int(number), tail)
            

def solution(files):
    arr = []
    
    for file in files:
        arr.append(seperator(file))
    
    arr.sort(key = lambda x:(x[1], x[2]))
    
    answer = [row[0] for row in arr]

    return answer