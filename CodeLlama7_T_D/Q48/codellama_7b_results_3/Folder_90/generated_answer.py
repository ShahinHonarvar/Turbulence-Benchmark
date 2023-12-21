
def return_binary_or_hexa(tuple):
    # Check if the tuple is empty
    if not tuple:
        return ""

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 60 and 90
    sum = 0
    for i in range(tuple[60], tuple[90]):
        if i + 1 not in tuple[60:90]:
            sum += i + 1

    # Check if the sum is an odd number
    if sum % 2 == 1:
        return bin(sum)[2:]

    else:
        return hex(sum)[2:]
