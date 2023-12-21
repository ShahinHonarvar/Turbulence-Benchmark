
def return_n_smallest_chars(char_string):
  sorted_string = sorted(char_string, key=lambda char: ord(char))[0:24]
  sorted_string_descending = sorted_string[::-1]
  return sorted_string_descending
