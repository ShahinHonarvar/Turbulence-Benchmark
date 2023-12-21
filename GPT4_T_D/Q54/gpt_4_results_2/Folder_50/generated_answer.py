
def all_right_truncatable_prime(tup):
    def is_prime(n):
        if n==1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True

    def is_right_truncatable(n):
        n = str(n)
        for i in range(len(n)):
            if not is_prime(int(n[:len(n)-i])):
                return False
        return True

    x = tup[57]
    res = []
    for i in range(2, x):
        if is_right_truncatable(i):
            res.append(i)
    return sorted(res,reverse=True)
