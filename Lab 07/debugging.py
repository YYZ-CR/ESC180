import time
import random

def test(value):
    if value == 'Calculus':
        while True:
            print('calculus')
    pass

if __name__ == '__main__':
    move_y = int(8*random.random())
    move_x = int(8*random.random())
    while move_y >= 0:
        move_y = int(8*random.random())
        move_x = int(8*random.random())
        
    '''test('calculus')
    time.sleep(2)
    test('Calculus')'''
