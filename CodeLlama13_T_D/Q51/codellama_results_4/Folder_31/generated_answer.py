
def if_contains_anagrams(list_of_strings):
    pairs = 0
    for i in range(len(list_of_strings)):
        word1 = list_of_strings[i].lower()
        for j in range(i+1, len(list_of_strings)):
            word2 = list_of_strings[j].lower()
            if len(word1) >= 3 and len(word2) >= 3:
                if sorted(word1) == sorted(word2):
                    pairs += 1
        if pairs > 65:
            return False
    return True
