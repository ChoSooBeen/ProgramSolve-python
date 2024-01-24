class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums :
            return []
        result = []
        start = nums[0]
        end = nums[0]
        idx = 1
        while idx < len(nums) :
            if nums[idx-1] + 1 != nums[idx] :
                if start == end :
                    result.append(str(start))
                else :
                    result.append(str(start)+"->"+str(end))
                start = nums[idx]
                end = nums[idx]
            end = nums[idx]
            idx += 1
        if start == end :
            result.append(str(start))
        else :
            result.append(str(start)+"->"+str(end))
        return result 