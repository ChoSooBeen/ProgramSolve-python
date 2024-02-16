class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i in range(len(citations)) :
            if h < citations[i] :
                h += 1
            else :
                break
        return h