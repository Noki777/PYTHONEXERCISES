print ("\n\t\t Great Tomb of Naza\n\t\t\tFloor Guardians \n\n 1. Albedo \t\t 2. Shalltear Bloodfallen \n 3. Demiurge \t\t 4. Cocytus \n 5. Aura Bella Fiora \t 6. Mare Bella Fiore \n 7. Victim \t\t 8. Gargantua \n 9. Pandora's Actor \n")
def noki():

    klienth = {"1": " Name: Albedo \n Gender: Female \n Height: 170cm \n Race: Succubus \n Occupation: Guardian Overseer", "2" : " Name: Shalltear Bloodfallen \n Gender: Female \n Height: 140cm \n Race: True Vampire \n Occupation: 1st-3rd Floor Guardian", "3" : " Name: Demiurge \n Gender: Male \n Height: 181cm \n Race: Arch Devil \n Occupation: 7th Floor Guardian", "4" : " Name: Cocytus \n Gender: Male \n Height: 2.5m \n Race: Vermin Lord \n Occupation: 5th Floor Guardian ", "5" : " Name: Aura Bella Fiora \n Gender: Female \n Height: 104cm \n Race: Dark Elf \n Occupation: 6th Floor Guardian ", "6" : " Name: Mare Bello Fiore \n Gender: Male \n Height: 104cm \n Race: Dark Elf \n Occupation: 6th Floor Guardian", "7" : " Name: Victim \n Gender: Unknown \n Height: 1m \n Race: Angel \n Occupation: 8th Floor Guardian", "8" : " Name: Gargantua \n Gender: None \n Height: 30m \n Race: Golem \n Occupation: 4th Floor Guardian", "9" : " Name: Pandora's Actor \n Gender: Male \n Height: 177cm \n Race: Doppleganger \n Occupation: Guardian of the Treasury",}

    alpha= input("\n NO.  ")
    if alpha == 1:
        print klienth["1"]
    elif alpha == 2:
        print klienth ["2"]
    elif alpha == 3:
        print klienth ["3"]
    elif alpha == 4:
        print klienth ["4"]
    elif alpha == 5:
        print klienth ["5"]
    elif alpha == 6:
        print klienth ["6"]
    elif alpha == 7:
        print klienth ["7"]
    elif alpha == 8:
        print klienth ["8"]
    elif alpha == 9:
        print klienth ["9"]
    else:
        print ("Wait for more!!!")
        return noki()
    return noki()

    
noki()
