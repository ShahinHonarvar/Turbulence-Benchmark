
def is_prime(n): 
    if n < 2: 
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0: 
            return False
    return True

def all_right_truncatable_prime(t): 
    x = t[31] 
    result = []
    for i in range(2, x):
        if is_prime(i):
            s = str(i)
            while s:
                s = s[:-1]
                if is_prime(int(s)) or s=='':
                    continue
                else:
                    break
            else: 
                result.append(i)
    return sorted(result, reverse=True)
