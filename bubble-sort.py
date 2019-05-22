''' Bubble sort'''

def bubblesort(arr):
  n = len(arr)
  for i in range(n):
    print("I am i",i)
    for j in range(0,n-i-1):
      print("I am j",j)
      if arr[j] > arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp

arr = [64, 34, 25, 12, 22, 11, 90] 
bubblesort(arr)
for i in range(len(arr)): 
    print (arr[i])
