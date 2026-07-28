# calculating the sum 
def sum(arr):
    sum = 0
    for i in arr: 
        sum = sum + i
    return sum

# calculating for the average
def average(arr):
    value = sum(arr) / len(arr)
    print(value)

# calculating the maximum number
def find_max(arr):
      max = arr[0]
      for i in arr:
           if i > max:
                max = i
      print(max)

#calculating the minimum
def find_min(arr):
     min = arr[0]
     for i in arr:
          if i < min:
               min = i
     print(min)
arr = [9,8,7,6,5]
find_min(arr)

find_max(arr)

print(sum(arr))
average(arr)