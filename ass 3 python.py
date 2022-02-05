##  QUESTION->1

print(" \t\t\t Question 1 \n\n")

# For making the code case insensitive,convert all upercase letters taking input string form user to count letters 
user_input = input("Enter string: ")
user_input = user_input.lower()

print()

count_dict = {}

# this empty dictionary helps to count a particular word 
# spliting the string in a list
user_words = user_input.split(" ")

# To check if input is a single word or not,for our help in counting dif character
if len(user_words) == 1:
    user_words = user_input

# user loop to count characters and words in the string
for word in user_words:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict.update({word : 1})

# Solution printing
if len(user_input) == 0:
    print("No word or sentence found.")
else:
    print("Number of each word/character in string is:" ,count_dict , "\n")
##  QUESTION->2 
print("\t\t\t Question 2 \n\n")

# Data required by the user
date = int(input("Enter the date: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
print()

# Calculation of the next date
if (1 <= month <= 12) and (1 <= date <= 31) and (1800 <= year <= 2025):
    
# Data validity check and calculating next date for 31 days months

    if month in (1,3,5,7,8,10):
        if date < 31:
            date += 1
        else:
            date = 1
            month += 1

# Calculating next date for 30 days months
    elif month in (4,6,9,11):
        if date < 30:
            date += 1
        else:
            date = 1
            month += 1

# Special case of february(28 days)
    elif month == 2:

# Leap year to be dealt separately, as 1 day is extra
        if year % 4 == 0:
            if date < 29:
                date += 1
            else:
                date = 1
                month += 1
        else:
            if date < 28:
                date += 1
            else:
                date = 1
                month += 1

# Next date for december (new year starts after 31st)
    else:
        if date < 31:
            date += 1
        else:
            date = 1
            month = 1
            year += 1

# Solution to the next date 
    if date == 1 and month == 1 and year == 2026:
        print("Date is out of range.")
    else:
        print(f"Next day is: {date}/{month}/{year}")
else:
# If date is invalid
    print("Invalid Date.")



## QUESTION->3
print("\n\t\t\t Question 3 \n")

# Initialise given list + output list
given_list = []
output_list = []

# User provides list data
max_input = int(input("Enter the total number of terms you gonna enter: "))
print()
for i in range(max_input):
    tmp_num = int(input(f"Enter the {i + 1} number: "))
    given_list.append(tmp_num)
print()

# Loop application for calculating square in given_list and add on this in output_list as tuple
for num in given_list:
    temp_tuple = (num,num*num)
    output_list.append(temp_tuple)

# Solution printed 
print(output_list)

##  QUESTION->4
print("\n\t\t\t Question 4 \n\n")

# taking grade point input
grade_num = int(input("Enter the grade number: "))
print()

# checking validity
if 4 <= grade_num <= 10:

    # If input is this, then what will your grade be
    if grade_num == 10:
        print("Your grade is 'A+' and Outstanding Performance")
    elif grade_num == 9:
        print("Your grade is 'A' and Excellent Performance")
    elif grade_num == 8:
        print("Your grade is 'B+' and Very Good Performance")
    elif grade_num == 7:
        print("Your grade is 'B' and Good Performance")
    elif grade_num == 6:
        print("Your grade is 'C+' and Average Performance")
    elif grade_num == 5:
        print("Your grade is 'C' and Below Average Performance")
    else:
        print("Your grade is 'D' and Poor Performance")

else:

# Printing invalid grade
    print("grade is Invalid.")
    
##  QUESTION->5
print("\n\t\t\t Question 5 \n\n")
print("\nQ.5")
print("The pattern is printed below:\n")
# Letters to be printed
abcd = "ABCDEFGHIJK"
# forming a list of letters
list_abcd = []
for i in abcd:
    list_abcd.append(i)
# Applying while loop to print required rows only
k = 1
while k <= 6:
    # printing 1st row intially when k=1
    for el in list_abcd:
        print(el, end="")
    # forming second row elements to be printed
    list_abcd.pop(len(list_abcd) - 1)  # removng las element of list
    list_abcd.pop(len(list_abcd) - 1)  # removing last element of list
    list_abcd.insert(0, " ")  # insertind space
    print()  # changing line using print()
    k = k + 1

    
##  QUESTION->6
print("\n\t\t\t Question 6 \n")
# First check running
repeat="Y"
# Empty dictionary
liste=["Y","y","n","N"]
dic={}
while repeat=="Y" or repeat=="y":
    # Input name and sid
    name = str(input("Enter student name:"))
    sid = int(input("Enter student SID:"))
    if sid<0:
        print("Error\nEnter correct SID")
    else:
        # SID addition to dic
        dic.update({sid: name})
        # More input condition because possible
        repeat = str(input("Enter Y to continue or N to end:"))
    if repeat=="N" or repeat=="n":
        break
    elif not (repeat in liste):
        print("\nError\nPlease enter valid input['Y' or 'N']")
        repeat=str(input("\nEnter Y to continue or N to end:"))

# a
print("\n Q6(a)")
print("The Dictionary containing {'SID':'Name'} is shown below")
print(dic)
# b
print("\n(b)\n")
# For sorting out sid with names make diff dic
student_names = list(dic.values())
student_sids = list(dic.keys())

# sort function used to sort names
sorted_names = sorted(student_names)

# iniliasing the sorted dict
sorted_dict_by_names = {}

# putting sorted values in dict
for name in sorted_names:
    for index in range(len(student_names)):
        if student_names[index] == name:
            sorted_dict_by_names.update({student_sids[index] : name})
        
#  Sorted dict by names
print("Sorted dict using students names is: " , sorted_dict_by_names)
# c
print("\n(c)\n")
sort_dic = sorted(dic)
dic2 = {}
for va in sort_dic:
    dic2.update({va: dic.get(va)})
print("The Dictionary after sorting according to SID:")
print(dic2)
# d
print("\n(d)\n)")
# Take input SID to be found out
enter_sid = int(input("Enter SID to get name of student:"))
# Dic search for sid 
output_name = str(dic.get(enter_sid))
# printing name with key sid
print(f"Name of student with SID {enter_sid} is {output_name}.")

##  QUESTION->7
print("\n\t\t\t Question 7 \n\n")

# Define the rec function to print fibonacci series
def fibonacci_seq(n):
    if n <= 1:
       return n
    return(fibonacci_seq(n-1) + fibonacci_seq(n-2))

# initialising variables to find the average
sum = 0
avg_counter = 0

while True:

    # User is to put the maximum number of terms to make the series
    max_num_of_terms = int(input("Enter the the max number of terms you want to print: "))
    print()

    # if max number is negative.
    if max_num_of_terms <= 0:
        print("Plese enter a positive integer")

    # printing fibonacci series using above rec function
    else:

        print(f"Fibonacci sequence with {max_num_of_terms} terms:")

        for count in range(max_num_of_terms):
            temp = fibonacci_seq(count)
            sum += temp
            avg_counter += 1
            print(temp)
        
        print()
        break

# To find average of fibonacci series
average_fab_seq = sum/avg_counter
print("Average of fab series is: ",average_fab_seq)

##  QUESTION->8
print("\n\t\t\t Question 8 \n\n")

# Set initialisation
set_1 = {1,2,3,4,5}
set_2 = {2,4,6,8}
set_3 = {1,5,9,13,17}

# part a
print("\t Part a \n")

# Intersection of set 1 & 2 is to be subtracted from union of both sets
set_sol_a = (set_1 | set_2) - (set_1 & set_2)
print("Set with all the elements of Set 1 and Set 2 but not both is:" ,set_sol_a)

# part b
print("\n\t (b) \n")

# Intersection of three sets and 2 at a time to be subtracted from total union of these three sets
set_sol_b = (set_1 | set_2 | set_3)- (set_1 & set_2 & set_3) - (set_2 & set_3) - (set_3 & set_1) - (set_2 & set_1)
print("The only non-repeating elements are : ", set_sol_b)

# part c
print("\n\t (c) \n")

# Intersection of two at a time and subtract intersection of three of these sets
set_sol_c = ((set_1 & set_2) | (set_2 & set_3) | (set_1 & set_3)) - (set_1 & set_2 & set_3)
print("The set of elements that are exactly two of the sets Set1, Set2 and Set3: ", set_sol_c)

# part d
print("\n\t (d) \n")

# Simply we write 1-10 and subtract set 1 from this
set_sol_d = {1,2,3,4,5,6,7,8,9,10} - set_1
print("The set having all int less than equal to 10 except that are not in set_1: ",set_sol_d)

# part e 
print("\n\t (e) \n")

# Simply we write 1-10 and subtract set 1,2,3 from this
set_sol_e = {1,2,3,4,5,6,7,8,9,10} - set_1 - set_2 - set_3
print("The set having all int less than equal to 10 except that are not in all the sets: ",set_sol_e)


