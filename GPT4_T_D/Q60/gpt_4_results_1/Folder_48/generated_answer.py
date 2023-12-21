
def all_left_right_truncatable_prime(nums):
    import sympy

    def check_prime(num):
        if sympy.isprime(num):
            num_str = str(num)
            for i in range(1,len(num_str)):
                if not sympy.isprime(int(num_str[i:])) or not sympy.isprime(int(num_str[:-i])):
                    return False
            return True
        return False

    def find_prime(n):
        return [x for x in range(10, n+1) if '0' not in str(x) and check_prime(x)]

    try:
        x = nums[835]
        return sorted(find_prime(x))
    except IndexError:
        return []
