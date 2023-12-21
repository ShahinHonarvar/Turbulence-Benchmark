
def return_binary_or_hexa(tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 13 and 70
    a = tuple[13]
    b = tuple[70]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple:
            sum += i
    # Check if the sum is an odd number
    if sum % 2 == 1:
        return f'{sum:b}'
    else:
        return f'{sum:x}'
