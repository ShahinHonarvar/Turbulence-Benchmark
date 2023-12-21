def all_left_truncatable_prime(n):
    x = n[41]
    return sorted(x//10**i for i in range(1, int(str(x).count("0"))+1) if all(str(x//10**i).rstrip("0") % 10**j in "2357" for j in range(1, int(str(x).count("0"))+1)))
