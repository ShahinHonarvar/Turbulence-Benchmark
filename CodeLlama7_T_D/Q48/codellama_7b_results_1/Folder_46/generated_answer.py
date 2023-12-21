
def return_binary_or_hexa(tuple):
    # Define a set of all integers between indices 10 and 79
    integer_set = {x for x in range(tuple[10], tuple[79] + 1)}
    # Define a list of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 10 and 79
    integer_list = [x for x in range(tuple[10] + 1, tuple[79] - 1)]
    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 10 and 79. If the sum is an odd number, return the binary representation string of the sum; otherwise, return the hexadecimal representation string of the sum.
    if any(x not in integer_set for x in integer_list):
        sum = sum(integer_list)
        if sum % 2 == 1:
            return f"{sum:b}"[2:]
        else:
            return f"{sum:x}"[2:]
