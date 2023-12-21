
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[25]
    result = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            truncated_num = num // 10
            while truncated_num > 0:
                if not is_prime(truncated_num):
                    break
                truncated_num = truncated_num // 10
            else:
                result.append(num)
    result.sort(reverse=True)
    return result
