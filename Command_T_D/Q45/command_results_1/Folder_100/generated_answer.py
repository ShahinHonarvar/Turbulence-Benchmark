import re
def palindromes_between_indices(strng):
    i=0
    j=5
    while i<=j:
        tmp_strng=strng[i:j+1]
        if len(tmp_strng)<=5:
            return set(re.findall(r'[a-z]+', tmp_strng.lower()))
        i+=1
        j-=1
