
def all_left_right_truncatable_prime(x):
    for i in range(2, x+1):
        if i % 2 == 1 and all(str(i).count(d) == 1 for d in str(i) if d in '0123456789'):
            yield i
    return sorted(list(range(2, x+1)), reverse=True)
