from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    
    size = len(truck_weights)
    bridge_weight = 0
    
    waited_trucks = truck_weights
    bridge_trucks = [0]*bridge_length
    passed_trucks = []
    
    while True:
        if len(passed_trucks) == size:
            break
        
        time += 1
        
        if bridge_trucks[0] != 0:
            bridge_weight -= bridge_trucks[0]
            passed_trucks.append(bridge_trucks[0])
        
        bridge_trucks = bridge_trucks[1:]
        
        if len(waited_trucks) > 0 and bridge_weight + waited_trucks[0] <= weight:
            bridge_trucks.append(waited_trucks[0])
            bridge_weight += waited_trucks[0]
            waited_trucks = waited_trucks[1:]
        else:
            bridge_trucks.append(0)
        
        
        
    return time