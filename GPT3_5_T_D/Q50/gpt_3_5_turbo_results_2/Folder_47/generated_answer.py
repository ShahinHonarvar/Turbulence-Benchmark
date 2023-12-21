
def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) == len(strings[j]) >= 3:
                if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                    count += 1
    return count >= 47
