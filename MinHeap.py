class MinHeap:# Min‑heap: smallest number always at the front
    def __init__(self):
        self.arr = []# Start with an empty list

    def push(self, val):# Add a number
        self.arr.append(val)# Put at the end
        i = len(self.arr) - 1 # Where it is now
        while i > 0:# Not at the front 
            mean = (i - 1) // 2# find the mean
            if self.arr[i] >= self.arr[mean]:# If it's not smaller than the mean, stop
                break
            self.arr[i], self.arr[mean] = self.arr[mean], self.arr[i]# Otherwise, swap with the mean
            i = mean# Move up and check again

    def pop(self):
        if not self.arr:
            return None
        if len(self.arr) == 1:
            return self.arr.pop()# Take out the smallest number (at the front)
        min_val = self.arr[0]# The front (smallest)
        self.arr[0] = self.arr.pop()# Move last number to front, remove last
        i = 0
        n = len(self.arr)
        while True:
            left = i * 2 + 1# First spot below (left side)
            right = i * 2 + 2# Second spot below (right side)
            smallest = i# Assume current spot is the smallest
            if left < n and self.arr[left] < self.arr[smallest]:
                smallest = left# Left below is smaller
            if right < n and self.arr[right] < self.arr[smallest]:
                smallest = right# Right below is smaller
            if smallest == i:# Current spot is already smaller than both below
                break# Swap with the smaller one below
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            i = smallest# Move down to that spot and continue
        return min_val

    def peek(self):# Look at the smallest number without removing it
        return self.arr[0] if self.arr else None

    def size(self):# How many numbers are in the heap
        return len(self.arr)

    def is_empty(self):# Check if it's empty
        return len(self.arr) == 0

def test_heap():
    h = MinHeap()
    n = input("Enter numbers separated by spaces:")
    nums = [int(x) for x in n.split()]
    for n in nums:
        h.push(n)
    print("the heap array:", h.arr)
    # User decides how many pops
    pop_count = int(input("How many times do you want to pop? Enter a number: "))
    print("Popping:")
    for P in range(pop_count):
        if h.is_empty():
            print("Heap is empty, stopping")
            break
        print("  pop ->", h.pop(), "heap left:", h.arr)
    # User enters any numbers to push
    push_input = input("Enter numbers to push (separated by spaces): ")
    push_nums = [int(x) for x in push_input.split()]
    for v in push_nums:
        h.push(v)
        print("  push", v, "->", h.arr)

    print("Smallest (peek):", h.peek())
    print("Size:", h.size())
    print("Is empty?", h.is_empty())

test_heap()





