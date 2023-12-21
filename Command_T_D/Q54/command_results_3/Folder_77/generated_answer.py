import bisect
def all_right_truncatable_prime(n):
    #your code here
    #sort by increasing length
    d = {str(i): i for i in range(1, int(n[0] ** .5) + 1) if all(i % d == 0 for d in range(2, int(str(i)) + 1) if d * 10 <= i)}
    return sorted(d.values(), reverse=True)
