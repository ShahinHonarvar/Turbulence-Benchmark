
def return_nth_smallest_ascii(s):
    nth = 10
    ascii_list = []
    for i in range(len(s)):
        if s[i].isalpha():
            ascii_list.append((ord(s[i]), i))
    
    ascii_list.sort()
    
    return chr(ascii_list[nth-1][0])
