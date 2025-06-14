
def if_perfect_num(my_list):
    # Check if the index is out of range
    if len(my_list) - 1 < 6:
        return False

    # Calculate the sum of the proper divisors of the number at index 6
    num = my_list[6]
    sum = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i

            if i * num // i != num:
                sum += num // i

    # Return True if the number at index 6 is a perfect number, otherwise return False
    if sum == 2 * num:
        return True

    else:
        return False
