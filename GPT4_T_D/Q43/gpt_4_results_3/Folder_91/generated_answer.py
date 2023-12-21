
def find_primes_between_indices(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    indices = arr[:2]
    indices.sort()
    nums = arr[indices[0]:indices[1]+1]
    primes = [num for num in nums if is_prime(num)]
    primes.sort()
    return primes
