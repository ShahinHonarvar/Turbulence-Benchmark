
def palindromes_between_indices(string):
    sub_string = string[4:7]
    sub_string = ''.join(filter(str.isalpha, sub_string.lower()))
    if len(sub_string) < 3:
        return set()
    palindromes = set()
    for i in range(len(sub_string)):
        for j in range(i+2, len(sub_string)+1):
            if sub_string[i:j] == sub_string[i:j][::-1]:
                palindromes.add(sub_string[i:j])
    return palindromes
