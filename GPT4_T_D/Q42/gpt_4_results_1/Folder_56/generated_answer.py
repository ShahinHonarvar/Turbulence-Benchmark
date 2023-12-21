
from typing import List
def prime_factors(nums: List[int]) -> set:
    number = nums[60]
    prime_factors = set()
    i=2
    while(i*i<=number):
        if(number%i):
            i+=1
        else:
            number//=i
            prime_factors.add(i)
    if(number>1):
        prime_factors.add(number)
    return prime_factors
