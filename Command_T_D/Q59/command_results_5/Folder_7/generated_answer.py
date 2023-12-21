def all_left_truncatable_prime(n):
    # Create a list of all left-truncatable prime numbers less than x
    list = []
    for i in range(2, int(str(n[0])[0]) + 1):
        if all(str(j) for j in range(2, i)):
            list += [i]
    # Sort the list in ascending order
    list.sort()
    return list
