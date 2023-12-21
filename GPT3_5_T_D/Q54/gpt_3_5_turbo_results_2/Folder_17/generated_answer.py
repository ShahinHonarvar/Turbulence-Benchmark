
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[36]
    result = []
    for i in range(x, 0, -1):
        if is_prime(i):
            truncatable = True
            num = str(i)
            while num:
                if not is_prime(int(num)):
                    truncatable = False
                    break
                num = num[:-1]
            if truncatable:
                result.append(i)
    result.sort(reverse=True)
    return result
