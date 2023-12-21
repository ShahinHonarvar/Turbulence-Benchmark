def find_primes_between_indices(lst):
    return sorted(list(filter(lambda x: x%2==0 and x%3==0 and x%5==0 and x%7==0 and x%11==0 and x%13==0 and x%17==0 and x%19==0 and x%23==0 and x%29==0 and x%31==0 and x%37==0 and x%41==0 and x%43==0 and x%47==0 and x%53==0 and x%59==0 and x%61==0 and x%67==0 and x%71==0, lst[25:72])))
