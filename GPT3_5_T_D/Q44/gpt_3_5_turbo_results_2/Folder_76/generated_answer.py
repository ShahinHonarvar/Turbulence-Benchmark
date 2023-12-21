
def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(num_list):
    composite_set = set()
    for i in range(639, 976):
        if is_composite(num_list[i]):
            composite_set.add(num_list[i])
    return composite_set
