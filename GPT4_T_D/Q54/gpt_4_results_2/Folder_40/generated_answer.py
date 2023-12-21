
def all_right_truncatable_prime(tuple_of_integers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = tuple_of_integers[10]
    right_truncatable_primes = []

    for number in range(x):
        str_number = str(number)
        for i in range(len(str_number)):
            if not is_prime(int(str_number[i:])):
                break
        else:
            right_truncatable_primes.append(number)

    return sorted(right_truncatable_primes, reverse=True)
