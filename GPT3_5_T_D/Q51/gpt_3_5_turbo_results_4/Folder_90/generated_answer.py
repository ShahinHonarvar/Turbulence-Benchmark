
import itertools

def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)-1):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if set(strings[i].lower()) == set(strings[j].lower()):
                    count += 1
            if count > 147:
                return False
    return True
