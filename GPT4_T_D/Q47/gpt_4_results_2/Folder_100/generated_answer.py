
def palindromes_of_specific_lengths(text):
    import re
    palindromes = set()
    text = text[29:97].lower()
    text = re.sub('[^a-z]', '', text)
    for i in range(len(text)):
        for j in range(i+12, min(i+19, len(text)+1)):
            sub_text = text[i:j]
            if sub_text == sub_text[::-1]:
                palindromes.add(sub_text)
    return palindromes
