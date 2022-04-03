game = {'dota':1, 'CS':5, 'valorant':4, 'LOL':2, 'COC':3 }
sortedbyval = {k: v for k, v in sorted(game.items(), key= lambda v: v[1])}
print(sortedbyval)