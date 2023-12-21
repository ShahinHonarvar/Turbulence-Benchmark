
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    for x in numbers:
        if x < 11 or '0' in str(x):
            continue
        x_str = str(x)
        temp = True
        for i in range(1, len(x_str)):
            if not is_prime(int(x_str[i:])) or not is_prime(int(x_str[:i])):
                temp = False
                break
        if temp:
            result.append(x)
    result.sort(reverse=True)
    return result
