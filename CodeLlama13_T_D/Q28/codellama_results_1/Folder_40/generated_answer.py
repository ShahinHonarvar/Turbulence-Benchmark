
def return_nth_smallest_ascii(string):
    asciis = []
    for i in range(len(string)):
        if string[i] not in asciis:
            asciis.append(ord(string[i]))
    sorted_asciis = sorted(asciis)
    return chr(sorted_asciis[4])
