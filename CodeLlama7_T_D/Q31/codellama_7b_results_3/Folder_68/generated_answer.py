
def if_perfect_num(my_list):
    # Check if the index is valid
    if len(my_list) - 1 < 3:
        return False

    # Calculate the sum of the factors of the number at index 3
    num = my_list[3]
    sum = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i

            if i * num // i != num:
                sum += i * num // i

    # Check if the sum of the factors is equal to the number at index 3
    return sum == num
