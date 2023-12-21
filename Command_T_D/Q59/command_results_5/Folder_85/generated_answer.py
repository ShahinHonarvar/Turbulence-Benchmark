def all_left_truncatable_prime(test_tup):
    res = []
    for num in range(1, test_tup[94]):
        str_num = str(num)
        prime_str = str_num[0] + str_num[1:]
        is_prime = True
        if prime_str == "2" or prime_str == "3":
            continue
        elif prime_str[0] == "5":
            if prime_str[1] != "0":
                continue
        elif prime_str[0] == "7":
            if prime_str[1] != "0" and prime_str[2] != "0":
                continue
        elif prime_str[0] == "9":
            if prime_str[1] != "0" and prime_str[2] != "0" and prime_str[3] != "0":
                continue
        elif prime_str[0] == "5" or prime_str[0] == "7" or prime_str[0] == "9":
            for c in range(1, len(prime_str)):
                if prime_str[c] == "0":
                    is_prime = False
                    break
        if is_prime:
            res.append(num)
    return res
