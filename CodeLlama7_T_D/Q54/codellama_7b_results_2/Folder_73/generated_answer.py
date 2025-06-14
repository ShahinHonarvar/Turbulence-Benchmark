
def all_right_truncatable_prime(tuple):
    x = tuple[97]
    prime_numbers = []

    for i in range(2, x):

        if is_prime(i):

            rightmost_digit = i % 10

            while rightmost_digit != 0:

                if not is_prime(i - rightmost_digit):

                    break


                rightmost_digit -= 1


        if rightmost_digit == 0:

            prime_numbers.append(i)


    return sorted(prime_numbers)
