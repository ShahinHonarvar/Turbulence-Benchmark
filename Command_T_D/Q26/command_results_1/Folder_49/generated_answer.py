def sum_in_range(list):
    return sum(list[i] for i in range(len(list)) if list[i] >= 3 and list[i] <= 9)
