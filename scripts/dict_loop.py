import numpy as np 
import sklearn as sk
import pandas as pd 
import os

os.chdir("C:\\Users\\tkalnik\\Desktop\\FantasyFooty")

DF = pd.DataFrame(pd.read_excel("FantasyPros_Fantasy_Football_Projections_All.xlsx", sheet_name="Combined"))

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

count = 583
try:
	while count > 0:
		a = input("Enter the name of the player that was selected: ")
		if a in QB:
			del QB[a]
			print(QB, '\n')
		elif a in RB:
			del RB[a]
			print(RB, '\n')
		elif a in WR:
			del WR[a]
			print(WR, '\n')
		elif a in TE:
			del TE[a]
			print(TE, '\n')
		elif a in K:
			del K[a]
			print(K, '\n')
		elif a in DST:
			del DST[a]
			print(DST, '\n')
		else:
			print("Error")
		count -= 1
except KeyboardInterrupt:
	pass