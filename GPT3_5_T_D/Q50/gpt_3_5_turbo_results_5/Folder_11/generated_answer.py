
def if_contains_anagrams(strings):
    def are_anagrams(a, b):
        if len(a) < 3 or len(b) < 3:
            return False
        return sorted(a.lower()) == sorted(b.lower())

    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if are_anagrams(strings[i], strings[j]):
                count += 1
                if count >= 28:
                    return True
    return False
