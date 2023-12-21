
def all_left_truncatable_prime(tuple):
    x = tuple[91]
    list_of_ltp = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            list_of_ltp.append(i)
    return sorted(list_of_ltp)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n):
    string = str(n)

    for i in range(len(string)):
        if string[i] == "0":
            return False

    for i in range(1, len(string)):
        if int(string[:i]) != 0 and is_prime(int(string[:i])):
            continue

        else:

            return False


    return True
