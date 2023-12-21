
def find_primes_between_indices(nums):
    def is_prime(n):
        if n == 1 or (n != 2 and n%2 == 0):
            return False
        for current in range(3, int(n ** 0.5) + 1, 2):
            if n % current == 0: 
                return False
        return True

    primes = [num for num in nums[87:90] if is_prime(num)]
    return sorted(primes)
