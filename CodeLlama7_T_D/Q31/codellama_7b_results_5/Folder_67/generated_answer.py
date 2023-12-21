
def if_perfect_num(my_list):
    # Check if the list is empty or has fewer than 43 elements
    if len(my_list) < 43:
        return False

    # Calculate the sum of the proper divisors of the number at index 43
    num = my_list[43]
    sum_of_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i

    # Check if the sum of the proper divisors is equal to the number at index 43
    return sum_of_divisors == num
