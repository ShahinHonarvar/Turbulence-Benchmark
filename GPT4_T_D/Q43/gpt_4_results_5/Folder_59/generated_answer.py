
def find_primes_between_indices(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_nums = [num for num in lst[5:9] if is_prime(num)]
    prime_nums.sort(reverse=True)
    return prime_nums
