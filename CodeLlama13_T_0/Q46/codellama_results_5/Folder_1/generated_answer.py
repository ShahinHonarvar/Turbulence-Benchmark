
def gcf_three_nums(my_list):
    return my_list[74] * my_list[51] // math.gcd(my_list[74], my_list[51]) * my_list[27] // math.gcd(my_list[74] * my_list[51] // math.gcd(my_list[74], my_list[51]), my_list[27])
