def drink_coffee():
    global last_coffee_time, last_coffee_time2, too_much_coffee, knols
    if (last_coffee_time + last_coffee_time2) < 120 and last_coffee_time >= 0 and last_coffee_time2 >= 0:
        too_much_coffee = True
    else:
        last_coffee_time, last_coffee_time2 = 0, last_coffee_time
    print(knols)


def study(minutes):
    global current_time, knols, too_much_coffee, last_coffee_time, last_coffee_time2
    current_time += minutes
    if too_much_coffee:
        pass
    elif last_coffee_time == 0:
        knols += minutes*10
        last_coffee_time += minutes
    else:
        knols += minutes*5
        last_coffee_time += minutes
    print(knols)

def initialize():
    global too_much_coffee
    global current_time
    global last_coffee_time
    global last_coffee_time2
    global knols
    too_much_coffee = False
    current_time = 0
    knols = 0
    last_coffee_time = -100
    last_coffee_time2 = -100
'''
if __name__ == '__main__':
    initialize() # start the simulation
    study(60) # knols = 300
    study(20) # knols = 400
    drink_coffee() # knols = 400
    study(20) # knols = 500
    drink_coffee() # knols = 500
    drink_coffee()
    study(10) # knols = 600
    drink_coffee() # knols = 600, 3rd coffee in 20 minutes
    study(10) # knols = 600
'''
initialize() # start the simulation
study(60) # knols = 300
study(20) # knols = 400
drink_coffee() # knols = 400
study(10) # knols = 500
drink_coffee() # knols = 500
study(10) # knols = 600
drink_coffee() # knols = 600, 3rd coffee in 20 minutes
study(10) # knols = 600