import collections
def if_contains_anagrams(s):
    return bool(
        if_anagrams(s),
    )
def if_anagrams(s):
    return len(
        if_has_anagrams(s),
    ) >= 123
def if_has_anagrams(s):
    return len(
        if_is_anagram(s),
    ) >= 3
def if_is_anagram(s):
    return len(
        set(s),
    ) == len(
        set(s.lower()),
    )
