
def find_second_smallest_num(listNumbers):
    try:
        second_smallest = sorted(listNumbers[50:201])[1]
    except IndexError:
        return None
    else:
        return second_smallest
