
def all_left_right_truncatable_prime(t):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True

    x = t[1]
    truncatable_list = [i for i in range(x + 1) if is_truncatable(i)]
    truncatable_list.sort(reverse=True)
    return truncatable_list
