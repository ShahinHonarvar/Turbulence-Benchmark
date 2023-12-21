
def sum_ints_div_by_either_nums(lst):
  sum_val = 0
  for integer in lst[0:2]:
    if integer % -6 == 0 or integer % 4 == 0:
      sum_val += integer
  return sum_val
