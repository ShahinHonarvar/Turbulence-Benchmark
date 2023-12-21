
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        digits = str(n)
        for i in range(len(digits)):
            left_trunc = int(digits[i:])
            right_trunc = int(digits[:len(digits)-i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True

    x = numbers[18]
    result = []
    for i in range(2, x+1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
