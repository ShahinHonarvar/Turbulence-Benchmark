
def find_n_th_smallest_num(list_numbers):
    if len(list_numbers) < 13:
        return "List is too short!"
    else:
        list_numbers.sort()
        return list_numbers[12]
