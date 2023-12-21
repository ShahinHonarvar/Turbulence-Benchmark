
def if_contains_anagrams(strings):
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(set(strings[i]).intersection(strings[j])) >= 3:
                return True
    return False
