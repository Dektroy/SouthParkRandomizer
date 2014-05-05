from random import randint
import winsound
import webbrowser

test = ""

#while not test:

saison = randint(1, 17)
episode = 0
if saison == 1:
	episode = randint(1, 13)
elif saison == 2:
	episode = randint(1, 18)
elif saison in [3, 4, 6]:
	episode = randint(1, 17)
elif saison == 7:
	episode = randint(1, 15)
elif saison == 17:
	episode = randint(1, 10)
else:
	episode = randint(1, 14)
	#print("Saison : " + str(saison) + ", episode : " + str(episode))
webbrowser.open('http://south-park-streaming.com/saison-' + str(saison) + "/episode-" + str(episode) + "/*")
winsound.Beep(440, 100)
winsound.Beep(1337, 50)
	#test = raw_input("")
