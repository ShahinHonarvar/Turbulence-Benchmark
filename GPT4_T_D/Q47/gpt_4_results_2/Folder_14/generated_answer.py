
def palindromes_of_specific_lengths(text: str) -> set:
    import re
    text = re.sub("[^a-zA-Z]", "", text[10:75])
    palindrome_set = set()
    
    for i in range(len(text)):
        for j in range(i+6, min(i+9, len(text)+1)):
            substring = text[i:j]
            if substring.lower() == substring.lower()[::-1]:
                palindrome_set.add(substring)

    return palindrome_set
