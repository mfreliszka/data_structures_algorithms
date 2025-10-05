# [PROBLEM STATEMENT]
# Top K Frequent Elements
#
# Given an integer array nums and an integer k, return the k most frequent elements.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.
#
# Example 1:
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]
#
# Example 2:
# Input: nums = [7,7], k = 1
# Output: [7]

# [Brute Force - Sorting]
# Time complexity: O(n log n) - We iterate through nums once to build frequency map O(n),
#                               then sort all unique elements by their frequency O(n log n),
#                               where n is the number of unique elements (worst case = array length).
#                               The sorting dominates, so total is O(n log n).
# Space complexity: O(n) - We use a hash map to store frequencies of all unique elements,
#                         and potentially a list to sort them. Both are O(n) in worst case.
# Explanation: Count frequency of each number using a hash map, then sort all elements 
#              by their frequency in descending order, and return the first k elements.
# Why this complexity: Sorting the frequency map is the bottleneck, requiring O(n log n) time.
class BruteForceSolution:
    def topKFrequent(self, nums, k):
        # Count frequencies
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # Sort by frequency (descending)
        sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        
        # Return top k elements
        return [num for num, freq in sorted_items[:k]]


# [Optimized - Min Heap]
# Time complexity: O(n log k) - Building frequency map takes O(n).
#                               For each of the n unique elements, we either:
#                               - Add to heap: O(log k) if heap size < k
#                               - Compare and potentially replace: O(log k) if heap is full
#                               Total: O(n) + O(n log k) = O(n log k)
# Space complexity: O(n + k) - O(n) for frequency map, O(k) for the heap.
#                             Simplifies to O(n) since k ≤ n.
# Explanation: After building the frequency map, we maintain a min heap of size k. 
#              We iterate through all elements and keep only the k elements with highest frequencies.
# Why this complexity: Using a heap of size k instead of sorting all n elements reduces 
#                     the sorting factor from O(n log n) to O(n log k).
import heapq

class HeapSolution:
    def topKFrequent(self, nums, k):
        # Count frequencies
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # Use min heap to keep track of top k frequent elements
        # Heap stores tuples of (frequency, number)
        min_heap = []
        
        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)  # Remove least frequent
        
        # Extract numbers from heap
        return [num for freq, num in min_heap]


# [Optimal - Bucket Sort]
# Time complexity: O(n) - Building frequency map: O(n)
#                        Creating and filling buckets: O(n) - we visit each unique element once
#                        Extracting k elements from buckets: O(n) - worst case we scan all buckets
#                        Total: O(n) + O(n) + O(n) = O(n)
# Space complexity: O(n) - Frequency map: O(n)
#                         Bucket array of size n+1: O(n)
#                         Total: O(n)
# Explanation: Use bucket sort where bucket[i] contains all numbers with frequency i.
#              Since max frequency is n (array length), we iterate from highest bucket backwards
#              and collect k elements.
# Why this complexity: By using frequency as array index (bucket sort), we avoid sorting
#                     and achieve linear time.
# THE TRICK: Frequencies are bounded by array length n (a number can appear at most n times).
#            This allows us to use bucket sort with buckets indexed by frequency.
#            We create n+1 buckets (indices 0 to n), where bucket[i] holds all numbers 
#            that appear exactly i times. Then iterate from highest frequency down,
#            collecting elements until we have k elements - all in O(n) time!
class Solution:
    def topKFrequent(self, nums, k):
        # Count frequencies
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # Create buckets: bucket[i] contains all numbers with frequency i
        # Max frequency possible is len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        # Collect top k frequent elements from highest frequency buckets
        result = []
        for i in range(len(buckets) - 1, 0, -1):  # Start from highest frequency
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result


# Test Cases
# Test Case 1
nums1 = [1, 2, 2, 3, 3, 3]
k1 = 2
# Output: [2, 3] (or [3, 2] - order doesn't matter)
# Explanation: Element 3 appears 3 times, element 2 appears 2 times,
#              element 1 appears 1 time. Top 2 frequent are 3 and 2.

# Test Case 2
nums2 = [7, 7]
k2 = 1
# Output: [7]
# Explanation: Only one unique element exists, and it appears 2 times.

# Test Case 3
nums3 = [1]
k3 = 1
# Output: [1]
# Explanation: Edge case with single element array.

# Test Case 4
nums4 = [4, 1, -1, 2, -1, 2, 3]
k4 = 2
# Output: [-1, 2] (or [2, -1])
# Explanation: Both -1 and 2 appear 2 times (tied for most frequent),
#              while 1, 3, and 4 appear once. We return any 2 of the most frequent.


# Summary of Approaches
# | Approach           | Time       | Space    | Pros                              | Cons                           |
# |--------------------|------------|----------|-----------------------------------|--------------------------------|
# | Brute Force        | O(n log n) | O(n)     | Simple to implement               | Slower due to sorting          |
# | Min Heap           | O(n log k) | O(n)     | Better than sorting when k << n   | More complex than bucket sort  |
# | Bucket Sort        | O(n)       | O(n)     | Optimal linear time, elegant      | Requires bounded frequency     |
#
# Winner: Bucket Sort (Solution) - Achieves optimal O(n) time complexity by exploiting the fact
#         that frequencies are naturally bounded by array length. This eliminates the need for
#         sorting or heap operations entirely. It's the most efficient solution for this problem.