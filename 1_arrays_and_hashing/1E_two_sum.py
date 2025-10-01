# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.

# Brute Force
# Time complexity: O(n^2) - Two nested loops iterate through all possible pairs.
#                  The outer loop runs n times, and for each iteration, the inner loop
#                  runs (n-1), (n-2), ..., 1 times respectively, totaling n(n-1)/2 comparisons.
# Space complexity: O(1) - Only uses a constant amount of extra space for loop variables.
# Why this complexity: We check every possible pair (i, j) where i < j by brute force.
class BruteForceSolution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# Sorting
# Time complexity: O(n log n) - Dominated by the sorting operation.
#                  Building array A is O(n), sorting is O(n log n), two-pointer scan is O(n).
#                  Overall: O(n) + O(n log n) + O(n) = O(n log n)
# Space complexity: O(n) - We create a new array A to store [value, index] pairs for all elements.
# Why this complexity: After sorting by value, we use two pointers (one at start, one at end)
#                      to find the pair. If sum is too small, move left pointer right; if too large,
#                      move right pointer left. This avoids checking all pairs but requires sorting first.
class SortingSolution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []


# HashMap (Optimal Solution)
# Time complexity: O(n) - Single pass through the array with O(1) hash map lookups.
# Space complexity: O(n) - In the worst case, we store all n elements in the hash map.
# Why this complexity: We iterate through the array once, and for each element, we perform
#                      constant-time operations (hash map lookup and insertion).
# THE TRICK: Instead of looking for pairs, we look for COMPLEMENTS.
#            For each number, we check if its complement (target - current_number) has already
#            been seen. We build the hash map as we go, so by the time we find the second number
#            of the pair, the first number is already in the map. This eliminates the need for
#            nested loops or sorting - we solve it in a single pass with O(1) lookups!
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


# Tests:
nums1 = [3,4,5,6]
target1 = 7
nums2 = [4,5,6]
target2 = 10