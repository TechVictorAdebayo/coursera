# Function to create a list of inegers from users
def create_integer_list():
    # initialize an empty list to store integers 
    integer_list = []

    #Ask the user how many integers they want to enter
    num_elements = int(input("How many integers do you want to enter? "))

    #loop to accept each integer from user and add it to the list

    for i in range (num_elements):
        #Get input from the user (an integer ) and add to the list
        num = int(input(f"Enter integers {i+1}: "))
        integer_list.append(num)

    #return the list of integers
    return integer_list               
# function to compute the sum of integers in a list
def compute_sum (integer_list):
    #initialize a variable to store the sum
    total_sum = 0

    #loop through each integer in the list and add it to the sum
    for num in integer_list:
        total_sum += num           
    #Return the total sum   
    return total_sum

# main function 
def main ():
    #create the list of integers using the craeate_integer_list () function
    integer_list = create_integer_list()

    #Compute the sum of integers in the list using the compute_sum () function
    total_sum = compute_sum(integer_list)

    #Print the sum of integers 
    print("The sum of all the integers is:", total_sum)  

#call the main function to start the program
if __name__ == "__main__":
    main()