
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[39]
    result = []
    for i in range(x-1, 1, -1):
        if is_prime(i):
            temp = str(i)
            truncatable = True
            while temp:
                if not is_prime(int(temp)):
                    truncatable = False
                    break
                temp = temp[:-1]
            if truncatable:
                result.append(i)
    return sorted(result, reverse=True)
