
def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[33]
    b = tuple_of_integers[78]
    total_sum = 0

    for num in range(a+1, b):
        if num not in tuple_of_integers[33:79]:
            total_sum += num

    if total_sum == 0:
        return ""

    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
