
def all_left_truncatable_prime(my_tuple):
    x = my_tuple[630]
    result = []
    for i in range(1, x + 1):
        if is_prime(i) and not contains_zero(str(i)):
            if all([is_prime(int(i[:j])) for j in range(1, len(i))]):
                result.append(i)
    return sorted(result, reverse=True)
