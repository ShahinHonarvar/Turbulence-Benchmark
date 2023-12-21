
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[70]
    result = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            left_truncatable = True
            for i in range(len(str(num))):
                truncated_num = int(str(num)[i:])
                if not is_prime(truncated_num):
                    left_truncatable = False
                    break
            if left_truncatable:
                result.append(num)
    return result
