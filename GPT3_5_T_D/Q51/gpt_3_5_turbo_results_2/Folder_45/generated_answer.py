
def if_contains_anagrams(strings):
    def count_anagrams(string):
        count = 0
        for i in range(len(strings)):
            if sorted(strings[i].lower()) == sorted(string.lower()):
                count += 1
        return count

    pairs = 0
    for i in range(len(strings)):
        if len(strings[i]) >= 3:
            pairs += count_anagrams(strings[i])

    return pairs <= 464
