#add import

def ask_list_rankings():

    list_rankings = []

    print("Hello! Please Enter Your 5 Numbers:")

    for i in range (1, 6):
        number = int(input(f"Please Enter Your Number {i}: "))
        list_rankings.append(number)


    lowest = min(list_rankings)
    highest = max(list_rankings)
    total = sum(list_rankings)
    average = total / len(list_rankings)


    print(f"The Lowest Number In The List Is {lowest}")
    print(f"The Highest Number In The List Is {highest}")
    print(f"The Total Of The Numbers In The List Is {total}")
    print(f"The Average Of The Numbers In The List Is {average}")

    

ask_list_rankings()
