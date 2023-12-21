
def if_contains_anagrams(lst):
    counter = 0
    seen = {}
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        key = ''.join(sorted(word))
        if key in seen:
            counter += 1
        seen[key] = word
    return counter >= 61
