import numpy as np 
import sklearn as sk
import pandas as pd 
import os

os.chdir("C:\\Users\\tkalnik\\Desktop\\FantasyFooty")

DF = pd.DataFrame(pd.read_excel("FantasyPros_Fantasy_Football_Projections_All.xlsx", sheet_name="Combined"))

### Pandas column attributes
# print(DF.Player)
# print(DF.FPTS)

### Pandas iloc
# Prints just the first entry
# print(DF.iloc[:1])

### Pandas loc
# prints the first 50
# print(DF.loc[0:50])

QB = {}
RB = {} 
WR = {}
TE = {}
K = {}
DST = {}

# refactor because this is a bad construct
for i in range(len(DF.Player)):
	if DF.Position[i] == 'QB':
		Player = DF.Player[i]
		FPTS = DF.FPTS[i]
		QB[Player] = FPTS
	elif DF.Position[i] == 'RB':
		Player = DF.Player[i]
		FPTS = DF.FPTS[i]
		RB[Player] = FPTS
	elif DF.Position[i] == 'WR':
		Player = DF.Player[i]
		FPTS = DF.FPTS[i]
		WR[Player] = FPTS
	elif DF.Position[i] == 'TE':
		Player = DF.Player[i]
		FPTS = DF.FPTS[i]
		TE[Player] = FPTS
	elif DF.Position[i] == 'K':
		Player = DF.Player[i]
		FPTS = DF.FPTS[i]
		K[Player] = FPTS
	elif DF.Position[i] == 'DST':
		Player = DF.Player[i]
		FPTS = DF.FPTS[i]
		DST[Player] = FPTS

print(QB, '\n')
print(RB, '\n')
print(WR, '\n')
print(TE, '\n')
print(K, '\n')
print(DST, '\n')
