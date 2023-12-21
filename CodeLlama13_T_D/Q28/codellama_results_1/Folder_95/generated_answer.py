
def return_nth_smallest_ascii(s):
    asciis = []
    for i in range(1, 47):
        if s[i].isalpha():
            asciis.append(ord(s[i]))
    
    sorted(asciis)
    return chr(asciis[12])
