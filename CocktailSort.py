# Algorithm -- Cocktail Sort
class CocktailSort():
    def __init__(self, list_sort):
        # The list that needed to be sorted
        self.list_sort = list_sort
        # To determine if there is number swapping in forward sorting 
        self.pos_count = False
        # To determine if there is number swapping in backward sorting 
        self.neg_count = False
        
    # Forward sorting
    def forward_sort(self, last):
        # Refresh the value of pos_count for every forward sort
        self.pos_count = False
        # To lock the number at the last index
        self.last = last
            
        # Use a for loop to compare each consecutive numbers in the list
        for item in range(len(self.list_sort) - 1 - self.last):
            # If the value of the current number is larger than the next number on the right
            if self.list_sort[item] > self.list_sort[item + 1]:
                # Swap the numbers
                self.list_sort[item], self.list_sort[item + 1] = self.list_sort[item + 1], self.list_sort[item]
                # Add one to pos_count
                self.pos_count = True
                
            # Print the current state of the list
            print(self.list_sort)
            
        # If there is number swapping in forward sorting 
        if self.pos_count == True:
            # Add one when a number was moved to the current last index of the list
            self.last += 1
            print("forward sort ends, moving to backward sort")# this line replaces print("for") in the video
            # Start backward sorting by calling the method 
            self.backward_sort(self.last)
       
        else:
            # End the sorting and print the final sorted result
            print("The sorted list is ", self.list_sort)
             
    #Backward sorting
    def backward_sort(self, first): 
        # Refresh the value of neg_count for every backward sort
        self.neg_count = False
        # To lock the number at the first index
        self.first = first - 1
        # Use a for loop to compare each consecutive numbers in the list
        for item in range(len(self.list_sort) - 1, self.first ,-1):
            # If the value of the current number is larger than the next number on the left
            if self.list_sort[item] < self.list_sort[item - 1]:
                # Swap the numbers
                self.list_sort[item], self.list_sort[item - 1] = self.list_sort[item - 1], self.list_sort[item]
                # Add one the neg_count
                self.neg_count = True
                
            # Print the current state of the list
            print(self.list_sort)
            
            
        # If there is number swapping in backward sorting 
        if self.neg_count == True:
            # Add one when a number was moved to the current first index of the list
            self.first += 1 
            print("backward sort ends, moving to forward sort")# this line replaces print("back") in the video
            # Start forward sorting by calling the method
            self.forward_sort(self.first)
            
        else:
            # End the sorting and print the final sorted result
            print("The sorted list is ", self.list_sort)

# User doesn't need to run to program again to sort another list
while True:
    # Ask for user's input and split the inputted value based on the space between them
    num_list = input("Enter some integer that you want to sort : ").split()
    # Convert the inputted data into numbers and put them into a list
    num_list = [float(i) for i in num_list ]
    # Start sorting the list 
    run_list = CocktailSort(num_list)
    run_list.forward_sort(0)
