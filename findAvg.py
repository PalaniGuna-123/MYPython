# num=int(input("How many numbers ?"))
# total_sum =0
# for n in range (num):
#     numbers = float(input("Enter any number"))
#     total_sum+=numbers
#     avg=total_sum/num
    
# print("Average is ",avg)

numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
count = len(numbers)
average = total / count
print("Sum:", total)
print("Average:", average)

def sumof(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    print(sum)
sumof([2,3,4,5,6])


def sum_and_average(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    average = total / len(arr) 
    
    print("Sum:", total)
    print("Average:", average)

sum_and_average([2, 3, 4, 5, 6])


def guna(arr):
    total=0
    for i in range (len(arr)):
        total+=arr[i]
    avg=total/len(arr)
    print(avg)
    print(total)
guna([12,12,12])
   

