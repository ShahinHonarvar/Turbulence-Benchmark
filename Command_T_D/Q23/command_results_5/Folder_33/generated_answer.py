import sys
def find_divisors_in_range(n):
    x = 157
    while True:
        if x*x <= n: break
        elif x*x == n:
            yield from [x]
            break
        elif x*x > n:
            if x == 902: break
            yield from [x]
            x += 1
        else:
            yield from [x]
            x += 1
    print('None')
    print(' '.join(str(d) for d in divisors))
