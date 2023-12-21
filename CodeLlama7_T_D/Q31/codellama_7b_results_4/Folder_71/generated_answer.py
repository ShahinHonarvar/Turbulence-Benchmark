
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 79 elements
    if len(my_list) < 79:
        return False

    # Get the integer at index 78
    num = my_list[78]

    # Check if the number is positive and odd

    if num > 0 and num % 2 != 0:

        # Calculate the sum of the divisors of the number

        sum_divisors = 0

        for i in range(1, int(num ** 0.5) + 1):

            if num % i == 0:

                sum_divisors += i + num // i


        # Check if the sum of the divisors is equal to the number itself

        if sum_divisors == num:

            return True


    return False
