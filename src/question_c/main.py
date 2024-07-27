#add import

from question_c import Stock


def display_get_stock_history_menu():
     
    stock_dict = get_stock_history()

    print("Please Make Your Choice: ")
    print("1 - Display Stock Purchase History")
    print("2 - Exit")


    choice = input("")
        
    if choice == '1':
        display_stock_history(stock_dict)

        continue_option()

    elif choice == '2':
        exit()   
    else:
        print("Invalid choice. Please enter 1 or 2.")

def get_stock_history():
    
        stock1 = Stock("AAPL", "Apple Inc")
        stock2 = Stock("CAT", "Caterpillar")
        stock3 = Stock("EK", "Eastman Kodak")
        stock4 = Stock("GOOG", "Google")
        stock5 = Stock("MSFT", "Microsoft")
       

        stock_dict = {

            stock1.get_symbol(): stock1,
            stock2.get_symbol(): stock2,
            stock3.get_symbol(): stock3,
            stock4.get_symbol(): stock4,
            stock5.get_symbol(): stock5

                    }
        
        return stock_dict

def display_stock_history(stock_dict):

    print()

    for symbol, stock in stock_dict.items():
        
        company_name = stock.get_company_name()

        print (f"{company_name}, {symbol}")
    print()

def continue_option():

    print("Would You Like To Continue?" )
    print("1 - Yes")
    print("2 - No")

    continue_choice = int(input(""))

    if continue_choice == 1:
        display_get_stock_history_menu()
    
    elif continue_choice == 2: 
          exit()

    else:
         print("Unknown Choice... Please Try Again")
         continue_choice()


display_get_stock_history_menu()





