
def all_left_right_truncatable_prime(numbers):
    from sympy import isprime

    def truncatable_prime(num):
        if '0' in str(num):
            return False

        return all(isprime(int(str(num)[:i])) and isprime(int(str(num)[-i:])) for i in range(1, len(str(num)) + 1))

    x = numbers[100]
    res = [i for i in range(10, x+1) if truncatable_prime(i)]
    res.sort(reverse = True)

    return res
