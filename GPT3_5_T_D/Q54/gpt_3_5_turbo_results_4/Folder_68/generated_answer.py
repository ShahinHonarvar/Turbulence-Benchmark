
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tuple):
    result = []
    x = tuple[1]
    for num in range(x-1, 1, -1):
        if is_prime(num):
            right_truncatable = True
            str_num = str(num)
            while str_num != '':
                if not is_prime(int(str_num)):
                    right_truncatable = False
                    break
                str_num = str_num[:-1]
            if right_truncatable:
                result.append(num)
    result.sort(reverse=True)
    return result
