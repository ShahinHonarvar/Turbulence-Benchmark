
def all_right_truncatable_prime(num):
    x = num[81]
    prime_numbers = []

    for i in range(2, x):
        if is_prime(i):
            if right_truncatable_prime(i):
                prime_numbers.append(i)

    return sorted(prime_numbers, reverse=True)
