# Link: https://www.hackerrank.com/candidates/82cngd9g7f2?b=eyJ1c2VybmFtZSI6ImhzaWFvdGluZzA5MTlAZ21haWwuY29tIiwicGFzc3dvcmQiOiIyODQwNzlhMyIsImhpZGUiOnRydWUsImhpZGVTd2l0Y2hBY2NvdW50IjpmYWxzZSwiaGlkZVNoYXJlSGFja2VyUHJvZmlsZSI6ZmFsc2UsImFjY29tbW9kYXRpb25zIjpudWxsfQ==&utm_campaign=candidate-portal-v1&utm_content=6hlc6c94q7s&utm_medium=api&utm_source=v3_api_invited&utm_term=invite

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getPrefixScores' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# import queue
import heapq

def getPrefixScores(arr):
    ans = []
    cur_mx, prev_ans = 0, 0
    
    for ele in arr:
        cur_mx += ele
        ans.append(prev_ans + cur_mx)
        prev_ans = ans[-1]
    
    cur_mx = 0
    for i in range(len(arr)):
        cur_mx = max(cur_mx, arr[i])
        ans[i] += (i+1)*cur_mx
        ans[i] %= (10**9+7)
    
    return ans


if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getPrefixScores(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

# stdin
# 3
# 1
# 2
# 1