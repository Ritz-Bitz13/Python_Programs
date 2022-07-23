#ask for 2 lists (elements are separated by spaces)

first_list = input("Enter your first list: ").split()
second_list = input("Enter your second list: ").split()


#easy way (pretend this does not exist)
#concat_list = first_list + second_list

#new list with enough capacity for all elements from both lists
concat_list = [None] * (len(first_list) + len(second_list))

#using a for loop to copy all elements from list 1
for index in range(len(first_list)):
    concat_list[index] = first_list[index]



#using a for loop to copy all elements from list 2
for index in range(len(second_list)):
    concat_list[index + len(first_list)] = second_list[index]


#regular way
for index in range (0, len(concat_list)):
    print(concat_list[index], end=" ")

#Exit Prompt    
input("\nPress [r] to restart: ")


##############another way############
first_list.extend(second_list)