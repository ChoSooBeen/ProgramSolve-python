class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        while idx < len(nums) :
            if nums[idx] == val :
                nums.remove(val)
            else :
                idx += 1
        return len(nums)