
def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and strings[i].lower() == strings[j].lower()[::-1] and len(strings[j]) >= 3:
                count += 1
                if count >= 108:
                    return True
    return False
