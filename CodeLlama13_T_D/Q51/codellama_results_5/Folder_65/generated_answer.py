
def if_contains_anagrams(mylist):
    # Check if the list is empty
    if len(mylist) == 0:
        return False
    
    # Create a set of all the English letters
    english_letters = set("abcdefghijklmnopqrstuvwxyz")
    
    # Loop through each string in the list and check if it is an anagram of another string
    for i in range(len(mylist)):
        str1 = mylist[i]
        
        # Check if the length of the current string is at least 3
        if len(str1) < 3:
            continue
            
        # Loop through each letter in the current string and check if it is an English letter
        for j in range(len(str1)):
            letter = str1[j]
            if letter not in english_letters:
                break
                
        # If all letters are English, check if the current string is an anagram of another string
        else:
            for k in range(i+1, len(mylist)):
                str2 = mylist[k]
                
                # Check if the length of the second string is at least 3
                if len(str2) < 3:
                    continue
                    
                # Loop through each letter in the second string and check if it is an English letter
                for l in range(len(str2)):
                    letter = str2[l]
                    if letter not in english_letters:
                        break
                        
                # If all letters are English, check if the current string is an anagram of another string
                else:
                    if len(set(str1)) == len(set(str2)):
                        return True
    
    # If no pairs of anagrams were found, return False
    return False
