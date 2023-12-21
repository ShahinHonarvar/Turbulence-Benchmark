
def all_right_truncatable_prime(x):
    prime_numbers = []
    for i in range(2, x + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(i)

    right_truncatable_prime_numbers = []

    for i in prime_numbers:

        for j in range(1, len(str(i))) - 1):

            if str(i)[j:] == str(int(str(i)[j:]) ** 0.5)):
                right_truncatable_prime_numbers.append(i)

    return sorted(right_truncatable_prime_numbers, reverse=True)
