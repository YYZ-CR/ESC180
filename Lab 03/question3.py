def display_current_value():
    global current_value
    print(f'Current Value: {current_value}')

def previous_value():
    global previous
    global current_value
    previous_previous_value()
    previous = current_value
    
def previous_previous_value():
    global previous2
    global previous
    previous2 = previous

def add(to_add):
    global current_value 
    previous_value()
    current_value += to_add

def mult(to_mult):
    global current_value 
    previous_value()
    current_value *= to_mult

def div(to_div):
    global current_value 
    previous_value()
    current_value /= to_div

def save_to_memory():
    global current_value
    global memory
    previous_value()
    memory = current_value

def recall():
    global current_value
    global memory
    previous_value()
    current_value = memory

def undo():
    global current_value
    global previous
    previous, current_value = current_value, previous

def undo2():
    global current_value
    global previous
    global previous2
    current_value, previous, previous2= previous2, current_value, previous

if __name__ == "__main__":
    current_value = 0
    memory = 0
    previous = 0
    previous2 = 0
    print('Welcome to the calculator page.')
    display_current_value() #0
    add(5)
    display_current_value() #5
    mult(3)
    display_current_value() #15
    div(4) # if 0 is used, there will be a ZeroDivisionError
    display_current_value() #3.75
    save_to_memory()
    add(5)
    display_current_value() #8.75
    recall()
    display_current_value() #3.75
    add(5)
    display_current_value() #8.75
    undo()
    display_current_value() #3.75
    undo()
    display_current_value() #8.75
    add(20)
    display_current_value() #28.75
    undo2()
    display_current_value() #3.75




