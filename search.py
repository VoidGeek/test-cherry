def search(arr, N, x):
	for i in range(0, N):
		if (arr[i] == x):
			return i
	return -1

if __name__ == "__main__":
	
	arr = [int(i) for i in input("Enter array elements:").split()]
	x = int(input("Enter element to search"))
	N = len(arr)

	result = search(arr, N, x)
	if(result == -1):
		print("Element is not present in array")
	else:
		print("Element is present at index", result)
