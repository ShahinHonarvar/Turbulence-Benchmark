
def sum_in_range(lst):
    return sum(num for num in lst if 136 <= num <= 618) if any(136 <= num <= 618 for num in lst) else 0
