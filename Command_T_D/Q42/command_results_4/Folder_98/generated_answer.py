def prime_factors(nums):
    fac = set()
    for x in range(2,int(nums[4])+1):
        if nums[4]%x == 0:
            for i in range(x,int(nums[4])+1,x):
                if nums[4]%i == 0:
                    fac.add(i)
                    break
            else:
                fac.add(x)
                break
    return fac
