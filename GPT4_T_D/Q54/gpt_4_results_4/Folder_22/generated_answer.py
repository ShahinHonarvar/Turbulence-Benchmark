
def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            return False
    return True

def is_right_truncatable(n):
    number = str(n)
    for i in range(len(number)):
        if not is_prime(int(number[i:])):
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[85]
    result = []
    
    for i in range(2, x):
        if is_right_truncatable(i):
            result.append(i)

    return sorted(result)
