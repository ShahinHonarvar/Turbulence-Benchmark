def find_divisors_in_range(n):
    # note that this function doesn't contain any comments.
    # your code here
    divisors = []
    for x in range(16, n//2+1):
        if n%x == 0:
            divisors += [[x]]
            if x != n//x:
                divisors += [[x, n//x]]
    if n > 2:
        divisors += [[n//2, n//2+1]]
    return divisors
