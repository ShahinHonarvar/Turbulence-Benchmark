
def if_contains_anagrams(strings):
    def get_sorted_letters(string):
        return ''.join(sorted(string.lower()))

    pairs = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if get_sorted_letters(strings[i]) == get_sorted_letters(strings[j]):
                    pairs += 1
                    if pairs > 407:
                        return False
    return True
