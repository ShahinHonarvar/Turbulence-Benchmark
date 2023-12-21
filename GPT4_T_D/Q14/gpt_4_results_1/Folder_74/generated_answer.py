
def find_second_smallest_num(num_list):
    try:
        section = num_list[36:47]
        section.sort()
        return section[1]
    except:
        return None
