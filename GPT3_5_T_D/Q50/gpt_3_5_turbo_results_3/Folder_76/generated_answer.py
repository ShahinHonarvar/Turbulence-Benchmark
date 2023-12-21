
def if_contains_anagrams(strings):
    def get_key(s):
        return tuple(sorted(s.lower()))

    count = {}
    for s in strings:
        if len(s) >= 3:
            key = get_key(s)
            count[key] = count.get(key, 0) + 1

    anagram_pairs = sum(n * (n - 1) // 2 for n in count.values())
    return anagram_pairs >= 143
