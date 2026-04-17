class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-m for m in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            k1=heapq.heappop(stones)
            k2=heapq.heappop(stones)
            if k2>k1:
                heapq.heappush(stones,k1-k2)
        stones.append(0)
        return abs(stones[0])


