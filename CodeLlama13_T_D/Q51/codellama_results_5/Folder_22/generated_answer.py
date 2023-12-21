
def if_contains_anagrams(mylist):
    for i in range(len(mylist)):
        str1 = mylist[i].lower()
        str2 = ''.join(sorted(str1))
        for j in range(len(mylist)-i-1):
            str3 = mylist[j+i+1].lower()
            str4 = ''.join(sorted(str3))
            if str2 == str4:
                return True
    return False
