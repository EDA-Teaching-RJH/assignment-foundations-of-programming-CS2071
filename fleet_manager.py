name = ["A", "B", "C"]
rank = ["a", "b", "c"]
division = ["1", "2", "3"]

def main():
    fleet_manager()

def fleet_manager():
    while True:
        print("\n^ - Display Menu     -","\n1 - View Crew Files  -", "\n2 - Add Crew File    -", "\n3 - Update Crew File -", "\n4 - Remove Crew File -", "\n5 - Search Crew File -", "\n6 - Leave            -")
        dis = int(input("Choose: "))

        # View Crew
        if dis == 1:
            for a in range(len(name)):
                print(name[a], " - ", rank[a], " - ", division[a], " - ", a+1)
                a = a +1
        
        # Add Crew
        if dis == 2:
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
        #if dis == 3

        # Remove Crew
        #if dis == 4

        # Search Crew
        #if dis == 5

        # Leave
        if dis == 6:
            print("Killing Program...")
            break

    # Add Crew

    # Update Crew

    # Remove Crew

    # Search Crew


main()
