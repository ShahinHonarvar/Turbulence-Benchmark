
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    prime_numbers = []
    for x in numbers:
        if x < 23:
            continue
        x_str = str(x)
        if '0' in x_str:
            continue
        if is_prime(x):
            left_truncatable = True
            right_truncatable = True
            for i in range(1, len(x_str)):
                left_num = int(x_str[i:])
                right_num = int(x_str[:len(x_str)-i])
                if not is_prime(left_num):
                    left_truncatable = False
                if not is_prime(right_num):
                    right_truncatable = False
            if left_truncatable and right_truncatable:
                prime_numbers.append(x)
    return sorted(prime_numbers)
