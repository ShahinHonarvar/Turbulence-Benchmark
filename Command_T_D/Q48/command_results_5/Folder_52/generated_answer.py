
import itertools

def return_binary_or_hexa(test_tup):
    non_list_str = set(test_tup)
    non_list_int = [int(x) for x in non_list_str]
    a = non_list_int[38]
    b = non_list_int[81]
    # Add all integers from a+1 to b-1 that are not present in the list between 38 and 81
    sum_str = ""
    for curr in range(a + 1, b - 1):
        if curr not in non_list_int:
            # odd number
            sum_str += curr
            break
    # even number
    for curr in range(a + 2, b - 2):
        if curr not in non_list_int:
            sum_str += curr
            break
    # print(sum_str)
    if len(sum_str) % 2 == 0:
        return hex(int(sum_str))
    else:
        return bin(int(sum_str))
