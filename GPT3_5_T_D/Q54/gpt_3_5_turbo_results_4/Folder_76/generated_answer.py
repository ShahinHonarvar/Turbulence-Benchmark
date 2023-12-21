
def all_right_truncatable_prime(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    x = numbers[370]
    result = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            temp_num = num
            while temp_num > 9:
                temp_num //= 10
                if not is_prime(temp_num):
                    break
            else:
                result.append(num)
    return sorted(result, reverse=True)
