def bin_to_nJinsu(n, num):
    stack = []
    while True:
        a = num % n
        b = num // n
        if num < n:
            stack.append(change_alpha_over10(num))
            break
            
        stack.append(change_alpha_over10(a))
        num = b
        
    stack.reverse()
    
    string = ""
    
    for s in stack:
        string += s
        
    return string

def change_alpha_over10(n):
    mapper = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    
    if n >= 10:
        return mapper[n]
    else:
        return str(n)
    
def solution(n, t, m, p):
    string = ""
    answer = ""
    
    for i in range(t*m):
        string += bin_to_nJinsu(n, i)

    for j, s in enumerate(string, start=1):
        if (j % m == p) or (m == p and j % m == 0):
            answer += s
            if len(answer) == t:
                break
        
    return answer