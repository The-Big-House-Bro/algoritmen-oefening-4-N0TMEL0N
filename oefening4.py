def countTargetPairs(lijst, getal):
    n = len(lijst)
    aantal = 0  
    for i in range(n):
        for j in range(i + 1, n):
            if lijst[i] + lijst[j] < getal:
                aantal += 1
    return aantal

nums = [-6,2,5,-2,-7,-1,3]
target = -2
print(countTargetPairs(nums, target))  
