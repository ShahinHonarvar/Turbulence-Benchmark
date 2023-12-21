
def all_left_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[49]
    list_of_ltp = []
    for i in range(2, x):
        if is_prime(i) and is_ltp(i, x):
            list_of_ltp.append(i)
    return sorted(list_of_ltp)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_ltp(n, x):

    if n < 2:

        return False


    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False


    for j in range(49, -1, -1):

        if tuple_of_integers[j] == 0:

            continue


        else:

            break


    while True:


        n = int(str(n)[:-1])

        if n < 2:

            return False


        for i in range(2, int(n ** 0.5) + 1):

            if n % i == 0:

                return False


        if n >= x:

            break


    return True
