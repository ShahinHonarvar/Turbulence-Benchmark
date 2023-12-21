
def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        for i in range(len(string) - 2):
            substring = string[i:i+3]
            if substring not in anagrams:
                anagrams.append(substring)
    return len(anagrams) >= 20
