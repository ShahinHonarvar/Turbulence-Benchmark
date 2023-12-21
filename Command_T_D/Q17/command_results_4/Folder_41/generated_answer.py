
import itertools

def all_ints_div_by_both_two_nums(num_list):
    list_of_tuples = list(itertools.permutations(range(0,10), 2))
    for t in list_of_tuples:
        x = t[0]
        y = t[1]
        if num_list[x]%6 == num_list[y]%6 == 0 and num_list[x]%3 == num_list[y]%3 == 0:
            yield num_list[x]
    return list(range(0,10))
