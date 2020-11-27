class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums2.extend(nums1)
        nums2.sort()
        mid = len(nums2)//2
        if len(nums2) == 0:
            return(float(0))
        if len(nums2) == 1:
            return(float(nums2[0]))
        if len(nums2)%2 == 0:
            return(float((nums2[mid-1]+nums2[mid])/2))
        else:
            return(float(nums2[mid]))