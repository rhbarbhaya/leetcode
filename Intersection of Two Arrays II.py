class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sol = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                sol.append(nums1[i])
                nums2.pop(nums2.index(nums1[i]))
        return(sol)

# Given two arrays, write a function to compute their intersection.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]