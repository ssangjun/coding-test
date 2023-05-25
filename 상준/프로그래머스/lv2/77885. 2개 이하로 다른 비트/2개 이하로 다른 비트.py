def decimal_to_bin(num):
    stack = []
    while True:
        if num==1:
            stack.append(num)
            break
        if num==0:
            break
            
        stack.append(num%2)
        num //= 2
    stack.append(0)
    return stack

def bin_to_decimal(binary):
    ret = 0
    for i, bit in enumerate(binary):
        ret += bit*(2**i)
    return ret

def solution(numbers):
    ans_arr = []
    
    for elem in numbers:        
        bin1 = decimal_to_bin(elem)
        
        for i, bit in enumerate(bin1):
            if bit==0:
                bin1[i]=1
                
                if i != 0:
                    bin1[i-1] = 0
                
                break
        
        
        ans_arr.append(bin_to_decimal(bin1))
        
    return ans_arr