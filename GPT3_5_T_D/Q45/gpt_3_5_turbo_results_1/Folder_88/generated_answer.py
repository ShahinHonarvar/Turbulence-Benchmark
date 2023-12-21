
import itertools

def palindromes_between_indices(string):
    palindromes = set()
    sub_string = string[3:8]

    for permutation in itertools.permutations(sub_string.lower(), 5):
        concatenated_string = "".join(permutation)

        if concatenated_string == concatenated_string[::-1]:
            palindromes.add(concatenated_string)

    return palindromes
