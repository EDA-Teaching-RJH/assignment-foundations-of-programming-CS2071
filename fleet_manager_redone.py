def main():
    print("- Made by Cameron Sands * CS2071@kent.ac.uk")
    name, rank, division = init_database()
    while True:
        try:
            display_menu()

            dis = int(input("^ - Choose: "))
            if dis == 1:
                display_roster(name,rank,division)

            elif dis == 2:
                add_crew(name,rank,division)
            
            elif dis == 3:
                update_crew(name,rank,division)

            elif dis == 4:
                remove_crew(name,rank,division)
            
            elif dis == 5:
                search_crew(name,rank,division)
            
            elif dis == 6:
                filter_by_division(name,rank,division)

            elif dis == 7:
                calculate_payroll(rank)

            elif dis == 8:
                count_officers(rank)

            elif dis == 9:
                    print("Killing Program...")
                    break
            
            elif dis > 9:
                print("| Input outside of range...", "\n| Try again...")
        
        except ValueError:
            print("| Invalid input...", "\n| Use numbers...")

def init_database():
    # Database
    name = ["Spock", "William", "Phlox", "Tom", "Kathryn", "Reginald"]
    rank = ["Commander", "First Officer", "Civilian", "Lieutenant", "Admiral", "Lieutenant"]
    division = ["Science", "Command", "Science", "Command", "Command", "Operations"]
    return name, rank, division
    # ID's can just use the .index function

def display_menu():
    print("\n^ - Display Menu     -")
    print("1 - View Crew Files  -")
    print("2 - Add Crew File    -")
    print("3 - Update Crew File -")
    print("4 - Remove Crew File -")
    print("5 - Search Crew File -")
    print("6 - Filter Crew File -")
    print("7 - Crew Payroll     -")
    print("8 - Officer Count    -")
    print("9 - Leave            -")

def add_crew(name, rank, division):
    i = str(input("\n* Enter New Crew Name: "))
    name.append(i)
    print("| Crew Name:", i, "\n|----------------")

    o = str(input("| Enter Crew Rank: "))
    rank.append(o)
    print("| Rank:", o, "\n|----------------")

    u = str(input("| Enter Crew Division: "))
    division.append(u)
    print("| Division:", u, "\n|----------------")

    print("|","New Crew Member Established!","\n|",i,"-",o,"-",u,"\n*----------------")
    return name, rank, division

def remove_crew(name, rank, division):
    Rask = input("\n* Index (I) or Names (N)? : ")
    if Rask == "I" or Rask == "i":
        print("| IDs from 1 to", len(name))
        try:
            IDRemove = int(input("| Which ID do you want to remove? : ")) -1
            name.pop(int(IDRemove))
            print("| Name has been removed...")
            rank.pop(int(IDRemove))
            print("| Rank has been removed...")
            division.pop(int(IDRemove))
            print("| Divison has been removed...")
            print("*----------------", "\n| Crew file has been cleared.")
        except ValueError:
            print("| Invalid input...", "\n| Try again...")


    if Rask == "N" or Rask == "n":
        print("|", name)
        try:
            NameRemove = name.index(str(input("| Which Name do you want to remove? :")))
            name.pop(int(NameRemove))
            print("| Name has been removed...")
            rank.pop(int(NameRemove))
            print("| Rank has been removed...")
            division.pop(int(NameRemove))
            print("| Divison has been removed...")
            print("*----------------", "\n| Crew file has been cleared.")
        except ValueError:
            print("| Invalid input...", "\n| Try again...")

def update_crew(name, rank, division):
    Uask = input("* Index (I) or Names (N)? : ")
    if Uask == "I" or Uask == "i":
        print("| 1 to", len(name))
        IDUpdate = int(input("| Which crew do you want to Update? : ")) -1
        print("*----------------")
        askUpdate = str(input("| Update Name (N), Rank (R), or Division (D)? : ")).strip()
        if askUpdate == "N" or askUpdate == "n":
            print("| Current name is:", name[IDUpdate])
            checkUpdate = input("| Is this the name you want to change (Y/N)? : ")
        if checkUpdate == "Y" or checkUpdate == "y":
            name.pop(IDUpdate)
            print("| Name removed")
            name.insert(IDUpdate, str(input("| Input new name: ")))
            print("|", name[IDUpdate], rank[IDUpdate], division[IDUpdate], "\n*----------------")
        elif checkUpdate == "N" or checkUpdate == "n":
            print("*----------------")
        else:
            print("| Try Again...", "\n*----------------")

    elif askUpdate == "R" or askUpdate == "r":
        print("| Current rank is:", rank[IDUpdate])
        checkUpdate = input("| Is this the rank you want to change (Y/N)? : ")
        if checkUpdate == "Y" or checkUpdate == "y":
            rank.pop(IDUpdate)
            print("| Rank removed")
            rank.insert(IDUpdate, str(input("| Input new rank: ")))
            print("|", name[IDUpdate], rank[IDUpdate], division[IDUpdate], "\n*----------------")
            
        elif checkUpdate == "N" or checkUpdate == "n":
            print("*----------------")
            
        else:
            print("| Try Again...", "\n*----------------")

    elif askUpdate == "D" or askUpdate == "d":
        print("| Current division is:", division[IDUpdate])    
        checkUpdate = input("| Is this the division you want to change (Y/N)? : ")
        if checkUpdate == "Y" or checkUpdate == "y":
            division.pop(IDUpdate)
            print("| Divison removed")
            division.insert(IDUpdate, str(input("| Input new division: ")))
            print("|", name[IDUpdate], rank[IDUpdate], division[IDUpdate], "\n*----------------")
            
        elif checkUpdate == "N" or checkUpdate == "n":
            print("*----------------")
            
        else:
                print("| Try Again...", "\n*----------------")
    
def display_roster(name, rank, division):
    print("*----------------")
    print("\n| Name", " - ", "Rank", " - ", "Division", " - ", "ID")
    for a in range(len(name)):
        print("|", name[a], " - ", rank[a], " - ", division[a], " - ", a+1)
        a = a +1
    print("*----------------")

def search_crew(name, rank, division):
    Sask = input("\n* Index (I) or Names (N)? : ")
    if Sask == "i" or Sask == "I":
        print("| IDs from 1 to", len(name))
        try:
            IDSearch = int(input("| Which ID do you want to look for? : ")) -1
            print("|", name[IDSearch], rank[IDSearch], division[IDSearch], IDSearch+1, "\n*----------------")
        except ValueError:
            print("| Invalid input...", "\n| Try again...")
    if Sask == "N" or Sask == "n":
        print("|", name)
        try:
            nameSearch = name.index(str(input("| What crew member do you want to look at? : ")).strip())
            print("|", name[nameSearch], rank[nameSearch], division[nameSearch], nameSearch+1, "\n*----------------")
        except ValueError:
            print("| Invalid input...", "\n| Try again...")

def filter_by_division(name, rank, division):
    print("\n| Science, Command, Operations")
    Dfilter = str(input("* What division would you like to filter? :")).strip()
    a=0
    for a in range(len(division)):
            if division[a] == str(Dfilter):
                print("|",name[a], rank[a], division[a])
                a = a+1
    print("*----------------")

def calculate_payroll(rank):
    payroll = ["1500","800","200","650","2500","650"]
    ...

def count_officers(rank):
    ...

def fleet_manager():
    while True:
        print("\n^ - Display Menu     -","\n1 - View Crew Files  -", "\n2 - Add Crew File    -", "\n3 - Update Crew File -", "\n4 - Remove Crew File -", "\n5 - Search Crew File -", "\n6 - Leave            -")
        # Funny
        try:
            dis = int(input("^ - Choose: "))

            # View Crew
            if dis == 1:
                print("*----------------")
                print("\n| Name", " - ", "Rank", " - ", "Division", " - ", "ID")
                for a in range(len(name)):
                    print("|", name[a], " - ", rank[a], " - ", division[a], " - ", a+1)
                    a = a +1
                print("*----------------")
        
            # Add Crew
            elif dis == 2:
                i = str(input("\n* Enter New Crew Name: "))
                name.append(i)
                print("| Crew Name:", i, "\n|----------------")

                o = str(input("| Enter Crew Rank: "))
                rank.append(o)
                print("| Rank:", o, "\n|----------------")

                u = str(input("| Enter Crew Division: "))
                division.append(u)
                print("| Division:", u, "\n|----------------")

                print("|","New Crew Member Established!","\n|",i,"-",o,"-",u,"\n*----------------")

            # Update Crew
            elif dis == 3:
                Uask = input("* Index (I) or Names (N)? : ")
                if Uask == "I" or Uask == "i":
                    print("| 1 to", len(name))
                    IDUpdate = int(input("| Which crew do you want to Update? : ")) -1
                    print("*----------------")
                    
                    askUpdate = str(input("| Update Name (N), Rank (R), or Division (D)? : ")).strip()
                    if askUpdate == "N" or askUpdate == "n":
                        print("| Current name is:", name[IDUpdate])
                        checkUpdate = input("| Is this the name you want to change (Y/N)? : ")
                        if checkUpdate == "Y" or checkUpdate == "y":
                            name.pop(IDUpdate)
                            print("| Name removed")
                            name.insert(IDUpdate, str(input("| Input new name: ")))
                            print("|", name[IDUpdate], rank[IDUpdate], division[IDUpdate], "\n*----------------")
                            continue
                        elif checkUpdate == "N" or checkUpdate == "n":
                            print("*----------------")
                            continue
                        else:
                            print("| Try Again...", "\n*----------------")

                    elif askUpdate == "R" or askUpdate == "r":
                        print("| Current rank is:", rank[IDUpdate])
                        checkUpdate = input("| Is this the rank you want to change (Y/N)? : ")
                        if checkUpdate == "Y" or checkUpdate == "y":
                            rank.pop(IDUpdate)
                            print("| Rank removed")
                            rank.insert(IDUpdate, str(input("| Input new rank: ")))
                            print("|", name[IDUpdate], rank[IDUpdate], division[IDUpdate], "\n*----------------")
                            continue
                        elif checkUpdate == "N" or checkUpdate == "n":
                            print("*----------------")
                            continue
                        else:
                            print("| Try Again...", "\n*----------------")

                    elif askUpdate == "D" or askUpdate == "d":
                        print("| Current division is:", division[IDUpdate])    
                        checkUpdate = input("| Is this the division you want to change (Y/N)? : ")
                        if checkUpdate == "Y" or checkUpdate == "y":
                            division.pop(IDUpdate)
                            print("| Divison removed")
                            division.insert(IDUpdate, str(input("| Input new division: ")))
                            print("|", name[IDUpdate], rank[IDUpdate], division[IDUpdate], "\n*----------------")
                            continue
                        elif checkUpdate == "N" or checkUpdate == "n":
                            print("*----------------")
                            continue
                        else:
                                print("| Try Again...", "\n*----------------")
                    else:
                        print("| Invalid input...", "\n| Try again...")



                if Uask == "N" or Uask == "n":
                    print("|", name)
                    nameUpdate = name.index(str(input("| Which crew do you want to Update? : ")))
                    print("*----------------")
                    
                    askUpdate = str(input("| Update Name (N), Rank (R), or Division (D)? : ")).strip()
                    if askUpdate == "N" or askUpdate == "n":
                        print("| Current name is:", name[nameUpdate])
                        checkUpdate = input("| Is this the name you want to change (Y/N)? : ")
                        if checkUpdate == "Y" or checkUpdate == "y":
                            name.pop(nameUpdate)
                            print("| Name removed")
                            name.insert(nameUpdate, str(input("| Input new name: ")))
                            print("|", name[nameUpdate], rank[nameUpdate], division[nameUpdate], "\n*----------------")
                            continue
                        elif checkUpdate == "N" or checkUpdate == "n":
                            print("*----------------")
                            continue
                        else:
                            print("| Try Again...", "\n*----------------")

                    elif askUpdate == "R" or askUpdate == "r":
                        print("| Current rank is:", rank[nameUpdate])
                        checkUpdate = input("| Is this the rank you want to change (Y/N)? : ")
                        if checkUpdate == "Y" or checkUpdate == "y":
                            rank.pop(nameUpdate)
                            print("| Rank removed")
                            rank.insert(nameUpdate, str(input("| Input new rank: ")))
                            print("|", name[nameUpdate], rank[nameUpdate], division[nameUpdate], "\n*----------------")
                            continue
                        elif checkUpdate == "N" or checkUpdate == "n":
                            print("*----------------")
                            continue
                        else:
                            print("| Try Again...", "\n*----------------")

                    elif askUpdate == "D" or askUpdate == "d":
                        print("| Current division is:", division[nameUpdate])    
                        checkUpdate = input("| Is this the division you want to change (Y/N)? : ")
                        if checkUpdate == "Y" or checkUpdate == "y":
                            division.pop(nameUpdate)
                            print("| Divison removed")
                            division.insert(nameUpdate, str(input("| Input new division: ")))
                            print("|", name[nameUpdate], rank[nameUpdate], division[nameUpdate], "\n*----------------")
                            continue
                        elif checkUpdate == "N" or checkUpdate == "n":
                            print("*----------------")
                            continue
                        else:
                                print("| Try Again...", "\n*----------------")
                    else:
                        print("| Invalid input...", "\n| Try again...")

                else:
                    print("| Try Again...", "\n*----------------")

            # Remove Crew
            elif dis == 4:
                Rask = input("\n* Index (I) or Names (N)? : ")
                if Rask == "I" or Rask == "i":
                    print("| IDs from 1 to", len(name))
                    try:
                        IDRemove = int(input("| Which ID do you want to remove? : ")) -1
                        name.pop(int(IDRemove))
                        print("| Name has been removed...")
                        rank.pop(int(IDRemove))
                        print("| Rank has been removed...")
                        division.pop(int(IDRemove))
                        print("| Divison has been removed...")
                        print("*----------------", "\n| Crew file has been cleared.")
                    except ValueError:
                        print("| Invalid input...", "\n| Try again...")


                if Rask == "N" or Rask == "n":
                    print("|", name)
                    try:
                        NameRemove = name.index(str(input("| Which Name do you want to remove? :")))
                        name.pop(int(NameRemove))
                        print("| Name has been removed...")
                        rank.pop(int(NameRemove))
                        print("| Rank has been removed...")
                        division.pop(int(NameRemove))
                        print("| Divison has been removed...")
                        print("*----------------", "\n| Crew file has been cleared.")
                    except ValueError:
                        print("| Invalid input...", "\n| Try again...")

            # Search and Filter Crew
            elif dis == 5:
                Fask = input("\n* Filter (F) or Search (S)? : ")

                if Fask == "F" or Fask == "f":
                    Sask = input("\n* Index (I) or Names (N)? : ")
                    if Sask == "i" or Sask == "I":
                        print("| IDs from 1 to", len(name))
                        try:
                            IDSearch = int(input("| Which ID do you want to look for? : ")) -1
                            print("|", name[IDSearch], rank[IDSearch], division[IDSearch], IDSearch+1, "\n*----------------")
                        except ValueError:
                            print("| Invalid input...", "\n| Try again...")
                    if Sask == "N" or Sask == "n":
                        print("|", name)
                        try:
                            nameSearch = name.index(str(input("| What crew member do you want to look at? : ")).strip())
                            print("|", name[nameSearch], rank[nameSearch], division[nameSearch], nameSearch+1, "\n*----------------")
                        except ValueError:
                            print("| Invalid input...", "\n| Try again...")

                        print("|", name)


            # Leave
            elif dis == 6:
                print("Killing Program...")
                break

            elif dis > 6:
                print("| Input outside of range...", "\n| Try again...")
        except ValueError:
            print("| Invalid input...", "\n| Use numbers...")



main()