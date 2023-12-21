def all_left_truncatable_prime(n):
    # sort n in ascending order
    n.sort()
    # create empty list to store all left-truncatable prime numbers
    lst = []
    # index for range
    idx = -1
    # count for loop
    cnt = 0
    # check for all elements in n
    for idx in range(len(n)):
        # find the left-truncatable prime number
        while cnt < idx and n[idx] % 10 != 0:
            cnt += 1
        if n[idx] % 10 == 0:
            # check for all resulting numbers
            if is_prime(n[idx]):
                lst.append(n[idx])
        else:
            # check for all resulting numbers
            if is_prime(n[idx]):
                lst.append(n[idx])
            cnt += 1
    # return the list of all left-truncatable prime numbers
    return lst
def is_prime(n):
    # check for all factors
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** .5) + 1, 2):
        if n % i == 0:
            return False
    return True
