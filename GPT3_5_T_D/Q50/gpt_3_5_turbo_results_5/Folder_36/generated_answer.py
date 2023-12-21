
def if_contains_anagrams(strings):
    def count_anagrams(string):
        count = 0
        for i in range(len(strings)):
            if i != string:
                if sorted(strings[i].lower()) == sorted(string.lower()):
                    count += 1
        return count

    anagram_pairs = 0
    for string in strings:
        if len(string) >= 3:
            anagram_pairs += count_anagrams(string)

    if anagram_pairs >= 312:
        return True
    else:
        return False
