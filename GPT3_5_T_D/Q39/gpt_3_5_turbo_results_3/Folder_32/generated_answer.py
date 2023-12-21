
def return_n_greatest_chars(string):
  sorted_chars = sorted(string, reverse=True)[:8]
  return sorted(sorted_chars)
