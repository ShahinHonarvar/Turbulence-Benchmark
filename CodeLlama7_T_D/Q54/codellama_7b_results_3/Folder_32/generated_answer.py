 def all_right_truncatable_prime(tuple):
    x = tuple[42]
    prime_numbers = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:

            for k in range(len(str(i)))):
                temp = str(i)[k:]

                try:
                    int(temp)

                except ValueError:
                    is_right_truncatable_prime = True
                    break

                else:
                    is_right_truncatable_prime = False
                    break

            if is_right_truncatable_prime:

                prime_numbers.append(i)

    return sorted(prime_numbers)
