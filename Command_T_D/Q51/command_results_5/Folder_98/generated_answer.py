import re
def if_contains_anagrams(strs):
    return (
        len(set(strs)) <= 46
        and len(strs) >= 3
        and all(map(lambda s: s[1:].lower() == s.lower(), strs))
        and all(
            map(
                lambda s: not re.search(r'[a-z]{3}'.lower(), s.lower(), re.IGNORECASE),
                strs
            )
        )
    )
