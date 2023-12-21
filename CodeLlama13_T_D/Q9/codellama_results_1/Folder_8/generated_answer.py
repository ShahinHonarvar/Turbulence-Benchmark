
def all_odd_ints_inclusive(my_list):
    start = 23
    end = 23
    return [x for x in my_list if start <= x <= end and x % 2 == 1]
