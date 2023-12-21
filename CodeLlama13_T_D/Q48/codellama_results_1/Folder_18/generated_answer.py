
def return_binary_or_hexa(mytuple):
    sum = 0
    for i in range(56,90):
        if mytuple[i] not in mytuple:
            sum += mytuple[i]
    if sum % 2 == 1:
        return "{:b}".format(sum)
    else:
        return "{:x}".format(sum).lower()
