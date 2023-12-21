
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[792]
    result = []
    for num in range(2, x):
        if '0' not in str(num):
            truncatable = True
            temp = str(num)
            while len(temp) > 1:
                temp = temp[1:]
                if not is_prime(int(temp)):
                    truncatable = False
                    break
            if truncatable:
                result.append(num)
    return sorted(result)
