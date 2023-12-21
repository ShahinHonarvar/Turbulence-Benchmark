
def all_left_right_truncatable_prime(x):
    result = []
    for i in range(x // 10, -1, -1):
        j = str(i)
        while j[0] == "0" or j[-1] == "0":
            j = j[1:-1]
        if str(i) == j and is_prime(i):
            result.append(i)
    return result

def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(5, int(x ** .5) + 1):
        if x % i == 0:
            return False
    return True
