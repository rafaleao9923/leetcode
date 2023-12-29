from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Assumption both nums1 and nums2 cannot be empty
        n = len(nums1)
        m = len(nums2)
        if (n > m):
            return self.findMedianSortedArrays(nums2, nums1)  # Swapping to make nums1 smaller
 
        start = 0
        end = n
        realmidinmergedarray = (n + m + 1) // 2
 
        while (start <= end):
            mid = (start + end) // 2
            leftAsize = mid
            leftBsize = realmidinmergedarray - mid
 
            # checking overflow of indices
            leftA = nums1[leftAsize - 1] if (leftAsize > 0) else float('-inf')
            leftB = nums2[leftBsize - 1] if (leftBsize > 0) else float('-inf')
            rightA = nums1[leftAsize] if (leftAsize < n) else float('inf')
            rightB = nums2[leftBsize] if (leftBsize < m) else float('inf')
 
            # if correct partition is done
            if leftA <= rightB and leftB <= rightA:
                if ((m + n) % 2 == 0):
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
                return max(leftA, leftB)
            elif (leftA > rightB):
                end = mid - 1
            else:
                start = mid + 1

if __name__ == "__main__":
    ans = Solution()
    arr1 = [-5, 3, 6, 12, 15]
    arr2 = [-12, -10, -6, -3, 4, 10]
    print("Median of the two arrays is")
    print(ans.findMedianSortedArrays(arr1, arr2))