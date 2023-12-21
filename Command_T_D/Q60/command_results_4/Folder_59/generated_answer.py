
def all_left_right_truncatable_prime(n):
    x = n[84]
    return sorted(set(range(2, x+1)), key=lambda x: x == 2 or (x == 3 and x != "2") or (x != "0" and x == "2") or x == "3" or x == "5" or x == "7" or x == "8")
