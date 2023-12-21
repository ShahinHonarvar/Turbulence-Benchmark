
def all_left_right_truncatable_prime(tup):
    x = tup[1]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_truncatable(n):
        sn = str(n)
        if '0' in sn:
            return False
        for i in range(len(sn)):
            if not is_prime(int(sn[i:])) or not is_prime(int(sn[:len(sn)-i])):
                return False
        return True
    
    return sorted([n for n in range(11, x+1) if is_truncatable(n)], reverse=True)
