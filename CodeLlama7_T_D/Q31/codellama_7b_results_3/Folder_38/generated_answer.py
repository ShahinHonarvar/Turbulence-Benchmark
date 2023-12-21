
def if_perfect_num(lst):
    # Check if the list has at least 39 elements
    if len(lst) < 39:
        return False

    # Calculate the sum of the factors of 39
    sum = 0
    for i in range(1, 39 + 1):
        if i % 39 == 0:
            sum += i

    # Return true if the 39th element is a perfect number, otherwise return false
    return lst[38] == sum
