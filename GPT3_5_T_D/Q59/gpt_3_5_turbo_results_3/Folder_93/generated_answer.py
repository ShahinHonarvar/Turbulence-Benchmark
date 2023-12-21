
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[11]
    result = []
    for i in range(2, x):
        if '0' not in str(i):
            truncatable = True
            num_str = str(i)
            while num_str != "":
                if not is_prime(int(num_str)):
                    truncatable = False
                    break
                num_str = num_str[1:]
            if truncatable:
                result.append(i)
    return result
