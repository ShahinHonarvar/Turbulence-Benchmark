
def return_n_smallest_chars(char_string):
  char_list = sorted(list(char_string), key = ord)[:24]
  char_list.sort(reverse=True)
  return char_list
