
def palindromes_between_indices(string):
    english_letters = [char.lower() for char in string if char.isalpha()]
    filtered_letters = english_letters[8:10]
    if filtered_letters != []:
        palindromes = set()
        for i in range(len(filtered_letters)):
            for j in range(i+3, len(filtered_letters)+1):
                substring = filtered_letters[i:j]
                if substring == substring[::-1]:
                    palindromes.add("".join(substring))
        return palindromes
    else:
        return set()
