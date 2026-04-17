class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[]
        for n in nums:
            count[n]=1+count.get(n,0) 
        #print(count)
        sorted_count=dict(sorted(count.items(), key=lambda item:item[1], reverse=True))
        #print(list(sorted_count)[:k])

        return list(sorted_count)[:k]





        
        