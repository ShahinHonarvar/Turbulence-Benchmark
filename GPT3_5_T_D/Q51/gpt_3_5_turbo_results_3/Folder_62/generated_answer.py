
def if_contains_anagrams(strings):
    def count_anagrams(string):
        count = 0
        for i in range(len(strings)):
            if sorted(string.lower()) == sorted(strings[i].lower()) and string.lower() != strings[i].lower():
                count += 1
        return count
    
    pair_count = 0
    for string in strings:
        if len(string) >= 3:
            pair_count += count_anagrams(string)
    
    return pair_count <= 289
