 
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = []
  
    for i in range(29, 73):
        if string[i] in vowels and '#' < string[i] <= '.':
            vowel_list.append(string[i])
   
    return vowel_list
