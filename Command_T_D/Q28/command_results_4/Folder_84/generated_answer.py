
def return_nth_smallest_ascii(s):
    ascii_dict = {}
    for i in range(len(s)):
        ascii_dict[s[i]] = ord(s[i])
    ascii_list = sorted(ascii_dict.values())
    seventh_smallest = ascii_list[6]
    return chr(seventh_smallest)
