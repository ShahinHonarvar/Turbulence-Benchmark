
def all_even_ints_exclusive(input_list):
    exclusive_list = input_list[277:376]
    even_list = [i for i in exclusive_list if i % 2 == 0]
    return even_list
