
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (GCF) of the elements at indices 92, 69 and 95
    i = 1
    while True:
        if my_list[92] % i == 0 and my_list[69] % i == 0 and my_list[95] % i == 0:
            return i
