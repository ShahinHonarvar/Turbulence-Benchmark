
def all_left_right_truncatable_prime(x):
    lst = []
    for i in range(2, x+1):
        if is_truncatable_prime(i) and not any(i % j == 0 for j in range(2, int(i**0.5)+1)):
            lst.append(i)
    return sorted(lst, reverse=True)

def is_truncatable_prime(n):
    if n <= 1 or any(n % i == 0 for i in range(2, int(n**0.5)+1)):
        return False
    for i in range(int((len(str(n))-1)//2), -1, -1):
        if not is_prime(int(str(n)[:i])):
            return False
        if not is_prime(int(str(n)[i+1:])):
            return False
    return True

def is_prime(n):
    if n <= 1 or any(n % i == 0 for i in range(2, int(n**0.5)+1)):
        return False
    return True
