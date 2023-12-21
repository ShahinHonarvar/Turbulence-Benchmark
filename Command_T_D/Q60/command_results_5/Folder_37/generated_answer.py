
def all_left_right_truncatable_prime(x):
    # your code here
    return sorted([y for y in range(2, x + 1) if all(str(y).count(d) == 1 for d in str(y) if d == '0')], reverse=True)
