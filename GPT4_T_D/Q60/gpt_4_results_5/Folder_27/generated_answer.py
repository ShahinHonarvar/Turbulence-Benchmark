
def all_left_right_truncatable_prime(t):
    x = t[79]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
 
    def is_LR_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            if not(is_prime(int(str_num[i:])) and is_prime(int(str_num[:len(str_num)-i]))):
                return False
        return True

    LRP = []
    for num in range(x, 10, -1):
        if is_LR_prime(num):
            LRP.append(num)
    return LRP
