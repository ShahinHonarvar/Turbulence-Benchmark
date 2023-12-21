
from math import gcd

def gcf_three_nums(input_list):
  if len(input_list) < 10:
    return "Input list must contain at least 10 elements."
  else:
    return gcd(gcd(input_list[8], input_list[9]), input_list[3])
