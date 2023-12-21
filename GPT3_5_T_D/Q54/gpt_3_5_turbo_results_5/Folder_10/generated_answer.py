 
def all_right_truncatable_prime(numbers):
    def is_prime(num):
        if num == 1 or num == 0:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    x = numbers[38]
    result = []
    for i in range(x - 1, 1, -1):
        num = i
        is_right_truncatable_prime = True
        while num > 0:
            if not is_prime(num):
                is_right_truncatable_prime = False
                break
            num = num // 10
        if is_right_truncatable_prime:
            result.append(i)
    return sorted(result, reverse=True)
