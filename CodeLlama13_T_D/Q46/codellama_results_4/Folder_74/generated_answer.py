
def gcf_three_nums(my_list):
    if len(my_list) < 90:
        return None
    else:
        return math.gcd(my_list[99], math.gcd(my_list[95], my_list[80]))
