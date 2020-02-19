import random

deck =[]
suits=["♠","♥","♦","♣"]
cards=["A ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10","J ","Q ","K "]

def Shuffle(array):
    for a in range(len(array)-2):
        g=random.randint(a,(len(array)-1))
        b=array[a]
        array[a]=array[g]
        array[g]=b
    return(array)
def num(string):
    num=0
    for i in range(len(suits)):
        if suits[i] in string:
            num+=i*14
    for j in range(len(cards)):
        if cards[j] in string:
            num+=j
    return(num)
def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if num(arr[j]) > num(arr[j+1]) :
                arr[j], arr[j+1] = arr[j+1], arr[j]
def selection_sort(nums):
    # This value of i corresponds to how many values were sorted
    for i in range(len(nums)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(nums)):
            if num(nums[j]) < num(nums[lowest_value_index]):
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

for i in suits:
    for j in cards:
        deck.append(f"{j} of {i}")
for i in range(10):
    deck=Shuffle(deck)
    
for d in deck:
    print(d)
print("now Sort")
selection_sort(deck)
for d in deck:
    print(d)