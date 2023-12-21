
def all_left_right_truncatable_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num%i == 0:
                return False
        return True

    def truncatable_prime(num):
        num_str = str(num)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:-i-1])):
                return False
        return True

    x = n[65]
    result = []
    for i in range(10, x + 1):
        if "0" not in str(i) and truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result
