def reward_function(params):

    # Read input parameters
    speed = params['speed']
    progress = params['progress']
    steps = params['steps']
    all_wheels_on_track = params['all_wheels_on_track']
    
    reward = 0.0001
    TOTAL_NUM_STEPS = 250
    
    if all_wheels_on_track:
        reward = speed
        if(progress == 100) and steps <= TOTAL_NUM_STEPS:
            reward += 100 + speed**2
        elif progress > (steps / TOTAL_NUM_STEPS) * 100:
            reward = reward + speed**2 
        
    return float(reward)
