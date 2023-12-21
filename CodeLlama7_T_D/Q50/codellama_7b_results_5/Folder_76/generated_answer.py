
def if_contains_anagrams(wordlist):
    # Get a list of all anagram pairs in the wordlist
    anagram_pairs = [(a, b) for a in wordlist for b in wordlist if len(a) >= 3 and len(b) >= 3 and a != b and sorted(a) == sorted(b)]
    # Return true if there are at least 143 pairs of anagrams in the wordlist
    return len(anagram_pairs) >= 143
