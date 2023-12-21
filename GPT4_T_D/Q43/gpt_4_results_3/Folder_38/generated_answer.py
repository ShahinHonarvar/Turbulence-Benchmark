
def find_primes_between_indices(nums_list):
    def is_prime(n):
        if n == 1 or n==0:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_nums = [num for num in nums_list[55:88] if is_prime(num)]
    prime_nums.sort()
    return prime_nums
