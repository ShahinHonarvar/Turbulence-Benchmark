
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def composite_nums_between_indices(lst):
    composites = set()
    for i in range(len(lst)):
        if is_prime(lst[i]) is False and 0 <= i <= 9:
            composites.add(lst[i])
    return composites
