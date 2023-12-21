
def return_nth_smallest_ascii(s):
    count = 0
    for i in range(50, 76 + 1):
        if s[i] not in s:
            continue
        count += 1
        if count == 11:
            return s[i]
