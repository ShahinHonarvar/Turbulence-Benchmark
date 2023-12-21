
def find_second_largest_num(num_list):
    if len(num_list[27:56]) > 1:
        num_list[27:56].sort(reverse=True)
        return num_list[27:56][1]
    else:
        return None
