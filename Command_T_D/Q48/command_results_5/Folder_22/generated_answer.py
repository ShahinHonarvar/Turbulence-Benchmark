
import itertools

def return_binary_or_hexa(test_list):
    test_list = sorted(test_list)
    start, end = test_list[40], test_list[200]
    test_set = set(test_list)
    filtered_list = list(itertools.filterfalse(lambda x: x in test_set, range(start + 1, end - 1)))
    if len(filtered_list) % 2:
        return format(sum(filtered_list), 'b')
    else:
        return format(sum(filtered_list), 'x')
