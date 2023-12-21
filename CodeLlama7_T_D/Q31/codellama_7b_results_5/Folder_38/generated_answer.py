
def if_perfect_num(my_list):
    # Check if the list is empty or if the index is out of range
    if len(my_list) == 0 or 38 >= len(my_list):
        return False

    # Calculate the sum of the factors of the number at index 38
    num = my_list[38]
    sum = 1

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i + num // i

    # Return true if the sum is equal to the number at index 38
    return sum == my_list[38]
