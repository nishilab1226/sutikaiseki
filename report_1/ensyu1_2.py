import sys
import time
import random
import SortFunction as sort
import traceback

#元配列の格納、及び型の変換
arr = sys.argv[1:]
arr = sort.str2float(arr)
print("original array = ",arr)
print("array length = ",len(arr))

#各種引数の入力
while 1:
	try:
		start = int(input("start >>> "))
		if not 0 <= start <= len(arr):
			print("InputError:Please input a number greater than 0　and less than ",len(arr)," !\n")
			continue
		end = int(input("end >>> "))
		if not 0 <= end <= len(arr):
			print("InputError:Please input a number greater than 0　and less than ",len(arr)," !\n")
			continue
		if start > end:
			print("InputError:Please input a number smaller than end for start!\n")
			continue
		order = int(input("up_order:0 , down_order:1 >>> "))
		if not order in [0,1]:
			print("InputError:Please enter 0 or 1 for order!\n")
			continue
		sort_type = int(input("bubble:0 , merge:1 , quick:2 >>> "))
		if not sort_type in [0,1,2]:
			print("InputError:Please enter 0 ~ 2 for sort_type!\n")
			continue
	except (EOFError,ValueError):
		print("ValueError : Please input only numeric value!\n")
		continue
	break

#ソート
t_start = time.time()
try:
	if sort_type == 0:
		print("start bubbleSort >>> ")
		arr = sort.bubbleSort(arr[:],start,end,order)
	elif sort_type == 1:
		print("start mergeSort >>> ")
		arr = sort.mergeSort(arr[:],start,end,order)
	elif sort_type == 2:
		print("start quickSort >>> ")
		arr = sort.quickSort(arr[:],start,end,order)
	else:
		exit()

except TypeError as e:
	t, v, tb = sys.exc_info()
	print(traceback.format_exception(t,v,tb))
	print(traceback.format_tb(e.__traceback__))
	exit()

print("sorted array = ",arr)
print("elapsed_time = ",time.time()-t_start)
