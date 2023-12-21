
def find_second_largest_num(numbers):
    sorted_num = sorted(numbers[:11], reverse=True)
    if len(sorted_num) > 1:
        return sorted_num[1]
    else:
        return None
