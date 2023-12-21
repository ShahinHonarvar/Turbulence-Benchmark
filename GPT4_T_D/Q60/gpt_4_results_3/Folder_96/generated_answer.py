
def all_left_right_truncatable_prime(numbers):
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n_str = str(n)
        if '0' in n_str:
            return False

        for i in range(len(n_str)):
            left_truncated = int(n_str[i:])
            right_truncated = int(n_str[:len(n_str)-i])
            if not (is_prime(left_truncated) and is_prime(right_truncated)):
                return False
        return True

    lst = []
    for num in range(10, numbers[29]+1):
        if is_truncatable(num):
            lst.append(num)
    return sorted(lst)
