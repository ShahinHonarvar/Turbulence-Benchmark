
def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    eligible_vowels = []
    s_71_81 = s[71:81]
    for letter in s_71_81:
        if letter > '>' and letter <= 'U' and letter in vowels:
            eligible_vowels.append(letter)
    return eligible_vowels
