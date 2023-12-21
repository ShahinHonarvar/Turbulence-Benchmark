
def find_second_largest_num(numbers):
    index_62_to_92 = numbers[62:93]
    if len(index_62_to_92) < 2:
        return None
    else:
        index_62_to_92.sort()
        return index_62_to_92[-2]
