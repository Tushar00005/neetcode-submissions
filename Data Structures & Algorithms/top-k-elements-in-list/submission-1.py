class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq={}
        # for i in nums:
        #     if i in freq:
        #         freq[i]+=1
        #     else:
        #         freq[i]=1
        # heap=[]
        # for num , count in freq.items():
        #     heapq.heappush(heap,(count,num))
        #     if len(heap)>k:
        #         heapq.heappop(heap)
        # return [num for count , num in heap]
        
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        heap=[]
        for num, count in freq.items():
            heapq.heappush(heap,(count,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for count , num in heap]

        