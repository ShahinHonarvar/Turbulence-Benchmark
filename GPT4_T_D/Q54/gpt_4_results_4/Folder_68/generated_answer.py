
def all_right_truncatable_prime(tup):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        num_str = str(n)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True

    x = tup[1]
    result = []
    for each in range(10, x):
        if is_right_truncatable(each):
            result.append(each)
    result.sort(reverse=True)
    return result
