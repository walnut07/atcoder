"""
問題文
N+1 個の街があり、i 番目の街は A 
i
​
  体のモンスターに襲われています。

N 人の勇者が居て、i 番目の勇者は i 番目または i+1 番目の街を襲っているモンスターを合計で B 
i
​
  体まで倒すことができます。

N 人の勇者がうまく協力することで、合計して最大で何体のモンスターを倒せるでしょうか。"""

def howManyMonsterKilled(N, A, B):
  carry = 0
  monsters_killed = 0
  for i in range(N):
    if A[i] <= carry + B[i]:
        monsters_killed += A[i]
        carry = B[i] + carry - A[i]
    else:
      monsters_killed += carry + B[i]
      carry = 0
  
  if A[-1] < carry:
    monsters_killed += A[-1]
  else:
    monsters_killed += carry
  
  return monsters_killed

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(howManyMonsterKilled(N, A, B))

# python3 "C-City Savers.py"