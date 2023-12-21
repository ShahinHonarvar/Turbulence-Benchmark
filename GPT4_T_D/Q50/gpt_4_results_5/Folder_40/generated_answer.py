
def if_contains_anagrams(strings_list):
    anagrams = {}
    for string in strings_list:
        if len(string) >= 3:
            sorted_str = "".join(sorted(string.lower()))
            if sorted_str in anagrams:
                anagrams[sorted_str] += 1
            else:
                anagrams[sorted_str] = 1
    count = sum(1 for value in anagrams.values() if value >= 2)
    if count >= 3:
        return True
    return False
