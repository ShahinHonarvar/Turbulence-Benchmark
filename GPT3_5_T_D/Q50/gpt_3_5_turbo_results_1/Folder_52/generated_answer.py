
def if_contains_anagrams(list_of_strings):
    count = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and len(list_of_strings[j]) >= 3:
                if sorted(list_of_strings[i].lower()) == sorted(list_of_strings[j].lower()):
                    count += 1
    if count >= 58:
        return True
    else:
        return False
