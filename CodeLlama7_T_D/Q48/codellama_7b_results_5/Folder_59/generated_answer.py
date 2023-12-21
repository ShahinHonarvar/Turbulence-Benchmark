 def return_binary_or_hexa(tuple):
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 0 and 10
    sum = 0
    for i in range(tuple[0] + 1, tuple[10] - 1):
        if i not in tuple:
            sum += i
    # If the sum is an odd number, return the binary representation string of the sum; otherwise, return the hexadecimal representation string of the sum
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
