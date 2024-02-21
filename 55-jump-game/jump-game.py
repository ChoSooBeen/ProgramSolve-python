class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = 0
        
        for i in range(len(nums)) :
            cur = max(i + nums[i], cur)

            if cur >= len(nums)-1 :
                return True
            
            if cur <= i :
                return False
        
        # return True