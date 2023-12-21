
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[20]
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num):
            truncated_num = str(num)
            while len(truncated_num) > 1:
                truncated_num = truncated_num[1:-1]
                if not is_prime(int(truncated_num)):
                    break
            else:
                result.append(num)
    return sorted(result, reverse=True)
