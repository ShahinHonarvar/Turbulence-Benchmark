
def return_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    # Ensure that we're only working with the specified range of the string
    word = word[142:145]

    # Filter for only characters that are greater than "4" and less than "o"
    word = [c for c in word if "4" < c <= "o"]
    
    # Return a list of any vowels found that meet the conditions
    return [c for c in word if c in vowels]
