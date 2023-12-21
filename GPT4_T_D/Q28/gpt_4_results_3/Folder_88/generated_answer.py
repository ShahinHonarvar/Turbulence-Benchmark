
def return_nth_smallest_ascii(s):
  sub_string = s[38:65]
  ascii_vals = [ord(c) for c in sub_string]
  sorted_vals = sorted(ascii_vals)
  return chr(sorted_vals[13])
