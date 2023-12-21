
def if_contains_anagrams(list_of_strings):
    count = 0
    for i in range(len(list_of_strings) - 1):
        for j in range(i + 1, len(list_of_strings))):
            if sorted(list_of_strings[i].lower()) == sorted(list_of_strings[j].lower()):
                count += 1
                if count >= 88:
                    return True
    return False
