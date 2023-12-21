
def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and strings[i].lower() == strings[j].lower():
                count += 1
                if count >= 177:
                    return True
    return False
