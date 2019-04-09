import os
os.remove("timestamp.log")
files = os.listdir(".\\storage\\frames\\")
for file in files:
	os.remove(".\\storage\\frames\\{}".format(file))