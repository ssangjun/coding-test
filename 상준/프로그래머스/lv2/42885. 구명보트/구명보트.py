def solution(people, limit):
    answer = 0
    
    people.sort()
    s, e = 0, len(people)-1
    
    while True:
        if s==e:
            answer += 1
            break
        if s>e:
            break
                
        if people[s]+people[e] > limit:
            answer += 1
            e -= 1
        else:
            answer += 1
            s += 1
            e -= 1
        
    return answer