 def all_left_right_truncatable_prime(nums):
    x = nums[77]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)
def is_left_right_truncatable_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    s = str(n)

    for i in range(len(s)):
        if s[i] == '0':
            return False

    left_right_truncatable = True

    for i in range(1, len(s)):
        if not is_prime(int(s[:i] + s[i+1:])):
            left_right_truncatable = False

            break

    return left_right_truncatable
def is_prime(n):

    if n < 2:

        return False


    for i in range(2, int(math.sqrt(n)) + 1):

        if n % i == 0:

            return False


    return True
