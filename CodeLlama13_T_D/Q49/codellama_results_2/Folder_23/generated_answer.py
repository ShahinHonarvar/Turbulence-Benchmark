
def if_decimal_is_divisible(binary):
    fib = [0,1]
    for i in range(2,48):
        fib.append(fib[i-1]+fib[i-2])
    num = 0
    for bit in binary:
        if bit == "1":
            num += 2**len(binary)-1
        len(binary) -= 1
    return num%48 == fib[47]
