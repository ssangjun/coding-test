def index_to_word(arr):
    moeums = ["", "A", "E", "I", "O", "U"]
    
    word = ""
    for elem in arr:
        word += moeums[elem]
    
    return word
        
def solution(word):
    answer = 0

    stack = []
    while True:
        answer += 1
        
        if len(stack) < 5:
            stack.append(1)
        else:
            while True:
                elem = stack.pop()+1
                if elem > 5:
                    continue
                else:
                    stack.append(elem)
                    break
        
        if word == index_to_word(stack):
            break
        
    return answer