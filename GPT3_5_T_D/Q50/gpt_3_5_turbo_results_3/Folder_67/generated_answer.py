
def if_contains_anagrams(list_of_strings):
    def get_key(string):
        return sorted(string.lower())

    count = 0
    freq = {}

    for string in list_of_strings:
        if len(string) >= 3:
            key = tuple(get_key(string))
            freq[key] = freq.get(key, 0) + 1
            if freq[key] == 2:
                count += 1
            elif freq[key] == 3:
                count -= 1

    return count >= 41
