
def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for string in list_of_strings:
        if len(string) < 3:
            continue
        string = string.lower()
        sorted_string = "".join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    count = 0
    for value in anagrams.values():
        count += len(value) * (len(value) - 1) // 2
    if count >= 155:
        return True
    return False
