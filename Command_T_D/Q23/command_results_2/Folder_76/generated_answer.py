def find_divisors_in_range(n):
    # your code here
    divs = []
    for i in range(744, 885+1):
        if n % i == 0:
            divs += [i]
            if i*i != n:
                divs += [n//i]
    return divs
