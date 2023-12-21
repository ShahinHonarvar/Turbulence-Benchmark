
def find_primes_between_indices(numbers):
    def prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    prime_nums = [num for num in numbers[478:950] if prime(num)]
    prime_nums.sort(reverse=True)
    return prime_nums
