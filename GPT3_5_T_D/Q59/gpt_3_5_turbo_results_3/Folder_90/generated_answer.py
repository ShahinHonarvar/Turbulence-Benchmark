
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[466]
    result = []
    for num in range(x-1, 2, -1):
        if '0' not in str(num):
            is_truncatable = True
            for i in range(len(str(num))):
                truncated_num = int(str(num)[i:])
                if not is_prime(truncated_num):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(num)
    return result
