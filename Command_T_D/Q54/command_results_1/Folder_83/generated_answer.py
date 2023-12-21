def all_right_truncatable_prime(x):
    for i in range(2, int(x ** .5) + 1):
        if all(i % j != 0 for j in range(3, int(str(i)[-1]) + 1)):
            yield i
