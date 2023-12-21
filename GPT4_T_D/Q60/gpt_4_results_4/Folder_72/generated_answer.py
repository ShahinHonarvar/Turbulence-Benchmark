
def all_left_right_truncatable_prime(integers):
    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            left = int(num_str[i:])
            right = int(num_str[:len(num_str)-i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True

    x = integers[31]
    result = [i for i in range(x + 1) if is_prime(i) and is_left_right_truncatable(i)]
    return sorted(result, reverse=True)
