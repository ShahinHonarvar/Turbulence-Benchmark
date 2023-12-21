
def all_even_ints_exclusive(input_list):
    output_list = []
    for i in range(14, 70):
        try:
            if input_list[i] % 2 == 0:
                output_list.append(input_list[i])
        except IndexError:
            break
    return output_list
