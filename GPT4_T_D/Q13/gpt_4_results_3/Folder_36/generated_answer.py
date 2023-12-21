
def find_second_largest_num(lst):
    try:
        sorted_nums = sorted(lst[246:751])
        return sorted_nums[-2]
    except IndexError:
        return None
