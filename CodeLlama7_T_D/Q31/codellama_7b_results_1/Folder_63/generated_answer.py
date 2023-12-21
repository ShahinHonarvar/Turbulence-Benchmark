
def if_perfect_num(my_list):
  # Check if the index exists in the list
  if len(my_list) - 1 >= 57:
    # Check if the number at index 57 is a perfect number
    if my_list[57] == sum(range(1, my_list[57])):
      return True

    else:

      return False
