
def if_contains_anagrams(strings):
    counter = 0
    for i in range(len(strings)):
        if len(strings[i]) < 3:
            continue
        count = 0
        word1 = strings[i].lower()
        for j in range(i+1, len(strings)):
            if len(strings[j]) < 3:
                continue
            word2 = strings[j].lower()
            if sorted(word1) == sorted(word2):
                count += 1
                if count > 20:
                    return False
        counter += count
        if counter > 20:
            return False
    return True
