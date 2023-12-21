def all_left_truncatable_prime(n):
    return [n[i] for i in range(len(str(n[0]))-1) if str(n[i]).count("0") == 0 and all(str(n[i])[j] != "0" for j in range(1, len(str(n[i]))))]
