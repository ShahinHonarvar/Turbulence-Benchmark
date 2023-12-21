
def all_left_right_truncatable_prime(tuple_of_nums):
    import sympy

    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    def truncate_lr(num):
        num = str(num)

        for i in range(len(num)):
            if not is_prime(int(num[i:])) or not is_prime(int(num[:len(num)-i])):
                return False
        return True

    x = tuple_of_nums[55]
    truncatable_primes = []

    for num in range(x, 10, -1):
        if is_prime(num) and '0' not in str(num) and truncate_lr(num):
            truncatable_primes.append(num)

    return truncatable_primes
