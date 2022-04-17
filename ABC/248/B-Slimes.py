#AC

A, B, K = map(int, input().split())

def slimes(A, B, K):
  slime = A
  count = 0

  if slime >= B:
    return 0

  else:
    while ( slime < B ):
      slime *= K
      count += 1

  return count

print(slimes(A, B, K))