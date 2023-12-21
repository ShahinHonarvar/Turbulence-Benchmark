
def palindromes_between_indices(s):
    import itertools
    import string
    
    # Get the substring between index 6 and index 9
    substring = s[6:10]
    
    # Filter out non-English letters from the substring
    english_letters = set(string.ascii_letters)
    filtered_substring = ''.join(filter(lambda x: x in english_letters, substring))
    
    # Get all possible arrangements of the English letters
    arrangements = set(''.join(perm) for perm in itertools.permutations(filtered_substring))
    
    # Find palindromes of length at least 3
    palindromes = set()
    for word in arrangements:
        if len(word) >= 3 and word.lower() == word.lower()[::-1]:
            palindromes.add(word)
    
    return palindromes
