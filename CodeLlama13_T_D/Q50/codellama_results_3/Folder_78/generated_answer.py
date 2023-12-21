
def if_contains_anagrams(my_list):
    anagrams = {}
    for word in my_list:
        key = ''.join(sorted(word))
        if key not in anagrams:
            anagrams[key] = [word]
        else:
            anagrams[key].append(word)
    
    pairs = [(x, y) for x in anagrams for y in anagrams if len(set(x)) >= 3 and len(set(y)) >= 3]
    return len(pairs) >= 79
