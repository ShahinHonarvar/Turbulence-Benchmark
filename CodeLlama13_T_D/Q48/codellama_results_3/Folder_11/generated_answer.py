
def return_binary_or_hexa(numbers):
    # Find the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 48 and 76.
    sum = 0
    for i in range(numbers[48] + 1, numbers[76]):
        if i not in numbers:
            sum += i
    
    # If the sum is an odd number, return its binary representation string. Otherwise, return its hexadecimal representation string.
    if sum % 2 == 0:
        return "{:x}".format(sum)
    else:
        return bin(sum)[2:]
