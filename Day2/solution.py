import math

# using division and O(1), space O(n) time
def naive_soln(arr):
	arr_prod = 1
	for i in arr:
		arr_prod = i*arr_prod
	for j in range(len(arr)):
		if arr[j] != 0:
			arr[j] = int(arr_prod/arr[j])
	return arr


# without using division and O(1) space, O(n) time
def smart_soln(arr):
	arr_sum = 0
	for i in range(len(arr)):
		arr_sum = arr_sum + math.log10(arr[i])
	for j in range(len(arr)):
		arr[j] = round(math.pow(10,arr_sum - math.log10(arr[j])))
	return arr

arr = [1, 2, 3, 4, 5]
#print(naive_soln(arr))
print(smart_soln(arr))
