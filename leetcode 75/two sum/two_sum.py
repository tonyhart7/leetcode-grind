class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #val : index
        
        for i, n in enumerate(nums):
            diff = target - n # check difference in target and current number
            if diff in prevMap: # if difference is in prevMap
                return [prevMap[diff], i] # return index of prevMap and current index
            prevMap[n] = i # otherwise, add current number to prevMap
        return
    
