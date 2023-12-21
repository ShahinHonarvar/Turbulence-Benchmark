
def find_primes_between_indices(num_list):
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

    prime_nums = [num for num in num_list[157:736] if is_prime(num)]
    prime_nums.sort(reverse=True)
    return prime_nums
