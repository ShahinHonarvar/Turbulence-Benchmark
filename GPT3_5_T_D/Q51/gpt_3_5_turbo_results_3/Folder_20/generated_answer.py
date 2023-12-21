
def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                sorted_i = sorted(strings[i].lower())
                sorted_j = sorted(strings[j].lower())
                if sorted_i == sorted_j:
                    count += 1
                    if count > 131:
                        return False
    return True
