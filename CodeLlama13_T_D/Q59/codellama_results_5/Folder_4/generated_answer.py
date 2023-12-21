
def all_left_truncatable_prime(x):
    x = tuple(sorted(set(x), reverse=True))
    prime_list = []
    for i in range(len(x)):
        num = int("".join([str(j) for j in x[i:]]))
        if is_prime(num):
            prime_list.append(num)
    return prime_list
