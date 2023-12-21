
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[39]
    result = []
    for i in range(2, x):
        if '0' not in str(i):
            temp = str(i)
            is_left_truncatable = True
            while temp:
                if not is_prime(int(temp)):
                    is_left_truncatable = False
                    break
                temp = temp[1:]
            if is_left_truncatable:
                result.append(i)
    return sorted(result, reverse=True)
