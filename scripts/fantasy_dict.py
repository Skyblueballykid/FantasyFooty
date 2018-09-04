import numpy as np 
import sklearn as sk
import pandas as pd 
import os

# this script actually creates a dict of dicts (FPTS of Player), which causes an error when trying to remove players 

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

count = 583
try:
	while count > 0:
		a = input("Enter the name of the player that was selected: ")
		if a in QBdict:
			del QBdict[a]
			print(QBdict)
		elif a in RBdict:
			del RBdict[a]
			print(RBdict)
		elif a in WRdict:
			del WRdict[a]
			print(WRdict)
		elif a in TEdict:
			del TEdict[a]
			print(TEdict)
		elif a in Kdict:
			del Kdict[a]
			print(Kdict)
		elif a in DSTdict:
			del DSTdict[a]
			print(DSTdict)
		else:
			pass
	count -= 1
except KeyboardInterrupt:
	pass






