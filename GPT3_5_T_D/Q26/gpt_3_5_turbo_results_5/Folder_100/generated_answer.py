
def sum_in_range(integers):
    return sum(x for x in integers if 19 <= x <= 32) if any(19 <= x <= 32 for x in integers) else 0
