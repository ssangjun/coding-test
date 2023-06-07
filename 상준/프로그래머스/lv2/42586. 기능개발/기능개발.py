def work_once(progresses, speeds):
    for i in range(len(progresses)):
        progresses[i] += speeds[i]

def solution(progresses, speeds):
    answer = []
    
    while True:
        if not progresses:
            break
            
        work_once(progresses, speeds)
        
        cnt = 0
        
        for p in progresses:
            if p >= 100:
                cnt += 1
            else:
                break
            
        progresses = progresses[cnt:]
        speeds = speeds[cnt:]
        
        print(progresses)
        if cnt > 0:
            answer.append(cnt)
        
        
            
    return answer