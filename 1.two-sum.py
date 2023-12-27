from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


class SolutionTwo:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, item in enumerate(nums):
            hashmap[item] = i
        for i, item in enumerate(nums):
            complement = target - item
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]


class SolutionThree:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, item in enumerate(nums):
            complement = target - item
            # print(complement, hashmap)
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[item] = i
            # print(hashmap)
            # print("------")


if __name__ == "__main__":
    # solution = Solution()
    # print(solution.twoSum([2, 7, 11, 15], 9))

    # solutiontwo = SolutionTwo()
    # print(solutiontwo.twoSum([2, 7, 11, 15], 9))

    solutionthree = SolutionThree()
    # solutionthree.twoSum([3, 4, 1, 2, 7, 11, 15], 9)
    print(solutionthree.twoSum([3, 4, 1, 2, 7, 11, 15], 9))