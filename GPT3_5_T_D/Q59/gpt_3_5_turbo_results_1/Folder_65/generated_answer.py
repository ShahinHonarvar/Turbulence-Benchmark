
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    truncatable_primes = []
    for i in range(2, numbers[32]):
        if '0' in str(i):
            continue
        is_truncatable = True
        curr_num = str(i)
        while curr_num:
            if not is_prime(int(curr_num)):
                is_truncatable = False
                break
            curr_num = curr_num[1:]
        if is_truncatable:
            truncatable_primes.append(i)

    return sorted(truncatable_primes)
