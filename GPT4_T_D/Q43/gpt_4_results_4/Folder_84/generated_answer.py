
def find_primes_between_indices(num_list):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while (i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0):
                return False
            i = i + 6
        return True

    primes_list = []
    for num in num_list[830:850]:
        if is_prime(num):
            primes_list.append(num)
    primes_list.sort()
    return primes_list
