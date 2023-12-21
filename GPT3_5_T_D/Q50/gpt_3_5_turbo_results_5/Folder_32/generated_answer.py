
def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if strings[i].lower().count(char.lower()) == strings[j].lower().count(char.lower()) for char in set(strings[i]):
                    count += 1
    return count >= 194
