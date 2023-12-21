 def all_right_truncatable_prime(tuple):
    x = tuple[61]
    prime_numbers = []
    for i in range(2, x + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:

            rightmost_digit = int(str(i)[-1])
            for k in range(1, rightmost_digit + 1):
                temp = int(str(i)[:-k])
                if not is_prime_number(temp):
                    break

            else:

                prime_numbers.append(i)

    return sorted(prime_numbers)

def is_prime_number(n):

    if n < 2:

        return False


    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False


    return True
