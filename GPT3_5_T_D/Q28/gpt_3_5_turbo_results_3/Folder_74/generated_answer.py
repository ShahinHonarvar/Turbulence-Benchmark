
def return_nth_smallest_ascii(string):
    chars = string[1:32]
    ascii_vals = [ord(char) for char in chars]
    sorted_vals = sorted(ascii_vals)
  
    return chr(sorted_vals[5])
