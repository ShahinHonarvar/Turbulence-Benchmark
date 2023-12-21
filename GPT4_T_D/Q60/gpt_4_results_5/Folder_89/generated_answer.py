
def all_left_right_truncatable_prime(nums):
    from sympy import isprime

    x = nums[97]

    def truncate(n):
        n = str(n)
        return [int(n[i:]) for i in range(len(n))] + [int(n[:i+1]) for i in range(len(n))]

    def is_truncatable(n):
        return all(isprime(i) for i in truncate(n))

    result = [i for i in range(11, x+1) if '0' not in str(i) and is_truncatable(i)]
    result.sort(reverse=True)
    
    return result
