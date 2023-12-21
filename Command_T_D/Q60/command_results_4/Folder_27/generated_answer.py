
def all_left_right_truncatable_prime(nums):
    left_right_truncatable_primes = []
    for num in nums:
        prime = True
        while len(str(num)) > 1:
            if str(num)[0] == '0':
                break
            if str(num)[-1] == '0':
                break
            num //= 10
            if not num % 10:
                break
            prime = num % 10 in [2, 3, 5, 7]
        if prime:
            left_right_truncatable_primes.append(num)
    return left_right_truncatable_primes
