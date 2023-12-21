import re
def if_contains_anagrams(test_list):
    test_list=list(test_list)
    test_list.sort()
    flag = True
    for i in range(len(test_list)-1):
        for j in range(i+1,len(test_list)):
            if test_list[i] == test_list[j]:
                continue
            elif re.match(r'(?i)(.*?[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[sS])(?=.*[dD])(?=.*[fF])(?=.*[gG])(?=.*[hH])(?=.*[jJ])(?=.*[kK])(?=.*[lL])(?=.*[mM])(?=.*[nN])(?=.*[pP])(?=.*[qQ])(?=.*[rR])(?=.*[tT])(?=.*[vV])(?=.*[wW])(?=.*[zZ])', test_list[i]):
                flag = False
                break
    if flag:
        return True
    else:
        return False
