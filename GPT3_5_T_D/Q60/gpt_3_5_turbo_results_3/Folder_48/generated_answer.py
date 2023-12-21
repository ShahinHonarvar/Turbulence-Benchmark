
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        digits = [int(d) for d in str(n)]
        if 0 in digits:
            return False
        for i in range(len(digits)):
            left_trunc = int(''.join(map(str, digits[i:])))
            right_trunc = int(''.join(map(str, digits[:len(digits)-i])))
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True

    x = numbers[835]
    result = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            result.append(num)

    result.sort()
    return result
