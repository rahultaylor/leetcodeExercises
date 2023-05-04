def twoSum(nums: list, target: int) -> list:
    gotSolution = False
    outList = []
    startIndex = 0

    while startIndex < len(nums) and not gotSolution:
        nextIndex = startIndex + 1
        while nextIndex < len(nums) and not gotSolution:
            if nums[startIndex] + nums[nextIndex] == target:
                gotSolution = True
                outList.append(startIndex)
                outList.append(nextIndex)
            nextIndex+=1
        startIndex+=1
    
    return outList

inputList = [1,2,3,4,5,5]
target = 4
print(twoSum(nums=inputList, target= target))
