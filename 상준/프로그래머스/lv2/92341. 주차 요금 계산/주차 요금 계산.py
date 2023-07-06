from math import ceil

def calc_time(time1, time2):
    min1 = int(time1.split(":")[0])*60 + int(time1.split(":")[1])
    min2 = int(time2.split(":")[0])*60 + int(time2.split(":")[1])
                                             
    return abs(min2-min1)  
                                             
def solution(infos, records):
    basic_time, basic_fee, unit_time, unit_fee = infos[0], infos[1], infos[2], infos[3]
    parked = {}
    total_time = {}
    
    for record in records:
        time, num, type = tuple(record.split())

        if type == "IN":
            parked[num] = time
        else:
            t = calc_time(parked[num], time)
            
            if num in total_time:
                total_time[num] += t
            else:
                total_time[num] = t
                
            parked.pop(num)
    
    
    while parked:
        num, time = parked.popitem()
        
        t = calc_time(time, "23:59")
        
        if num in total_time:
                total_time[num] += t
        else:
            total_time[num] = t
    
    temp = sorted(total_time.items())
    
    answer = []
    while temp:
        num, time = temp.pop()
        fee = basic_fee+ceil((time-basic_time)/unit_time) * unit_fee
        answer.append(max(fee, basic_fee))
    answer.reverse()
    
    return answer