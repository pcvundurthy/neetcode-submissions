class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        #print('res',res)
        for s in strs:
            count = [0] * 26
            for c in s:
                #print(ord(c), ord('a'),'ordc')
                count[ord(c) - ord('a')] += 1
            #print('count',s,count)
            res[tuple(count)].append(s)
            #print('resvalues',res)
        #print(res.values)    
        return list(res.values())