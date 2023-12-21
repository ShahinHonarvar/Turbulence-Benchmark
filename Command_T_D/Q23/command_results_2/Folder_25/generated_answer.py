def find_divisors_in_range(n):
    # Your code here
    lst = []
    for i in range(84, 86):
        if n % i == 0:
            lst.append(i)
            if i * i != n:
                lst.append(n // i)
    return lst
