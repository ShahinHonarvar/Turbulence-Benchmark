
def return_binary_or_hexa(tuple):
    # Define variables for the range of values and the sum
    start = tuple[45] + 1
    end = tuple[48] - 1
    sum = 0

    # Iterate over the range of values and calculate the sum
    for i in range(start, end + 1):
        if i not in tuple[45:48]:
            sum += i

    # Check if the sum is an odd number or not
    if sum % 2 == 0:
        return "{}".format(hex(sum))

    else:
        return "{}".format(bin(sum))
