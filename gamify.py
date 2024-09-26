def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''
    
    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration

    global cur_star, cur_star_activity, last_star, second_last_star
    
    global last_finished
    global bored_with_stars
    
    cur_hedons = 0
    cur_health = 0
    
    cur_star = False
    cur_star_activity = None
    last_star = -120
    second_last_star = -120
    
    bored_with_stars = False
    
    last_activity = None
    last_activity_duration = 0
    
    cur_time = 0
    
    last_finished = 0 # how long ago you last ran or textbook

def star_can_be_taken(activity):
    global cur_star_activity, cur_star, bored_with_stars
    return activity == cur_star_activity and not bored_with_stars and cur_star

def tired():
    global last_activity, last_finished
    if last_activity == None:
        return False
    return last_finished < 120
    
def perform_activity(activity, duration):
    global cur_hedons, cur_health, cur_star_activity, cur_time, cur_star, last_activity_duration, last_activity, last_finished
    cur_time += duration
    # if there is a star
    if star_can_be_taken(activity):
        if duration < 10:
            cur_hedons += 3 * duration
        else:
            cur_hedons += 3 * 10
    if activity == 'running':
        # updating health
        if duration > get_effective_minutes_left_health(activity):
            cur_health += 3 * get_effective_minutes_left_health(activity)
            cur_health += 1 * (duration - get_effective_minutes_left_health(activity))
        elif get_effective_minutes_left_health(activity) > 0:
            cur_health += 3 * duration
        else:
            cur_health += 1 * duration
        # updating hedons
        if tired(): # and cur_star_activity != activity:
            cur_hedons += -2 * duration
        else:
            if duration < 10:
                cur_hedons += 2 * duration
            else:
                cur_hedons += 20 - 2 * (duration - 10)
        # updating last_activity
        if last_activity != 'running':
            last_activity = 'running'
            last_activity_duration = 0
    elif activity == 'textbooks':
        # updating health
        cur_health += 2 * duration
        # updating hedons
        if tired(): # and cur_star_activity != activity:
            cur_hedons += -2 * duration
        else:
            if duration < 20:
                cur_hedons += 1 * duration
            else:
                cur_hedons += 20 - 1 * (duration - 20)
        # updating last_activity
        if last_activity != 'textbooks':
            last_activity = 'textbooks'
            last_activity_duration = 0
    elif activity == 'resting':
        cur_health += 0 * duration
        cur_hedons += 0 * duration
        if last_finished > 0 and last_activity == 'resting':
            last_finished += duration
        else:
            last_finished = duration
        if last_activity != 'resting':
            last_activity = 'resting'
            last_activity_duration = 0
    cur_star = False
    last_activity_duration += duration
    

def get_cur_hedons():
    global cur_hedons
    return cur_hedons
    
def get_cur_health():
    global cur_health
    return cur_health
    
def offer_star(activity):
    global cur_star, cur_star_activity, cur_time, last_star, bored_with_stars, second_last_star
    cur_star_activity = activity
    cur_star = True
    if (cur_time - second_last_star) < 120:
        bored_with_stars = True
    last_star, second_last_star = cur_time, last_star
    
        
def most_fun_activity_minute():
    if cur_star:
        return cur_star_activity
    elif tired():
        return 'resting'
    return 'running'
    
################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    pass
    
def get_effective_minutes_left_health(activity):
    global last_activity, last_activity_duration
    if last_activity == activity:
        return 180 - last_activity_duration
    return 180

def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    pass
            

def estimate_health_delta(activity, duration):
    pass
        
################################################################################
        
if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)    
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2           		
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)    
    offer_star("running")              
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)  
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10