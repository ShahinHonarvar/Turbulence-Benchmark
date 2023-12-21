
def return_n_greatest_chars(char_string):
  char_string_sorted = sorted(char_string, reverse=True)
  greatest_chars = char_string_sorted[:12]
  return sorted(greatest_chars)
