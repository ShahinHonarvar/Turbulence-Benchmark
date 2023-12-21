
def sum_even_ints_inclusive(int_list):
    if len(int_list) < 210: 
        return 0
  
    sum_of_evens = sum(i for i in int_list[209:557] if i % 2 == 0)
    return sum_of_evens
