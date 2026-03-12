# START

while True:   # START OVER loop
    
    # INPUT
    L = input("Enter Left Gear sensor (1 = Retracted, 0 = Extended): ")
    R = input("Enter Right Gear sensor (1 = Retracted, 0 = Extended): ")
    C = input("Enter Cockpit Gear sensor (1 = Retracted, 0 = Extended): ")
    
    # Convert to Boolean
    L = bool(int(L))
    R = bool(int(R))
    C = bool(int(C))
    
    # PROCESS
    RL = not(not(C) and not(L) and not(R))
    GL = not(C) and not(L) and not(R)
    
    # DECISION
    if RL:
        print("All Gears Retracted")
        break   # END
    
    else:
        if GL:
            print("All Gears Extended")
            break   # END
        else:
            print("Problems with the gears!!!")    
        # Loop repeats automatically
