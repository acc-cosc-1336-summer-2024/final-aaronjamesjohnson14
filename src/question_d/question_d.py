
def create_multiplication_table():

    multiplication_table = []

    for i in range (1, 6):
        row = []

        for j in range (1, 11):
            row.append(i*j)

        multiplication_table.append(row)

    return multiplication_table

def display_multiplication_table(multiplication_table):

    for row in multiplication_table:
        
        for num in row:
            print(num, end="\t")
       
        print()


def continue_option():

    print("Would You Like To Generate Again?" )
    print("1 - Yes")
    print("2 - No")

    continue_choice = int(input(""))

    if continue_choice == 1:
        menu_for_multiplication_table()
    
    elif continue_choice == 2: 
          exit()

    else:
         print("Unknown Choice... Please Try Again")
         continue_choice()

def menu_for_multiplication_table():

    multiplication_table = create_multiplication_table()

    display_multiplication_table(multiplication_table)

    continue_option()

menu_for_multiplication_table()

