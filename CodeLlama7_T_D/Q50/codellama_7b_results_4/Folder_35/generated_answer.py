
def if_contains_anagrams(strings):
    anagram_pairs = set()
    for string in strings:
        sorted_string = "".join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue

        for other_string in strings:
            if other_string == string:
                continue

            if sorted_string == "".join(sorted(other_string.lower()))):
                anagram_pairs.add((string, other_string))
    return len(anagram_pairs) >= 153
