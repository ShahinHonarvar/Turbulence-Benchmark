
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[466]
    result = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            truncatable = True
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    truncatable = False
                    break
                temp //= 10
            if truncatable:
                result.append(num)
    return sorted(result, reverse=True)
