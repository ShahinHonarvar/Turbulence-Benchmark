
def palindromes_between_indices(string):
    indices = range(6, 10)
    letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in indices:
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                sub_string = string[i:j+1]
                if sub_string[::-1] == sub_string and len(sub_string) >= 3:
                    palindromes.add(sub_string)
    return palindromes
