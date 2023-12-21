
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[55]
    result = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            temp = num
            is_right_truncatable_prime = True
            while temp > 0:
                if not is_prime(temp):
                    is_right_truncatable_prime = False
                    break
                temp //= 10
            if is_right_truncatable_prime:
                result.append(num)
    result.sort(reverse=True)
    return result
