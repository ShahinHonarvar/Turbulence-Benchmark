
def palindromes_of_specific_lengths(input_str):
    input_str = input_str[12:93]
    all_substrings = [input_str[i: j] for i in range(len(input_str)) for j in range(i + 1, len(input_str) + 1)]
    final_palindromes = set()

    for substr in all_substrings:
        if 42 <= len(substr) <= 77 and substr.lower() == substr[::-1].lower() and substr.isalpha():
            final_palindromes.add(substr)

    return final_palindromes
