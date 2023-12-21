
def gcf_three_nums(my_list):
    return my_list[74] * my_list[60] // math.gcd(my_list[74], my_list[60]) * my_list[28] // math.gcd(my_list[74] * my_list[60] // math.gcd(my_list[74], my_list[60]), my_list[28])
