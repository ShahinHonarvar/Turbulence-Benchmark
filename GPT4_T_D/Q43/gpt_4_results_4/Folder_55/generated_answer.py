
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    result = []
    if len(int_list) >= 3:
        for i in range(2, min(3, len(int_list))):
            if is_prime(int_list[i]):
                result.append(int_list[i])
        return sorted(result)
    else:
        return []
