
def all_left_right_truncatable_prime(x):
    # your code here
    #mine
    return sorted(list(range(3, x, 2)), key=lambda i: str(i))
