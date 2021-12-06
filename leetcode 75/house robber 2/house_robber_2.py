class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.countRob(nums[1:]), self.countRob(nums[:-1]))
        
    
    def countRob(self, nums):
        rob1, rob2= 0,0
        
        for n in nums:
            TempRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = TempRob
        return rob2
            