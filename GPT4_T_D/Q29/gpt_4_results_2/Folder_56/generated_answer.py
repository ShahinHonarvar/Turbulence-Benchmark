
def gcf_two_nums(num_list):
    def gcf(a, b):
        while(b):
            a, b = b, a % b
        return a
    
    if len(num_list) > 84 and len(num_list) > 13:
        return gcf(num_list[84], num_list[13])
    else:
        return "List not long enough"
