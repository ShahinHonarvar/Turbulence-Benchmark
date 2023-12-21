
def all_left_right_truncatable_prime(tup):
    x = tup[54]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(num):
        if '0' in str(num):
            return False
        length = len(str(num))
        for i in range(length):
            if not is_prime(int(str(num)[i:])):
                return False
            if not is_prime(int(str(num)[:length-i])):
                return False
        return True

    result = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)
