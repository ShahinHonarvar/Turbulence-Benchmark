
def all_right_truncatable_prime(arg):
    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for current in range(3, int(n ** 0.5) + 1, 2):
            if n % current == 0: 
                return False
        return True
   
    def is_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
 
    x = arg[30]
    result = []
    for i in range(0, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)
