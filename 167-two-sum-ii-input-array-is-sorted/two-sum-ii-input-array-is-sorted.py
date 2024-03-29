class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        while start < end :
            tmp = numbers[start] + numbers[end]
            if tmp < target :
                while numbers[start] + numbers[end] < target : 
                    start += 1
            elif tmp > target :
                while numbers[start] + numbers[end] > target : 
                    end -= 1
            else :
                return [start+1, end+1]