
def return_nth_smallest_ascii(s):
    return next((char for char in s[5:-5] if ord(char) in range(ord(s[0])+5, ord(s[1])+10)), s[0])
