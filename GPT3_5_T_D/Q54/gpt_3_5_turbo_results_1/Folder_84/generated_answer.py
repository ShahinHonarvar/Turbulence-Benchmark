
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[630]
    result = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            truncatable = True
            temp = i
            while temp >= 10:
                temp //= 10
                if not is_prime(temp):
                    truncatable = False
                    break
            if truncatable:
                result.append(i)
    result.sort(reverse=True)
    return result
