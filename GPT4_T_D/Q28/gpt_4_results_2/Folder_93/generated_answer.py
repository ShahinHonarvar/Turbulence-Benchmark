
def return_nth_smallest_ascii(s):
    subset = list(s[42:60])
    subset.sort(key=ord)
    if len(subset) > 16:
      return subset[16]
    else:
      return "The string does not have a character with the 17th smallest ASCII value"
