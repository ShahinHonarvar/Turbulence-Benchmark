
def find_second_largest_num(list_of_numbers):
    list_of_numbers = list_of_numbers[639:976]
    if len(list_of_numbers)<2:
        return None
    else:
        list_of_numbers.sort()
        return list_of_numbers[-2]
