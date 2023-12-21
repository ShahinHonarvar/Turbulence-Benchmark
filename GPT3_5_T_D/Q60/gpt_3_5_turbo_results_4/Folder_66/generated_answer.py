
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[25]
    result = []
    for num in range(x, 0, -1):
        if '0' in str(num):
            continue
        truncated_num = str(num)
        while len(truncated_num) > 2:
            truncated_num = truncated_num[1:-1]
            if not is_prime(int(truncated_num)):
                break
        else:
            result.append(num)
    return sorted(result, reverse=True)
