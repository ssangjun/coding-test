def seperator(name):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    head = []
    number = ""
    tail = []
    
    head_done = False 
    number_done = False
    
    for l in name:
        if not l in nums and not head_done:
            head.append(l.lower())
            continue
        
        head_done = True
        
        if l in nums and not number_done:
            if number or l != 0:
                number += l
            continue
        
        number_done = True
        
        tail.append(l)
        
    return (name, head, int(number), tail) 
        

def solution(files):
    stack = []
    
    for file in files:
        stack.append(seperator(file))
        # print(seperator(file))
        
    stack.sort(key = lambda x:(x[1], x[2]))
    
    answer = []
    
    for s in stack:
        answer.append(s[0])
        
    return answer