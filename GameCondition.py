class GameCondition:

if Player1HP = 0 && Player2HP != 0
    print "Player 2 Wins"
    break

else if Player2HP = 0 && Player1HP != 0
    print "Player 1 Wins"
    break

else if Player1HP = 0 && Player2HP == 0
    print "You both lose"
    break

else continue

if Player1AP = 0 && Player2AP = 0
    #run battlephase

else if Player1AP = 0 && Player2AP ! 0
    print "Waiting on Player 2"

else if Player1AP != 0 && Player2AP = 0
    print "Waiting on Player 1"

else continue

if Move 
    #Distance = sqrt ((x^2)^2 + (y^2)^2)  
    #AP <= Distance && AP -= Distance
    while AP <= Distance
        print "Invalid Movement"
        return 

if Attack
    #run abilities for each witch
    if Magic Arrow 
        
    

#From V: My code is below. Dont trust it, its busted.
#Start
#Load OldWitch
#Load Young Witch
if OldWitchHP == 0 and YoungWitchHP == 0:
    print('You Both Lose')
    elif OldWitchHP == 0 and YoungWitchHP != 0:
        print('YoungWitch Wins')
    elif OldWitchHP != 0 and YoungWitchHP ==0:
        print('OldWitch Wins')
    else continue:
            if OldWitchAP ==0 and YoungWitchHP == 0:
                end
        elif OldWitchAP == 0 and YoungWitchAP != 0:
            print('Waiting on YoungWitch')
        elif OldwitchAP != 0 and YoungWitchAP == 0:
            print('Waiting on OldWitch')
        else continue:
            #If Moving
            if move:
                location = #pull from character (x,y)
                x0 = location()[0]
                y0 = location()[1] #Z value, not y value
                movelocation = #pull location from Unity
                x = movelocation()[0]
                y = movelocation()[1]
                distance = sqrt((x^2)+(y^2))
                    check distance <= AP #Need to figure out how to make it do this for both
                        if false:
                            print('Invalid Movement')
                        else
                            location(x,y) = (x0+x , y0+y)
                end
            if MagicArrow:
                #Pull Magic Arrow stats
                arrowto = #pull from character click
                arrowfrom = location
                arrowdistance = sqrt((x^2)+(y^2))
                    check arrowdistance <= #Arrow Range
                        if false:
                            print('Invalid Target')
                        else
                    end #remember to do the damage calculation after all ap is used
            if MeleeAttack:
                meleefrom = location
                melee to #pull from character click
                melee distance = sqrt((x^2)+(y^2))
                    check meleedistance<= #melee range
                        if false:
                            print('Invalid Target')
                        else
                    end #remember to do the damage calculation after all the ap is used
            if FireBall:
                firefrom = location
                fireto = #pull from character click
                firedistance = sqrt((x^2)+(y^2))
                    check firedistance <= #fire range
                        if false:
                            print('Invalid Target')
                        else
                    end
