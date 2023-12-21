
def if_perfect_num(my_list):
    # Check if the list has at least 460 elements
    if len(my_list) < 460:
        return False

    # Calculate the sum of the proper divisors of the number at index 459
    num = my_list[459]
    sum = 1

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i

            if num / i != i:
                sum += num / i

    # Check if the sum of the proper divisors is equal to the number at index 459
    if sum == my_list[459]:
        return True

    else:

        return False
