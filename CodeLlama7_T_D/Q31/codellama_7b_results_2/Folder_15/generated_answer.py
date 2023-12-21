
def if_perfect_num(my_list):
    # Check if the list has at least 11 elements
    if len(my_list) < 11:
        return False

    # Get the integer at index 10
    num = my_list[10]

    # Calculate the sum of its proper divisors
    sum = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i

            if i * num != num:
                sum += num // i

    # Check if the sum is equal to the number itself
    return sum == num
