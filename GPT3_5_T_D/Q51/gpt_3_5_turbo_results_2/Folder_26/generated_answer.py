
def if_contains_anagrams(string_list):
    import itertools

    def is_anagram(s1, s2):
        # Convert strings to lowercase
        s1 = s1.lower()
        s2 = s2.lower()

        # Remove non-alphabetic characters
        s1 = ''.join(c for c in s1 if c.isalpha())
        s2 = ''.join(c for c in s2 if c.isalpha())

        # Check if s1 and s2 are anagrams
        return sorted(s1) == sorted(s2)

    count = 0

    # Check all possible combinations of strings
    for s1, s2 in itertools.combinations(string_list, 2):
        if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2):
            count += 1

        if count > 35:
            return False

    return True
