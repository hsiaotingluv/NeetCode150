import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.p = nums
        self.k = k
        heapq.heapify(self.p)
        while len(self.p) > k:
            heapq.heappop(self.p)
        
    def add(self, val: int) -> int:
        # if size of p is less than k, just push
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        # if size of p is k, push and pop
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]
        

k = 3
nums = [4, 5, 8, 2]
val = 3
# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(k, nums)
param_1 = obj.add(val)
print(param_1)

