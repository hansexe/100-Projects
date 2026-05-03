import art
print(art.logo)

bidders = {}
def finalbid(bidding):
    highest_bid = 0
    for bidvalue in bidding:
        bidamount = bidding[bidvalue]
        if bidamount > highest_bid:
            highest_bid = bidamount
            winner = bidvalue
    print(f"The Winner is {winner}, with the bid value of {highest_bid}")

continuebid = True
while continuebid:
    name = input("Write you name.\n")
    value = int(input("Write an amount.\n"))
    bidder = input("Is there any other bidder?yes or no.\n").lower()
    bidders[name] = value
    if bidder == "yes":
       print("\n" * 20)
    else:
        continuebid = False
        finalbid(bidders)
