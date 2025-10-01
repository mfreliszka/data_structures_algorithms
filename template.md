# DSA Problem Solution Template

When providing solutions to data structure and algorithm problems, follow this format:

## Response Structure

For each solution provided (whether brute force, optimized, or optimal), add detailed comments ABOVE the solution explaining:

1. **Time Complexity**: State the Big O notation
2. **Space Complexity**: State the Big O notation
3. **Detailed Explanation**: Explain WHY the complexity is what it is
   - Break down what operations contribute to the time complexity
   - Explain what data structures contribute to space complexity
   - Show the mathematical reasoning (e.g., "n iterations × m operations = O(n*m)")

4. **For the Optimal Solution**: Add a "THE TRICK" section explaining:
   - The key insight that makes this solution optimal
   - What problem-solving technique or data structure enables the optimization
   - How it improves upon previous approaches

## Format Example
```python
# [Solution Type] (e.g., Brute Force, Sorting, HashMap, etc.)
# Time complexity: O(...) - [Detailed explanation of why]
#                  [Break down each operation and its cost]
#                  [Show how they combine: O(n) + O(n log n) = O(n log n)]
# Space complexity: O(...) - [Detailed explanation of extra space used]
# Why this complexity: [1-2 sentence summary of the approach and why it has this complexity]
# THE TRICK: [For optimal solutions only - explain the key insight that makes it optimal]
#            [What technique/pattern is being used: complement lookup, sliding window, etc.]
#            [Why this eliminates the need for less efficient approaches]
class Solution:
    def methodName(self, params):
        # implementation
        pass