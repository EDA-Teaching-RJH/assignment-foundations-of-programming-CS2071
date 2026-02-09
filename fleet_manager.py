name = ["A", "B", "C"]
rank = ["a", "b", "c"]
division = ["1", "2", "3"]
dis = 0

def main():
    fleet_manager()

def fleet_manager():
    print("\n^ - Display Menu     -","\n1 - View Crew Files  -", "\n2 - Add Crew File    -", "\n3 - Update Crew File -", "\n4 - Remove Crew File -", "\n5 - Search Crew File -")
    dis = int(input("Choose: "))

    if dis == 0:
        print("it broke")
    if dis == 1:
        for a in range(lens(name)):
            print(name, " - ", rank, " - ", division, " - ", name.index())
            a = a +1
        print("if works")

    # View Crew

    # Add Crew

    # Update Crew

    # Remove Crew

    # Search Crew


main()
