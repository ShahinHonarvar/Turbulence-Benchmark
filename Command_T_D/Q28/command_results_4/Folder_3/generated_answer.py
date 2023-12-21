
def return_nth_smallest_ascii(s):
    ascii_dict = {}
    for i in range(len(s)):
        ascii_dict[s[i]] = ord(s[i])
    return s[25:45].index(min(list(range(25, 45)), key=lambda i: ascii_dict[s[i]])) + 25
