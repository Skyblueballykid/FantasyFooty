import numpy as np 
import sklearn as sk
import pandas as pd 
import os

os.chdir("C:\\Users\\tkalnik\\Desktop\\FantasyFooty")

QB = pd.DataFrame(pd.read_excel("FantasyPros_Fantasy_Football_Projections_All.xlsx", sheet_name="QB_short"))
RB = pd.DataFrame(pd.read_excel("FantasyPros_Fantasy_Football_Projections_All.xlsx", sheet_name="RB_short"))
WR = pd.DataFrame(pd.read_excel("FantasyPros_Fantasy_Football_Projections_All.xlsx", sheet_name="WR_short"))
TE = pd.DataFrame(pd.read_excel("FantasyPros_Fantasy_Football_Projections_All.xlsx", sheet_name="TE_short"))
K = pd.DataFrame(pd.read_excel("FantasyPros_Fantasy_Football_Projections_All.xlsx", sheet_name="K_short"))
DST = pd.DataFrame(pd.read_excel("FantasyPros_Fantasy_Football_Projections_All.xlsx", sheet_name="DST_short"))


QBdict = QB.set_index('Player').to_dict(orient='dict')
print("QBs", '\n', QBdict, '\n')

RBdict = RB.set_index('Player').to_dict(orient='dict')
print("RBs", '\n', RBdict, '\n')

WRdict = WR.set_index('Player').to_dict(orient='dict')
print("WRs", '\n', WRdict, '\n')

TEdict = TE.set_index('Player').to_dict(orient='dict')
print("TEs", '\n', TEdict, '\n')

Kdict = K.set_index('Player').to_dict(orient='dict')
print("Kickers", '\n', Kdict, '\n')

DSTdict = DST.set_index('Player').to_dict(orient='dict')
print("DSTs", '\n', DSTdict)








