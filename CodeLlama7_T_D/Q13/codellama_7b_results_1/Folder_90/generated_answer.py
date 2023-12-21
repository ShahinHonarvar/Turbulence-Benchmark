
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None

    sorted_list = sorted(my_list)

    for i in range(len(sorted_list) - 1):
        if i >= 262 and i <= 746:
            if sorted_list[i + 1] > sorted_list[i]:
                return sorted_list[i]

    return None
