
def if_perfect_num(my_list):
    if my_list[68] == 0:
        return False

    # calculate the sum of the proper divisors
    sum = 1

    for i in range(2, int(my_list[68]) ** 0.5 + 1):
        if my_list[68] % i == 0:
            sum += i + my_list[68] / i

    # check if the sum is equal to the number itself
    return sum == my_list[68]
