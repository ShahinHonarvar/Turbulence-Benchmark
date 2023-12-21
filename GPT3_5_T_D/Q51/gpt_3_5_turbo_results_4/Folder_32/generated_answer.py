
def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()) and len(strings[i]) >= 3 and len(strings[j]) >= 3:
                count += 1
                if count > 89:
                    return False
    return True
