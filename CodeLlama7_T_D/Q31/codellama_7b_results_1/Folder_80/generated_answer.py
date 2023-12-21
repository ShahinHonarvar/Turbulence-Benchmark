
def if_perfect_num(my_list):
    if len(my_list) < 746:
        return False

    perfect_number = my_list[746]

    # Calculate the sum of the factors of the perfect number using the Sieve of Eratosthenes

    factor_sum = 0

    for i in range(1, perfect_number // 2 + 1):
        if perfect_number % i == 0:
            factor_sum += i

    # Check if the sum of the factors is equal to the perfect number

    return factor_sum == perfect_number
