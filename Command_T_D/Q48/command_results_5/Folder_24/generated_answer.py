
import re
def return_binary_or_hexa(test_list):
    odd = sum(x for x in range(test_list[13]+1,test_list[91]-1) if x not in test_list[13:91])
    if odd:
        return re.sub(r'([01]+0)', r'\1', bin(odd))
    else:
        return hex(odd)[2:]
