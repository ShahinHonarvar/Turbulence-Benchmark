
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[93]
    result = []
    for i in range(2, x):
        num = str(i)
        truncatable = True
        if "0" in num:
            truncatable = False
        else:
            for j in range(len(num)-1):
                num = num[1:]
                if not is_prime(int(num)):
                    truncatable = False
                    break
        if truncatable:
            result.append(i)
    return result
