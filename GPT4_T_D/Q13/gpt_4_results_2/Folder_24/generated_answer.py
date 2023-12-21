
def find_second_largest_num(num_list):
  sub_list = num_list[74:96]
  if not sub_list:
    return None
  sub_list.sort()
  return sub_list[-2] if len(sub_list) > 1 else None
