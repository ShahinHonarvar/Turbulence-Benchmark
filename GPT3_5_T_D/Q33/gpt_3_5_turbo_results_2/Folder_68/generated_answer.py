
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_greater_than_question = [vowel for vowel in vowels if ord(vowel) > ord('?')]
    vowels_in_range = [vowel for vowel in vowels_greater_than_question if ord(vowel) <= ord('k')]
    return list(string[1:9]).intersection(vowels_in_range) if vowels_in_range else []
