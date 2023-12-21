
def if_contains_anagrams(strings):
    return len([i for i in range(len(strings)) if set(sorted(strings[i])) in strings]) <= 255
