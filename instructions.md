# Key Guidelines

1. Be Specific: Don't just say "O(n) because one loop" - explain what n represents and what operations happen in that loop
2. Show the Math: For nested operations, show how complexities combine (e.g., "O(n) × O(log n) = O(n log n)")
3. Identify Dominance: When multiple operations exist, identify which dominates (e.g., "O(n) + O(n²) = O(n²)")
4. Explain Trade-offs: Mention when we're trading space for time or vice versa
5. Highlight the Insight: For optimal solutions, clearly articulate the "aha moment" or pattern being used
6. Single Code Block: ALL content (solutions, tests, table, winner) in ONE code snippet
7. Consistent Naming: Use descriptive class names (BruteForceSolution, SortingSolution, HashMapSolution, Solution for optimal)
8. Test Cases: Include 2-4 test cases with:
- Input values clearly labeled
- Expected output
- Explanation of why that's the answer (especially for complex cases)
- At least one edge case
9. Comparison Table: Format as commented table at the bottom, comparing all approaches
10. Winner Declaration: Place after the table as a comment, stating which approach is best and why
11. All as Comments: The table and winner must be Python comments (using #) inside the code block

# Pattern Recognition Keywords for "THE TRICK"
## Use these patterns when explaining optimal solutions:

1. Complement/Difference lookup (e.g., target - current)
2. Sliding window (for subarray/substring problems)
3. Two pointers (for sorted array problems)
4. Hash map for O(1) lookup (trading space for time)
5. Monotonic stack/queue (for next greater/smaller element)
6. Dynamic programming (overlapping subproblems)
7. Prefix sum (for range queries)
8. Binary search (on sorted data)
9. Array as hash map (when domain is limited, e.g., lowercase letters)
10. Greedy approach (local optimal leads to global optimal)

# Example Structure for Multiple Solutions
## When presenting multiple solutions (brute force → optimized → optimal):

1. Start with the brute force approach with full comments
2. Progress to more optimized versions with full comments
3. End with the optimal solution, emphasizing THE TRICK that makes it best
4. Keep the original problem statement at the top
5. Keep test cases at the bottom

# Remember: The goal is to teach the pattern and reasoning, not just provide working code.
# Remember also: EVERYTHING goes in one code block - solutions, tests, table, and winner declaration!