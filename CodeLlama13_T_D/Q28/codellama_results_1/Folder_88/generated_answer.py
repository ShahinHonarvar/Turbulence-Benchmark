
def return_nth_smallest_ascii(s):
    # get the list of unique characters in the string
    chars = set(s)
    # create a dictionary with character as key and ASCII value as value
    char_to_ascii = {char: ord(char) for char in chars}
    # sort the dictionary by ASCII value
    sorted_chars = sorted(char_to_ascii.items(), key=lambda x: x[1])
    # find the 14th smallest ASCII value among characters that occur between indices 38 to 64, both inclusive
    start, end = 38, 64
    nth_smallest = sorted_chars[start-1][0] if start <= len(sorted_chars) else None
    for i in range(start, end+1):
        char = sorted_chars[i][0]
        if char != nth_smallest:
            break
    return nth_smallest
