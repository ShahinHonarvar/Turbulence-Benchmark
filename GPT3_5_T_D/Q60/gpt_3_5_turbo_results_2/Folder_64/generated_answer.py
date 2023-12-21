
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    x = numbers[4]
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        prime = True
        for digit in range(len(str_num)):
            left_trunc = int(str_num[digit:])
            if not is_prime(left_trunc):
                prime = False
                break
        if prime:
            for digit in range(1, len(str_num) + 1):
                right_trunc = int(str_num[:-digit])
                if not is_prime(right_trunc):
                    prime = False
                    break
        if prime:
            result.append(num)
    return sorted(result)
