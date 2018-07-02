import sys
import random
import SortFunction as sort
import traceback

#元配列の格納、及び型の変換
arr = list(range(10))
random.shuffle(arr)
arr = sort.str2float(arr)
print("original array = ",arr)
print("array length = ",len(arr),"\n")
print("-"*80)
#ソート
try:
	print("bubbleSort , default >>> ",sort.bubbleSort(arr[:]),"\n")
	print("bubbleSort , start=2 , end=5 >>> ",sort.bubbleSort(arr[:],2,5),"\n")
	print("bubbleSort , order=down_order >>> ",sort.bubbleSort(arr[:],order=1),"\n")
	print("bubbleSort , start=2 , end=5 , order=down_order >>> ",sort.bubbleSort(arr[:],2,5,1),"\n")
	print("-"*80)
	print("mergeSort , default >>> ",sort.mergeSort(arr[:]),"\n")
	print("mergeSort , start=2 , end=5 >>> ",sort.mergeSort(arr[:],2,5),"\n")
	print("mergeSort , order=down_order >>> ",sort.mergeSort(arr[:],order=1),"\n")
	print("mergeSort , start=2 , end=5 , order=down_order >>> ",sort.mergeSort(arr[:],2,5,1),"\n")
	print("-"*80)
	print("quickSort , default >>> ",sort.quickSort(arr[:]),"\n")
	print("quickSort , start=2 , end=5 >>> ",sort.quickSort(arr[:],2,5),"\n")
	print("quickSort , order=down_order >>> ",sort.quickSort(arr[:],order=1),"\n")
	print("quickSort , start=2 , end=5 , order=down_order >>> ",sort.quickSort(arr[:],2,5,1),"\n")

except TypeError as e:
	t, v, tb = sys.exc_info()
	print(traceback.format_exception(t,v,tb))
	print(traceback.format_tb(e.__traceback__))
	exit()

