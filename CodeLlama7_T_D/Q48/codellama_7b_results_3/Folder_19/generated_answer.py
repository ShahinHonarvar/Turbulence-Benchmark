 def return_binary_or_hexa(my_tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 1 and 4
    sum = 0
    for i in range(my_tuple[1] + 1, my_tuple[4]):
        if i not in my_tuple:
            sum += i
    # Check if the sum is an odd number
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
