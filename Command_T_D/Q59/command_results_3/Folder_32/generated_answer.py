import itertools
def all_left_truncatable_prime(test_input):
    input_list = test_input[1]
    input_num = int(test_input[0])
    input_list = sorted(set(input_list))
    input_list_alt = list(itertools.permutations(input_list))
    input_list_alt = sorted(input_list_alt)
    return input_list_alt
