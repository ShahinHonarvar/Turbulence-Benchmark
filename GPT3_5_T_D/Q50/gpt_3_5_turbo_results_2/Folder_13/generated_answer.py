
def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:   # Consider only anagrams of length at least three
                if sorted(strings[i].lower()) == sorted(strings[j].lower()):   # Compare strings in a case-insensitive manner
                    count += 1
                    if count >= 144:
                        return True
    return False
