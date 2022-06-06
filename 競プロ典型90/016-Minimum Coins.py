"""
問題文
A 円硬貨、B 円硬貨、C 円硬貨をそれぞれ 0 枚以上使ってちょうど N 円を支払うとき、使う硬貨の枚数として考えられる最小値を求めてください。

ただし、それぞれの硬貨は無数にあるものとします。"""

import math
N = int(input())
A, B, C = map(int, input().split())

def minCoins(N, A, B, C):
  ans = math.inf
  for a in range(9999):
    for b in range(9999 - a):
      c = (N - (A * a + B * b)) // C
      if (A * a + B * b + C * c) == N and c >= 0:
        ans = min(ans, a + b + c)

  return ans

print(minCoins(N, A, B, C))
#   python3 "016-Minimum Coins.py"