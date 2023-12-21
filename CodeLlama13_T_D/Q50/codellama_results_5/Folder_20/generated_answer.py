
def if_contains_anagrams(strings):
    pairs = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(set(strings[i]).intersection(set(strings[j]))) == len(set(strings[i])):
                pairs += 1
                if pairs >= 64:
                    return True
    return False
