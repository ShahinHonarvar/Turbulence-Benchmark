
def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)-1):
        for j in range(i+1, len(strings)):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                count += 1
            if count > 3:
                return False
    return True
