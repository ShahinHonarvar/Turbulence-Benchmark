
def all_odd_ints_inclusive(integer_list):
    odd_ints = []
    for num in integer_list[209:557]:
        if num % 2 != 0:
            odd_ints.append(num)
    return odd_ints
