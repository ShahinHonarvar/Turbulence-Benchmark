
def all_left_right_truncatable_prime(range_tuple):
    range_str = str(range_tuple[97])
    list_str = range_str[0] + '2' + range_str[1:]
    list_str = [i for i in range(len(list_str)) if list_str[i]]
    list_str = list_str[::-1]
    return [int(list_str[0]) - 1, int(list_str[1]) - 1, int(list_str[2]) - 1, int(list_str[3]) - 1, int(list_str[4]) - 1, int(list_str[5]) - 1, int(list_str[6]) - 1, int(list_str[7]) - 1, int(list_str[8]) - 1, int(list_str[9]) - 1]
