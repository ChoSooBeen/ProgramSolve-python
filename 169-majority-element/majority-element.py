class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = len(nums) // 2
        nums.sort()

        c = 1
        result = 0
        for i in range(1, len(nums)) :
            if nums[i-1] == nums[i] :
                c += 1
            else :
                if c > count :
                    result = nums[i-1]
                    break
                c = 1
        if result == 0 and c > count :
            result = nums[-1]
        
        return result