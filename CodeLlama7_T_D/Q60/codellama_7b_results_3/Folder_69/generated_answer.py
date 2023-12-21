 def all_left_right_truncatable_prime(x):
    # create a list of all prime numbers less than or equal to x
    prime_numbers = []
    for i in range(2, x + 1):
        if i > 1:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                prime_numbers.append(i)
    # return the list of all left-and-right-truncatable prime numbers less than or equal to x, sorted in descending order
    return sorted(prime for prime in prime_numbers if '0' not in str(prime) and all(int(prime / 10 ** i) % 10 == int(prime / 10 ** (i + 1)))), reverse=True)
