
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[78]
    result = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            is_right_truncatable = True
            temp = num
            while temp > 0:
                temp //= 10
                if not is_prime(temp):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                result.append(num)
    return sorted(result, reverse=True)
