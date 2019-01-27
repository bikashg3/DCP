
# This returns in O(n^2) and is a naive solution
def naive_sol(arr,k):
  for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
      if (arr[i] + arr[j]) == k:
        return True
  return False
  


# This returns in O(nlogn) and in single pass
def one_pass(arr,k):
  arr.sort()
  start = 0
  end = len(arr)-1
  while start <= end:
    if (arr[start] + arr[end]) == k:
      return True
    elif arr[start] + arr[end] < k:
      start = start + 1
    else:
      end = end - 1
  return False


  
