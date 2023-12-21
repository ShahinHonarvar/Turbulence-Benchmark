
def return_nth_smallest_ascii(s):
    chars = set()
    for i in range(63, 77):
        if s[i].isalpha():
            chars.add(ord(s[i]))
    smallest = sorted(chars)[14]
    return chr(smallest)
