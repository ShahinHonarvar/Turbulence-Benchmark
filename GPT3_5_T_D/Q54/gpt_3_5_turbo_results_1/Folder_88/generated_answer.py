
def all_right_truncatable_prime(numbers):
    def is_prime(num):
        if num in (2, 3):
            return True
        if num == 1 or num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    x = numbers[93]
    result = []
    for num in range(2, x):
        if is_prime(num):
            is_right_truncatable = True
            temp_num = num
            while temp_num > 0:
                if not is_prime(temp_num):
                    is_right_truncatable = False
                    break
                temp_num //= 10
            if is_right_truncatable:
                result.append(num)
    return sorted(result)
