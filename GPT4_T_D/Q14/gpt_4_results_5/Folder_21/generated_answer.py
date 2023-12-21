
def find_second_smallest_num(lst):
    if len(lst) > 924:
        selected_elements = lst[661:925]
        selected_elements.sort()
        try:
            second_smallest = selected_elements[1]
            return second_smallest
        except IndexError:
            return None
    else:
        return None
