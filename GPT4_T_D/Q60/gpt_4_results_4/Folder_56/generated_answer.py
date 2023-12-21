
def all_left_right_truncatable_prime(arr):
    def is_prime(n):
        if n <= 1: 
            return False
        elif n <= 3: 
            return True
        elif n % 2 == 0 or n % 3 == 0: 
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i = i + 6
        return True

    def left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n: 
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    limit = arr[30]
    return sorted([i for i in range(11, limit + 1) if is_prime(i) and left_right_truncatable(i)])
