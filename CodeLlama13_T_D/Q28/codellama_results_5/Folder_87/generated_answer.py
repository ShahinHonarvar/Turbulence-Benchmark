
def return_nth_smallest_ascii(s):
    # find the 5th smallest ASCII value among characters in s[29:34]
    ascii_values = []
    for i in range(29, 34):
        if s[i].isalpha():
            ascii_values.append(ord(s[i]))
    
    # sort the list and return the 5th element (index starts from 0)
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[4])
