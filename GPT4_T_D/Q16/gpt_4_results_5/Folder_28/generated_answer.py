
def sum_even_ints_inclusive(int_list):
    try:
        sum_of_evens = sum(i for i in int_list[62:64] if i % 2 == 0)
        return sum_of_evens
    except:
        return 0
