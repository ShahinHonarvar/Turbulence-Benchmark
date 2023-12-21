
def all_left_right_truncatable_prime(t):
    def is_prime(n):
        if n < 2:
            return False
        else:
            for i in range(2, int(n**0.5)+1):
                if n%i == 0:
                    return False
            return True

    def left_right_truncate_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        else:
            for i in range(len(str_n)):
                if not is_prime(int(str_n[i:len(str_n)])) or not is_prime(int(str_n[0:i+1])):
                    return False
        return True

    x = t[98]
    return [num for num in range(10, x+1) if left_right_truncate_prime(num)]
