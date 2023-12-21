
def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n%2 == 0:
        return False
    if n < 9:
        return True
    if n%3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0:
            return False
        if n%(f + 2) == 0:
            return False
        f +=6
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    x = numbers[81]
    for num in range(x, 0, -1):
        if is_prime(num):
            string_num = str(num)
            if '0' not in string_num:
                is_left_right_truncatable = True
                for i in range(1, len(string_num)):
                    left_trunc_num = int(string_num[i:])
                    right_trunc_num = int(string_num[:i])
                    if not is_prime(left_trunc_num) or not is_prime(right_trunc_num):
                        is_left_right_truncatable = False
                        break
                if is_left_right_truncatable:
                    result.append(num)
    return sorted(result, reverse=True)
