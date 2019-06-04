def insertSort(arr):
	i = 1
	for i in range(len(arr)):
		k = arr[i]
		j = i - 1
		while j >= 0 and k < arr[j]:
			temp = arr[j]
			arr[j] = arr[j+1]
			arr[j]	= temp
			j+=1
			return arr																					

a = 3
b = 4
def swap(a, b):
	# always include this function in all your sorting algorithms
	a, b = b,a
	return ( a, b)


newArr = [4,1,3,6,2]

print(insertSort(newArr))













		# while sorted_list <= arr:
		# 	if len(sorted_list) == 0:
		# 		sorted_list.append(arr[0])
		# 	if marker < sorted_list[0]:
		# 		sorted_list[0] =  marker




















	# sorted_list = []
	# marker = arr[0]
	# j = 1
	# for j in range(len(arr)):
	# 	if marker > arr[j]:
	# 		marker = arr[j]
	# 		largest_num = marker
	# 	while sorted_list <= arr:
	# 		sorted_list[0] = largest_num
	# 		# sorted_list.append(marker)
	# 		if marker < largest_num:
	# 			try:
	# 				marker = sorted_list[0]
	# 			except IndexError:
	# 				sorted_list.append(marker)
	# return sorted_list
