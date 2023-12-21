
def return_nth_smallest_ascii(string):
    asciis = []
    for i in range(51, 61):
        if string[i] not in asciis:
            asciis.append(string[i])
    return chr(sorted(asciis)[4])
