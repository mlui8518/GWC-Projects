class User: 

	def __init__(self, name):
		self.name = name 
		self.id = id
		self.connections = []


answer = input("Press 'a' to add connections; Press 'p' to make a post; Press 'm' to write a message; Press 'e' to exit")

selfConnections = {}
posts = {}

while answer != 'e':

	def add_connections ():
		#selfConnections = {}
		counter = 1 
		while True:
			Username = input("First Username (Type 'done' to quit):")
			if Username == 'done':
				break
			selfConnections[counter] = Username
			counter += 1
			print(selfConnections)
		

	def add_post ():
		#posts = {}
		counter = 1
		while True:
			timeMarker = input("Time Marker (Type 'done' to quit):")
			post = input("Post Content:")
			if post == 'done':
				break
			posts[counter] = timeMarker, post 
			counter += 1
			print(posts)
			#specific

	def add_message ():
		messages = {}
		counter = 1
		while 
		messageWho = input("Who are you sending this message to?")
		return messageWho
		messageText = input("Type your message.")
		return messageText
		print(messageWho, messageText)

	if answer == "a":
		add_connections()
		answer = input("Press 'a' to add connections; Press 'p' to make a post; Press 'e' to exit")

	if answer == "p":
		add_post()
		answer = input("Press 'a' to add connections; Press 'p' to make a post; Press 'e' to exit")

	if answer == "e":
		exit()

