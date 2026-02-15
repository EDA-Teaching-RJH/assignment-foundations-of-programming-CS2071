name = ["A", "B", "C"]
rank = ["a", "b", "c"]
division = ["1", "2", "3"]

def main():
    fleet_manager()

def fleet_manager():
    while True:

        print("\n^ - Display Menu     -","\n1 - View Crew Files  -", "\n2 - Add Crew File    -", "\n3 - Update Crew File -", "\n4 - Remove Crew File -", "\n5 - Search Crew File -", "\n6 - Leave            -")
        try:
            dis = int(input("Choose: "))

            # View Crew
            if dis == 1:
                for a in range(len(name)):
                    print(name[a], " - ", rank[a], " - ", division[a], " - ", a+1)
                    a = a +1
        
            # Add Crew
            elif dis == 2:
                i = str(input("\nEnter New Crew Name: "))
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
                Uask = input("Index (I) or Names (N)? : ")
                if Uask == "I":
                    print("0 to", len(name))
                if Uask == "N":
                    print(name)

            # Remove Crew
            elif dis == 4:
                Rask = input("Index (I) or Names (N)? : ")
                if Rask == "I":
                    print("1 to", len(name)+1,"\n")
                    IDRemove = input("Which ID do you want to remove? : ")
                    name.pop(IDRemove-1)
                    print("Name has been removed...")
                    rank.pop(IDRemove)
                    print("Rank has been removed...")
                    division.pop(IDRemove)
                    print("Divison has been removed...")
                    print("Crew file has been cleared.")


                if Rask == "N":
                    print(name)

            # Search Crew
            elif dis == 5:
                Sask = input("Index (I) or Names (N)? : ")

            # Leave
            elif dis == 6:
                print("Killing Program...")
                break

            elif dis > 6:
                print("Input outside of range...", "\nTry again...")
        except ValueError:
            print("Invalid")



main()
