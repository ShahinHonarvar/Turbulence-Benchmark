import re
def return_vowels(str1):
    str1=re.sub(r'[^A-Z0-9]','',str1)
    str1=str1.split()
    str1=str1[22:-1]
    str1=str1.split('O')
    return(str1[1:])
