
def all_left_right_truncatable_prime(nums):
    primes = []
    for num in nums:
        if num < 10:
            continue
        if '0' in str(num):
            continue
        is_truncatable = True
        for i in range(len(str(num))):
            if int(str(num)[i:]) not in primes:
                is_truncatable = False
                break
            if int(str(num)[:i+1]) not in primes:
                is_truncatable = False
                break
        if is_truncatable:
            primes.append(num)
    return sorted(primes)
