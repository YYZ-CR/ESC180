def display_current_value():
    global current_value
    print(f'Current Value: {current_value}')

def previous_value():
    global previous
    global current_value
    previous = current_value

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

if __name__ == "__main__":
    current_value = 0
    memory = 0
    previous = 0
    print('Welcome to the calculator page.')
    display_current_value()
    add(5)
    mult(3)
    div(4) # if 0 is used, there will be a ZeroDivisionError
    display_current_value()
    save_to_memory()
    add(5)
    display_current_value()
    recall()
    display_current_value()
    add(5)
    display_current_value()
    undo()
    display_current_value()
    undo()
    display_current_value()




