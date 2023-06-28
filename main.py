from nltk.chat.util import Chat

pairs = [
	[
		r"hi|hello|hey|sup|good morning|good afternoon|good night",
		["Well, howdy-doody!",
			"Hey there, partner!",
			"Howdy-ho, neighborino!",
			"How's it going, friend-a-roo?",
			"Hey, hey, fellas! What's kickin'?",
			"Golly gee, nice to see ya!",
			"Hello, hello! Ready for some adventures?",
			"Hey, hey! How's your day in this crazy old world?",
			"Greetings and salutations, my good chums!",
			"Hey, folks! Hope you're having a super-duper day!",]
	],
	[
		r"(.*)my name is (.*)(.*)",
		["Oh, hamburgers! It's nice to meet ya, %2! What can I do for ya today?",
			"Well, jumpin' Jupiter! %2 huh? That's a mighty fine name you got there. How can I assist ya?",
			"Hot diggity-dog! %2 is the name, huh? Pleasure to make your acquaintance. What can ol' Butters do for ya?",
			"Well, butter my biscuit! %2 you say? That's a swell name! How can I lend a hand today?",
			"Oh, gee willikers! %2 is in the house! Nice to meet ya! What brings ya here today?",
			"Holy moly! %2 is the name, and I'm Butters, pleased to meet ya! How can I be of service?",
			"Golly gee whiz! %2 huh? That's a real fancy name ya got there. How can ol' Butters help ya out?",]
	],
	[
		r"tell me about yourself|tell me something about you|i would like to know more about you",
		["""Well, hey there! I'm Butters Scotch, a cheerful and curious little fella from South Park. I may be a bit on the
naive side, but I always try my best to see the bright side of things. Life's an adventure, and I'm just a kid 
exploring the world one misadventure at a time!""",

			"""Golly gee, hiya! The name's Butters Scotch, and I'm just your friendly neighborhood kid in South Park. I've got
a heart as pure as a puppy's, always ready to lend a hand or share a laugh. I may get into some sticky situations, 
but with a smile on my face, I'll always find my way out!""",

			"""Howdy-ho, everybody! Butters Scotch reporting for duty! I may not be the smartest cookie in the jar, but I've 
got a heart of gold and an unwavering optimism that keeps me going. Whether it's facing bizarre challenges or 
making new friends, I'm always up for an exciting escapade!""",

			"""Hey, fellas! Butters Scotch here, just a kid with an imagination as big as South Park itself. I'm a bundle of 
energy and enthusiasm, ready to dive headfirst into whatever crazy situation comes my way. Life's full of 
surprises, and I'm here to embrace them with a giggle and a skip!""",

			"""Gee whiz, hello there! Butters Scotch at your service, folks. In this wild and unpredictable town of South Park, 
I'm just a lovable goofball, navigating the ups and downs with wide-eyed wonder. With my signature optimism and a 
knack for finding silver linings, I'm here to spread smiles and laughter wherever I go!"""]
	],
	[
		r"what are you gonna do today|any plans for today?|any ideas for today?",
		["""Golly gee, today I'm gonna embark on a grand adventure with my friends in South Park! We're planning to build 
the world's biggest snowman in Stark's Pond. I've got my trusty snow shovel and a heart full of excitement. Let's 
go make some frosty magic!""",

			"""Howdy-ho, pals! Today, I'm gonna spend some quality time with my folks. We're gonna have a good ol' family 
picnic in the park, complete with sandwiches, lemonade, and lots of laughter. It's all about cherishing those simple 
moments and creating memories that'll warm our hearts!""",

			"""Hey there, fellas! Guess what I'm up to today? I'm attending my art class at South Park Elementary. I'll be 
painting a masterpiece—maybe a landscape of our town or a colorful portrait of my friends. Art lets me express 
myself, and who knows, maybe I'll be the next Picasso!""",

			"""Gee whiz, today I've got a playdate with my buddy, Kenny. We're gonna have a blast at Casa Bonita, the coolest 
place in town! We'll go on thrilling rides, dive into a pool of sopapillas, and watch an exciting puppet show. 
It's gonna be a day filled with fun and endless giggles!""",

			"""Hello, hello! Today, I'm putting on my detective hat. My friends and I are playing detective, solving mysteries 
in South Park. We've got magnifying glasses, notepads, and a keen eye for clues. It's time to crack the case of the 
missing ice cream and bring justice to our sweet-toothed town!"""]
	],
	[
		r"tell me about your friends|what about your friends|do you have friends?",
		["""Well, let me tell ya all about my friends in South Park! First off, there's Stan Marsh, a brave and caring 
fella. He's always there to lend a helping hand and stands up for what's right, even if it means getting into 
trouble. Then we've got Kyle Broflovski, the brains of the group. He's super smart and passionate about making the 
world a better place. Cartman, well, he's... unique. He's the loud and outspoken one, always coming up with crazy 
schemes and stirring up trouble. Despite his flaws, he's still part of our gang. And let's not forget about Kenny 
McCormick, our lovable mystery. He may have some tough luck, but his loyalty and fearlessness are unmatched. 
Together, we go on wild adventures, navigate the ups and downs of growing up, and create memories that'll last a 
lifetime. With each of us bringing something special to the table, we're an unstoppable team, always ready to face 
whatever challenges come our way. Friendship, folks, that's what keeps us going in this crazy old town!""",

			"""Howdy-ho, let me introduce you to my incredible pals from South Park! Stan Marsh is like the anchor of our group. 
He's the voice of reason and has a heart of gold. Then there's Kyle Broflovski, the moral compass. He's never afraid to 
stand up for what's right, no matter the cost. Now, Cartman, he's a real character. He's got a big personality and can 
be a handful, but deep down, there's some semblance of friendship there. And of course, we have Kenny McCormick, the 
mysterious one. He's got a tough life, but his resilience and unwavering spirit inspire us all. Together, we're an 
eclectic bunch, navigating the wild and wacky adventures of South Park with laughter, loyalty, and a bond that can't be 
broken.""",

			"""Hey there, let me tell you about my extraordinary friends in South Park! Stan Marsh is the heart and soul of our 
gang. He's a natural-born leader, always looking out for everyone and making sure we stick together. Kyle Broflovski is 
the intellectual powerhouse, with a strong sense of justice and a knack for critical thinking. Then there's Cartman, a 
complicated character to say the least. He brings chaos, but also a bizarre form of friendship that somehow keeps us connected. 
And last but never least, we have Kenny McCormick, the enigma wrapped in an orange parka. Despite his frequent mishaps, 
he's a fiercely loyal friend who will go to great lengths for us. With this colorful crew by my side, South Park becomes 
an even more unpredictable and unforgettable place."""]
	],
]

reflections = {
	"i am": "you are",
	"i was": "you were",
	"i": "you",
	"i'm": "you are",
	"i'd": "you would",
	"i've": "you have",
	"i'll": "you will",
	"my": "your",
	"you are": "I am",
	"you were": "I was",
	"you've": "I have",
	"you'll": "I will",
	"your": "my",
	"yours": "mine",
	"you": "me",
	"my name is": "your name is",
	"my": "your",
	"i'm": "you're",
	"call me": "I'll call you",
}

print("To stop this chat type 'quit'")

while True:
	chatbot = Chat(pairs, reflections)
	input_text = input("You: ")
	response = chatbot.respond(input_text)

	if input_text == "quit":
		print("Well, it looks like it's time for me to say goodbye, folks.")
		break
	else:
		print(f"Butters: {response}")