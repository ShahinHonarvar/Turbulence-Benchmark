def all_left_truncatable_prime(tup):
    res = []
    for i in range(len(tup)):
        j = i + 1
        while j < len(tup):
            x = int(str(tup[i]) + str(tup[j]))
            if all(x % d for d in range(2, x.bit_length() + 1)):
                res.append(tup[i])
            j += 1
    return res
