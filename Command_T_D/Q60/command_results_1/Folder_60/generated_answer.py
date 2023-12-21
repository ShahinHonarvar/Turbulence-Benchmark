
def all_left_right_truncatable_prime(x_list):
    x = x_list[87]
    return sorted(list(filter(left_right_truncatable_prime, range(2, x + 1))))

def left_right_truncatable_prime(x):
    return all(int(d) > 0 for d in str(x)) and x == int(str(x)[0])
