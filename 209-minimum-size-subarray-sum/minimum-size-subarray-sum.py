class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = nums[0]
        length = 1
        start = 0
        idx = 1
        answer = len(nums) + 1

        while start < len(nums) and idx < len(nums) :
            if sum < target :
                sum += nums[idx]
                length += 1
                idx += 1
            else :
                answer = min(answer, length)
                sum -= nums[start]
                start += 1
                length -= 1
        
        while start < len(nums) :
            if sum >= target :
                answer = min(answer, length) 
            sum -= nums[start]
            start += 1
            length -= 1

        if answer > len(nums) :
            return 0
        return answer