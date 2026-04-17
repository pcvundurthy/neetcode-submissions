class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #CALCULATE COUNT AND PUSH TO MIN HEAP
        count={}
        freq=[]
        for num in nums:
            count[num]=1+count.get(num,0)
        for num in count.keys():
            heapq.heappush(freq,(count[num],num))
        #REMOVE MIN HEAP topmost value which is small IF THE LEN IS GREATER THAN K
            if len(freq)>k:
                heapq.heappop(freq)
        #EXTRACT ONLY VALUES FROM MIN HEAP AND OUTPUT        
        res=[]
        for i in range(k):
            res.append(heapq.heappop(freq)[1])
        return res

 







        
        