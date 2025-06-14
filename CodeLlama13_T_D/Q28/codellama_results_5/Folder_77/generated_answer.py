
def return_nth_smallest_ascii(s):
    s = list(set(s)) # remove duplicates
    ascii_values = [ord(c) for c in s if 63 <= ord(c) <= 76] # get ASCII values between indices 63 to 76
    return chr(sorted(ascii_values)[14]) # return the character with the 14th smallest ASCII value
