#!/usr/bin/env python3
import numpy as np

def main():

    yahtzee = 0
    rigole = 0
    sims = int(1e6)
    for i in range(int(sims)):
        dice = np.random.randint(1,7,size=5)
        for j in range(1,7):
            rigole_check = np.sum(dice)-3*j
            if np.sum(dice==j)==4 and rigole_check == 7:
    #            print(dice)
                rigole += 1
            yahtzee_check = np.sum(dice)-5*j
            if np.sum(dice==j)==5 and yahtzee_check == 0:
    #            print(dice)
                yahtzee += 1

    print(yahtzee, rigole)            

if __name__ == "__main__":
    main()
