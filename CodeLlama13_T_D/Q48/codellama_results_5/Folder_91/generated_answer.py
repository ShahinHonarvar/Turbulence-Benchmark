
def return_binary_or_hexadecimal(mytuple):
    a = mytuple[0]
    b = mytuple[6]
    sum = 0
    for i in range(a+1,b-1):
        if i not in mytuple:
            sum += i
    if (sum % 2) == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
