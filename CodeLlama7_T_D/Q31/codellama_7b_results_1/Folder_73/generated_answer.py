
def if_perfect_num(my_list):
    # Check if the list has at least 42 elements
    if len(my_list) < 42:
        return False

    # Calculate the sum of the proper divisors of the number at index 41
    num = my_list[41]
    sum = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i + num // i

    # Check if the sum is equal to the number at index 41
    return sum == num
