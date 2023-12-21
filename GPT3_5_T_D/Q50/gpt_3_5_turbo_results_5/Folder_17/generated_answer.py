
def if_contains_anagrams(strings):
    anagrams_count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()) and len(strings[i]) >= 3:
                anagrams_count += 1
                if anagrams_count >= 97:
                    return True
    return False
