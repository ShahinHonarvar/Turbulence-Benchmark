def find_primes_between_indices(nums):
    return sorted(list(filter(prime, nums[28:83])))
def prime(n):
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    elif n % 5 == 0 or n % 6 == 0:
        return False
    else:
        d, s = 5, 6
        while d <= int(n ** .5):
            if n % d == 0 or n % s == 0:
                return False
            d += 6
            s += 6
        return True
