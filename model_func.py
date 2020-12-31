#!/usr/bin/env python3
import os
from pathlib import Path
import sys

__projectdir__ = Path(os.path.dirname(os.path.realpath(__file__)) + '/')

def main():
    """
    We see that the only way this yields a solution is if Pi is a state.
    """
    inputdict = {}
    inputdict['equations'] = [
    'Pi = KAPPA * X + BETA * Pi_p'
    ,
    'X = X_p + 1/GAMMA*Pi_p'
    ]

    inputdict['paramssdict'] = {'BETA': 0.95, 'KAPPA': 0.1, 'GAMMA': 1}


    inputdict['controls'] = ['X']
    inputdict['states'] = ['Pi']
    inputdict['shocksindirect'] = ['Pi']

    inputdict['savefolder'] = __projectdir__ / Path('temp/')
    inputdict['savefolderlatexname'] = '\\reviewprojectdir nk-simple-fixedinterest-dsge/' + 'temp/'

    inputdict['loglineareqs'] = True
    sys.path.append(str(__projectdir__ / Path('submodules/dsge-perturbation/')))
    from dsge_bkdiscrete_func import discretelineardsgefull
    discretelineardsgefull(inputdict)

# Run:{{{1

main()
