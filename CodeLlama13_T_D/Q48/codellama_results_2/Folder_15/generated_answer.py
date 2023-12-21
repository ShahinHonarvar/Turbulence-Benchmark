
def return_binary_or_hexa(mytuple):
    a, b = mytuple[0], mytuple[4]
    sum = 0
    for i in range(a+1,b):
        if i not in mytuple:
            sum += 1
    if sum % 2 == 0:
        return f"{sum:X}"
    else:
        return f"{sum:b}"
