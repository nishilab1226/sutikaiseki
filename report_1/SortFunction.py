#バブルソート、マージソート、クイックソート、値の型判定、配列の範囲判定
import random
#--------------------------------------------------------------
def bubbleSort(arr,start=0,end=-1,order=0) :
	if end == -1: end=len(arr)
	if not (start <= end or 0 <= start <= len(arr) or 0 <= end <= len(arr) or order in [0,1]):
		print("TypeError : Argument is wrong!")
		raise TypeError
	if len(arr) <= 1 :
		return arr

	for i in range(end-1,start,-1) :
		for j in range(start,i) :
			if arr[j]<arr[j+1] if order else arr[j]>arr[j+1] :
				arr[j],arr[j+1] = arr[j+1],arr[j]
	return arr

#--------------------------------------------------------------
def mergeSort(arr,start=0,end=-1,order=0) :
	if end == -1: end=len(arr)
	if not (start <= end or 0 <= start <= len(arr) or 0 <= end <= len(arr) or order in [0,1]):
		print("TypeError : Argument is wrong!")
		raise TypeError

	if len(arr) <= 1 :
		return arr
	mid = int((end+start)/2)
	left = mergeSort(arr[start:mid],order=order)
	right = mergeSort(arr[mid:end],order=order)

	result = []
	while 0 < len(left) and 0 < len(right) :
		if left[0] >= right[0] if order else left[0] <= right[0] :
			result.append(left.pop(0))
		else :
			result.append(right.pop(0))
	if left :
		result.extend(left)
	if right :
		result.extend(right)
	if end != len(arr) :
		result = result + arr[end:len(arr)]
	if start != 0 :
		result = arr[0:start] + result

	return result

#--------------------------------------------------------------
def quickSort(arr,start=0,end=-1,order=0):
	if end == -1: end=len(arr)
	if not (start <= end or 0 <= start <= len(arr) or 0 <= end <= len(arr) or order in [0,1]):
		print("TypeError : Argument is wrong!")
		raise TypeError
	if len(arr) == 0: return arr
	left = [x for x in arr[start+1:end] if (x < arr[start] if order==0 else x >= arr[start])]
	right = [x for x in arr[start+1:end] if (x >= arr[start] if order==0 else x < arr[start])]
	return arr[:start] + \
		quickSort(left,0,len(left),order=order) + \
		[arr[start]] + \
		quickSort(right,0,len(right),order=order) + \
		arr[end:]

#--------------------------------------------------------------
def str2float(arr):
	try:
		return list(map(int,arr))
	except ValueError:
		print("ValueError : Please input only numeric value!")
		exit()
	except TypeError:
		return [float(arr)]