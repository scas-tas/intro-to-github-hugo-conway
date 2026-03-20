#tickets = 0
points = sales
def redeem_prizes(points):
    prizes = 0
    p = 5
    while points >= p:
        prizes += 1
        p *= 2
    return prizes
# print(redeem_prizes(points))

name = input("Name: ")
duration = int(input("How many weeks are you selling cookie dough for? "))
week = 1
while duration > week:
    sales = int(input(f"Week {week}, How many have you sold this week? "))
    week += 1
