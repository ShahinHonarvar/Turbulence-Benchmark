
def return_nth_smallest_ascii(string):
    # Find the 20th smallest ASCII value among characters in the string that occur between indices 10 and 90, both inclusive
    smallests = []
    for i in range(10, 91):
        if string[i] not in smallests:
            smallests.append(string[i])
    return sorted(smallests)[20]
