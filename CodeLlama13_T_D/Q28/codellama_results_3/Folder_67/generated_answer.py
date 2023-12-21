
def return_nth_smallest_ascii(s):
    count = 0
    for i in range(60, 84):
        if s[i] == 'a':
            count += 1
    return chr(97 + count)
