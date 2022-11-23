def main():
    print("This program converts US dollars to Turkısh lira")
    print()

    dollars = eval(input("Enter amount in dollars: "))

    tl = convert_to_tl(dollars)

    print("That is", tl, "tl. ")


convert_to_tl = lambda dollars: dollars * 18.62

main()