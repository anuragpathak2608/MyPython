'''Probelm statemetn : you have 2 list one containing name and other containing score of players, You have to print player name and his corsponding score'''

Player_Name = ['Sachin', 'Rahul', 'Pathan']
Player_Score = ['99', '65', '18']

ziped = zip(Player_Name,Player_Score)
ziped = set(ziped)

for player, score in ziped:
    print(player, score)

'''other way of printing'''
for p, s in ziped:
    print("Player : %s    Score : %s" %(p, s))