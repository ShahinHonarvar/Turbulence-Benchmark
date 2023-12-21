
def all_left_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        str_num = str(num)
        while str_num:
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[1:-1]
        return True

    x = numbers[175]
    res = []
    for i in range(11, x + 1):
        if is_truncatable_prime(i):
            res.append(i)
    return res
