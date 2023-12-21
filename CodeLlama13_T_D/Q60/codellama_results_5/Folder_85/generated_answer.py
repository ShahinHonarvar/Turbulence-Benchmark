
def all_left_right_truncatable_prime(x):
    lst = []
    for i in range(10**94, x+1):
        s = str(i)
        if not '0' in s:
            for j in range(len(s)):
                if is_prime(int(s[:j])) and is_prime(int(s[j+1:])):
                    lst.append(i)
                    break
    return sorted(lst)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
