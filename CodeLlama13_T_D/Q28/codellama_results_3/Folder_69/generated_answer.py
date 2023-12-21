
def return_nth_smallest_ascii(string):
    characters = []
    for i in range(67, 78):
        if string[i].isalpha():
            characters.append(ord(string[i]))
    return chr(sorted(characters)[6])
