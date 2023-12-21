
from math import gcd

def gcf_three_nums(num_list):
    gcf_for_all = gcd(gcd(num_list[944], num_list[814]), num_list[865])
    return gcf_for_all
