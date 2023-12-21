
def find_second_smallest_num(list_num):
    if 556<len(list_num)>208:
        subset = list_num[209:557]
        subset.sort()
        try:
            return subset[1]
        except IndexError:
            return None
    else:
        return None
