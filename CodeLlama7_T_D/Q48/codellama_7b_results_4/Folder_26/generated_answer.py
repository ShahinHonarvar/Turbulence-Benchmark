
def return_binary_or_hexa(tuple_):
    # Get the indices of the range of interest
    start = tuple_.index(tuple_[68]) + 1
    end = tuple_.index(tuple_[99])
    # Calculate the sum of all integers in the range that are not present in the tuple
    sum = 0
    for i in range(start, end + 1):
        if tuple_[i] not in tuple_[68:99]:
            sum += tuple_[i]
    # Return the binary or hexadecimal representation of the sum
    if sum % 2 == 0:
        return f"{sum:x}"
    else:
        return f"{sum:b}"
