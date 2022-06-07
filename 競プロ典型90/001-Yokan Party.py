"""
左右の長さが L [cm] のようかんがあります。 N 個の切れ目が付けられており、左から i 番目の切れ目は左から A 
i
​
  [cm] の位置にあります。

あなたは N 個の切れ目のうち K 個を選び、ようかんを K+1 個のピースに分割したいです。そこで、以下の値を スコア とします。

K+1 個のピースのうち、最も短いものの長さ（cm 単位）
スコアが最大となるように分割する場合に得られるスコアを求めてください。"""

def yokanParty(N, L, A, K):
  left = -1
  right = L + 1

  def check(mid):
    cut_count = 0
    prev = 0

    for i in range(N):
      if A[i] - prev >= mid:
        cut_count += 1
        prev = A[i]
    
    if L - prev >= mid:
      cut_count += 1

    return (cut_count >= K + 1)

  while right - left > 1:
    mid = (right + left) // 2
    if check(mid): # K回またはそれ以上でスコアをmid以上にできた場合
      left = mid
    else:
      right = mid

  return mid

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

print(yokanParty(N, L, A, K))

# python3 "001-Yokan Party.py"