import sys
def all_left_truncatable_prime(l):
    # code here
    # sys.setrecursionlimit(10**7)
    # sys.setprofile(f"profile.txt")
    return [int(x) for x in range(2, l[0]+1) if all(x%d==0 for d in range(2, int(str(x)[0])+1)) and all(str(x)[:d] in '2357' for d in range(1, int(str(x)[0])+1)) ]
