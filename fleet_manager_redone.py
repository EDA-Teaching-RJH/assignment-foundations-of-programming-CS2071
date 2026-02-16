def main():
    print("- Made by Cameron Sands * CS2071@kent.ac.uk")
    name, rank, division, UnID = init_database()
    while True:
        try:
            display_menu()

            dis = int(input("^ - Choose: "))
            if dis == 1:
                display_roster(name,rank,division,UnID)

            elif dis == 2:
                add_crew(name,rank,division,UnID)
            
            elif dis == 3:
                update_crew(name,rank,division,UnID)

            elif dis == 4:
                remove_crew(name,rank,division,UnID)
            
            elif dis == 5:
                search_crew(name,rank,division,UnID)
            
            elif dis == 6:
                filter_by_division(name,rank,division,UnID)

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
    name = ["William", "Data", "Ro", "Tom", "Alyssa", "Reginald"]
    rank = ["Commander", "Lieutenant Commander", "Ensign", "Lieutenant", "Lieutenant Junior Grade", "Lieutenant"]
    division = ["Command", "Operations", "Command", "Command", "Science", "Operations"]
    UnID = ["1","2","3","4","5","6"]
    return name, rank, division, UnID
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

def add_crew(name, rank, division, UnID):
    i = str(input("\n* Enter New Crew Name: "))
    name.append(i)
    print("| Crew Name:", i, "\n|----------------")

    while True:
        print("| Ensign, Lieutenant Junior Grade, Lieutenant, Lieutenant Commander, Commander, Captain, Admiral")
        o = str(input("| Enter Crew Rank: "))
        match o:
            case "Ensign" | "Lieutenant Junior Grade" | "Lieutenant" | "Lieutenant Commander" | "Commander" | "Captain" | "Admiral" :
                rank.append(o)
                print("| Rank:", o, "\n|----------------")
                break
            case _:
                print("| Incorrect rank...\n| Try again...")

    u = str(input("| Enter Crew Division: "))
    division.append(u)
    print("| Division:", u, "\n|----------------")

    while True:
        n = str(input("| Enter Unique ID: "))
        if n not in UnID:
            UnID.append(n)
            print("| Unique ID:", n, "\n|----------------")
            break
        else:
            print("| Unique ID not usable...\n| Try again...")

    print("|","New Crew Member Established!","\n|",i,"-",o,"-",u,"\n*----------------")
    return name, rank, division, UnID

def remove_crew(name, rank, division,UnID):
        print(UnID)
        print(name)
        try:
            IDRemove = int(UnID.index(input("| Which Unique ID do you want to remove? : ")))
            name.pop(int(IDRemove))
            print("| Name has been removed...")
            rank.pop(int(IDRemove))
            print("| Rank has been removed...")
            division.pop(int(IDRemove))
            print("| Divison has been removed...")
            UnID.pop(int(IDRemove))
            print("| Unique ID has been removed...")
            print("*----------------", "\n| Crew file has been cleared.")
        except ValueError:
            print("| Invalid input...", "\n| Try again...")

def update_crew(name, rank, division, UnID):
    print("| 1 to", len(name))
    IDUpdate = int(input("| Which crew do you want to Update? : ")) -1
    print("*----------------")
                
    askUpdate = str(input("| Update Name (N), Rank (R), Division (D), or Unique ID (U)? : ")).strip()
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

    elif askUpdate == "U" or askUpdate == "u":
        print("| Current Unique ID is:", UnID[IDUpdate])
        checkUpdate = input("| Is this the ID you want to change (Y/N)? : ")
        if checkUpdate == "Y" or checkUpdate == "y":
            UnID.pop(IDUpdate)
            print("| Unique ID removed")
            while True:
                UnIDSelect =  str(input("| Input new ID: "))
                if UnIDSelect not in UnID:
                    UnID.insert(IDUpdate, UnIDSelect)
                    print("|", name[IDUpdate], rank[IDUpdate], division[IDUpdate], "\n*----------------")
                    break
                else:
                    print("| Unique ID not usable...\n| Try again...") 
        elif checkUpdate == "N" or checkUpdate == "n":
             print("*----------------")
            
        else:
            print("| Try Again...", "\n*----------------")
    
    else:
        print("| Invalid input...", "\n| Try again...")
    
def display_roster(name, rank, division,UnID):
    print("*----------------")
    print("\n| Name", " - ", "Rank", " - ", "Division", " - ", "UID")
    a=0
    for a in range(len(name)):
        print("|", name[a], " - ", rank[a], " - ", division[a], " - ", UnID[a])
        a = a +1
    print("*----------------")

def search_crew(name, rank, division, UnID):
    Sask = str(input("\n* Input search request: ")).strip()
    a=0
    if Sask in name:
        print("| Name found")
        for a in range(len(name)):
            if Sask == name[a]:
                print("|", name[a], rank[a], division[a], UnID[a])
            a = a+1
        print("*----------------")

    elif Sask in rank:
        print("| Rank found")
        for a in range(len(rank)):
            if Sask == rank[a]:
                print("|", name[a], rank[a], division[a], UnID[a])
            a = a+1
        print("*----------------")

    elif Sask in division:
        print("| Division found")
        for a in range(len(division)):
            if Sask == division[a]:
                print("|", name[a], rank[a], division[a], UnID[a])
            a = a+1
        print("*----------------")

    elif Sask in UnID:
        print("| Unique ID found")
        for a in range(len(UnID)):
            if Sask == UnID[a]:
                print("|", name[a], rank[a], division[a], UnID[a])
            a = a+1
        print("*----------------")
    else:
        print("| Nothing found")

def filter_by_division(name, rank, division,UnID):
    print("\n| Science, Command, Operations")
    Dfilter = str(input("* What division would you like to filter? :")).strip()
    a=0
    for a in range(len(division)):
            if division[a] == str(Dfilter):
                print("|",name[a], rank[a], division[a], UnID[a])
                a = a+1
    print("*----------------")

def calculate_payroll(rank):
    print("\n* Calculating total crew cost...")
    a=0
    b=0
    for a in range(len(rank)):
        match rank[a]:
            case "Ensign":
                b = b+200
                a = a+1

            case "Lieutenant Junior Grade":
                b = b+500
                a = a+1

            case "Lieutenant":
                b = b+650
                a = a+1

            case "Lieutenant Commander":
                b = b+800
                a = a+1

            case "Commander":
                b = b+1100
                a = a+1

            case "Captain":
                b = b+1400
                a = a+1

            case "Admiral":
                b = b+2000
                a = a+1
            case _:
                a = a+1
    print("| Total crew cost:",b)
    print("*----------------")

def count_officers(rank):
    print("\n* Officer Count")
    print("|", rank.count("Commander") + rank.count("Captain"))

main()