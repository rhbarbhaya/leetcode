class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse = True)
            stones.append(stones.pop(0)-stones.pop(0))
        return(stones[0])