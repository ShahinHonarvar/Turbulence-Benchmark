
def return_binary_or_hexa(numbers):
    # Find the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 13 and 35
    sum = 0
    for i in range(numbers[12] + 1, numbers[34]):
        if i not in numbers:
            sum += i
    
    # If the sum is an odd number, return its binary representation string
    if sum % 2 == 1:
        return bin(sum)[2:]
    # Otherwise, return its hexadecimal representation string
    else:
        return hex(sum)[2:].lower()
