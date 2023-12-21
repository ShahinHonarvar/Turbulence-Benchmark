
def all_right_truncatable_prime(tuple):
    x = tuple[3]
    prime_list = []
    for i in range(2,x+1):
        if is_prime(i) == True:
            if is_right_truncatable_prime(i) == True:
                prime_list.append(i)
    prime_list.sort(reverse=True)
    return prime_list

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    for i in range(len(str(n)) - 1, 0, -1):
        if str(n)[i:] == int(str(n)[i:]) ** len(str(n)) - i:
            return True
    return False
