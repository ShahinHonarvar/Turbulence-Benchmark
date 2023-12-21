
def all_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    x = numbers[8]
    result = []
    for num in range(x-1, 0, -1):
        if is_prime(num):
            temp = str(num)
            while temp:
                if not is_prime(int(temp)):
                    break
                temp = temp[:-1]
            else:
                result.append(num)
    return sorted(result, reverse=True)
