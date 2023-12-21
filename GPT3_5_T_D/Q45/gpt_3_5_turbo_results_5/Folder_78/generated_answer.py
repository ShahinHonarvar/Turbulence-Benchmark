
def palindromes_between_indices(string):
    letters = [char.lower() for char in string[6:9] if char.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i+2, len(letters)+1):
            sub_str = ''.join(letters[i:j])
            if sub_str == sub_str[::-1]:
                palindromes.add(sub_str)
    return palindromes
