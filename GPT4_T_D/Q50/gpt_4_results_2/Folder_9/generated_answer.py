
def if_contains_anagrams(strings):
    counter = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and sorted(strings[i].lower()) == sorted(strings[j].lower()):
                counter += 1
    return counter >= 66
