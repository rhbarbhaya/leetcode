class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        grand = sum(nums)
        leftsum = 0
        for idx, val in enumerate(nums):
            if leftsum == (grand - leftsum - val):
                return(idx)
            leftsum += val
        return(-1)