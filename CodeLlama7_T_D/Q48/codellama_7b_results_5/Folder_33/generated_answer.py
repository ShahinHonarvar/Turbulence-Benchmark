
def return_binary_or_hexa(tuple):
    # Initialize variables for sum and number of odd sums
    sum = 0
    num_odd_sums = 0
    # Iterate over the tuple
    for i in range(13, 35 + 1):
        # Add the current element to the sum
        sum += tuple[i]
        # Check if the sum is an odd number
        if sum % 2 != 0:
            # Increment the number of odd sums
            num_odd_sums += 1
    # If there are no odd sums, return an empty string
    if num_odd_sums == 0:
        return ""
    # Otherwise, return the binary or hexadecimal representation of the sum
    elif num_odd_sums == 1:
        return bin(sum)[2:]

    else:

        return hex(sum)[2:]
