name = ["Spock", "William", "Phlox", "Tom", "Kathryn", "Reginald"]
rank = ["Commander", "FIrst Officer", "Civilian", "Lieutenant", "Admiral", "Lieutenant"]
division = ["Science", "Command", "Science", "Command", "Command", "Operations"]

def main():
    fleet_manager()

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
                    print("| ", name[a], " - ", rank[a], " - ", division[a], " - ", a+1)
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
                if Uask == "I":
                    print("| 0 to", len(name))
                if Uask == "N":
                    print("|", name)

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

            # Search Crew
            elif dis == 5:
                Sask = input("Index (I) or Names (N)? : ")

            # Leave
            elif dis == 6:
                print("Killing Program...")
                break

            elif dis > 6:
                print("| Input outside of range...", "\n| Try again...")
        except ValueError:
            print("| Invalid input...", "\n| Use numbers...")



main()
