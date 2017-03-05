import random
from random import randint
import math
import time
import os
# first we need to import the random shit that let's us generate random things

#now we're going to ask the user for some inputs and define a few things
times = int(input('How many Cities? '))
citySize = input('input City size. 1-7. put 0 for random. ')

#this makes the size of the cities they want to generate an integer so we can use it
k = int(citySize)

iteration = 0
timeInitial = time.time()
timeEstimate = '...'
#this is so you can have an idea of how far along the program is and how much time is left
avgFileSize = ((random.randint(955,985)/1000) + (random.randint(955,985)/1000) + (random.randint(955,985)/1000) + (random.randint(955,985)/1000) + (random.randint(955,985)/1000)) / 5

for i in range(0,int(times)):

	#this is for the loading bar
	#this is the percentage done the program is
	barPercent = round((iteration + 1) / times * 100, 1)
	#this rewrites the number by rounding it to the numbers between 0 and 20 by dividing it by 5 since it's already out of 100 and then rounding
	percentDone = int(round(barPercent/5.0))
	#this makes the percent left a number from 0 to 20 by subtracting the percent done from 20
	percentLeft = int(20 - percentDone)
	#this if statement makes the loading bar one extra space over when there are only 4 characters in the percentage instead of 5
	if barPercent < 10:
		#this is the clever bit, it takes the numbers from 1 to 20 and uses them to make a bar, █ is a 5% finished so it simply repeats by however many 5%'s have been done
		barImage = str(timeEstimate) + 's ' + '[' + str('█'*percentDone) + str('-'*percentLeft) + '] ' + 'Estimated File Size on Completion: ' + str(round(times * avgFileSize, 2)) + 'KB  '
	else:
		barImage = str(timeEstimate) + 's ' + '[' + str('█'*percentDone) + str('-'*percentLeft) + '] ' + 'Estimated File Size on Completion: ' + str(round(times * avgFileSize, 2)) + 'KB  '


#This is to assign appropriate names and population to the cities
	if k == 1:
		j = random.randint(40,200)
		foo2 = ['ville', ' Thorp' , 'ton', 'bur', 'port', 'y', 'dale', ' Beach', 'hill', 'rock', 'stone', 'borough', 'rapids', 'on']
		secondPart = random.choice(foo2)
	elif k == 2:
		j = random.randint(200,500)
		foo2 = [' town', 'ville', ' Thorp' , 'ton', 'bur', 'port', 'y', 'dale', ' Beach', 'hill', 'rock', 'stone', 'borough', 'rapids', 'on']
		secondpart = random.choice(foo2)
	elif k == 3:
		j = random.randint(500,1000)
		foo2 = [' town', 'ville', 'ton', 'bur', 'port', 'y', 'dale', ' Beach', 'hill', 'rock', 'stone', 'borough', 'rapids', 'on']
		secondpart = random.choice(foo2)
	elif k == 4:
		j = random.randint(1000,5000)
		foo2 = [' City', ' town', 'ville', 'ton', 'bur', 'port', 'y', 'dale', ' Beach', 'hill', 'rock', 'stone', 'borough', 'rapids', 'on']
		secondpart = random.choice(foo2)
	elif k == 5:
		j = random.randint(5000,10000)
		foo2 = [' City', ' town', 'ville', 'ton', 'bur', 'port', 'y', 'dale', ' Beach', 'hill', 'rock', 'stone', 'borough', 'rapids', 'on']
		secondpart = random.choice(foo2)
	elif k == 6:
		j = random.randint(10000,75000)
		foo2 = [' City', 'ville', 'ton', 'bur', 'port', 'y', 'dale', ' Beach', 'hill', 'rock', 'stone', 'borough', 'rapids', 'on']
		secondpart = random.choice(foo2)
	elif k == 7:
		j = random.randint(75000,160000)
		foo2 = [' City', 'ville', 'ton', 'bur', 'port', 'y', 'dale', ' Beach', 'hill', 'rock', 'stone', 'borough', 'rapids', 'on']
		secondpart = random.choice(foo2)
	else:
		k0 = random.randint(1,30)
		if 1 <= k0 <= 8 :
			j = random.randint(40,200)
			foo2 = ['ville', ' Thorp' , 'ton', 'bur', 'port', 'y', 'dale', ' Beach', 'hill', 'rock', 'stone', 'borough', 'rapids', 'on']
			secondpart = random.choice(foo2)
		elif 9 <= k0 <= 15 :
			j = random.randint(200,500)
			foo2 = [' town', 'ville', ' Thorp' , 'ton', 'bur', 'port', 'y', 'dale', ' Beach', 'hill', 'rock', 'stone', 'borough', 'rapids', 'on']
			secondpart = random.choice(foo2)
		elif 16 <= k0 <= 20 :
			j = random.randint(500,1000)
			foo2 = [' town', 'ville', 'ton', 'bur', 'port', 'y', 'dale', ' Beach', 'hill', 'rock', 'stone', 'borough', 'rapids', 'on']
			secondpart = random.choice(foo2)
		elif 21 <= k0 <= 24 :
			j = random.randint(1000,5000)
			foo2 = [' City', ' town', 'ville', 'ton', 'bur', 'port', 'y', 'dale', ' Beach', 'hill', 'rock', 'stone', 'borough', 'rapids', 'on']
			secondpart = random.choice(foo2)
		elif 25 <= k0 <= 27 :
			j = random.randint(5000,10000)
			foo2 = [' City', ' town', 'ville', 'ton', 'bur', 'port', 'y', 'dale', ' Beach', 'hill', 'rock', 'stone', 'borough', 'rapids', 'on']
			secondpart = random.choice(foo2)
		elif 28 <= k0 <= 29 :
			j = random.randint(10000,75000)
			foo2 = [' City', 'ville', 'ton', 'bur', 'port', 'y', 'dale', ' Beach', 'hill', 'rock', 'stone', 'borough', 'rapids', 'on']
			secondpart = random.choice(foo2)
		elif k0 <= 30 :
			j = random.randint(75000,160000)
			foo2 = [' City', 'ville', 'ton', 'bur', 'port', 'y', 'dale', ' Beach', 'hill', 'rock', 'stone', 'borough', 'rapids', 'on']
			secondpart = random.choice(foo2)
		else:
			j = random.randint(40,160000)
			foo2 = [' City', ' town', 'ville', 'ton', 'bur', 'port', 'y', 'dale', ' Beach', 'hill', 'rock', 'stone', 'borough', 'rapids', 'on']
			secondpart = random.choice(foo2)
	#this generates a random population
	# this is the part where we generate a name based on word parts instead of letters

	#similar to above, this determines how long the name will be. 20% of the time the name will have 4 parts instead of 3 and a 20% for a two part
	foo1 = ['Ard' ,'Ath', 'Bally', 'Bella', 'Bane', 'Begg', 'Bell', 'Bel', 'Ben', 'Bin', 'Boy', 'Brack', 'Bun', 'Cashel', 
	 'Carn', 'Carrow', 'Carry', 'Carrig', 'Carrack', 'Crai', 'Cahir', 'Clare', 'Clon', 'Com', 'Cor', 'Corry',
	 'Crough', 'Cul', 'Break', 'Derry', 'Dona','Drum', 'Duff', 'Dun', 'Doon', 'Enis', 'Esk', 'Finn', 'Fin',
 	  'Frack', 'Garf', 'Glass', 'Glen', 'Glan', 'Gorm', 'Gort', 'Ilian', 'Inish', 'Kin', 'Knock', 'Letter', 'Lis', 
	  'Lough', 'Lurgan', 'Maum', 'May', 'Mona', 'Mulla', 'More', 'Poll', 'Port', 'Rath', 'Roe', 'Ros', 'Rus', 'Sall', 'Shan', 
	  'Sheskin', 'Ske', 'Stra', 'Slieve', 'Termon', 'Tyr', 'Tubber', 'Tra', 'Taum', 'Tully', 'Knights', 'Night', 'Gale'
	  'Ar', 'Art', 'Ark', 'Jons', 'Sot', 'Ice', 'Wind', 'Shining', 'Gleam', 'Gleaming', 'Red', 'James', 'Erik', 'Boulder', 'Rapids',
	  'Cliff', 'Break']

	foo1andHalf = ['ard' ,'ath', 'bally', 'bella', 'bane', 'begg', 'bell', 'bel', 'ben', 'bin', 'boy', 'brack', 'bun', 'cashel', 
	 'carn', 'carrow', 'carry', 'carrig', 'carrack', 'crai', 'cahir', 'clare', 'clon', 'com', 'cor', 'corry',
	 'crough', 'cul', 'break', 'derry', 'dona','drum', 'duff', 'dun', 'doon', 'enis', 'esk', 'finn', 'fin',
 	  'frack', 'garf', 'glass', 'glen', 'glan', 'gorm', 'gort', 'ilian', 'inish', 'kin', 'knock', 'letter', 'lis', 
	  'lough', 'lurgan', 'maum', 'may', 'mona', 'mulla', 'more', 'poll', 'port', 'rath', 'roe', 'ros', 'rus', 'sall', 'shan', 
	  'sheskin', 'ske', 'stra', 'slieve', 'termon', 'tyr', 'tubber', 'tra', 'taum', 'tully', 'knights', 'night', 'gale'
	  'ar', 'art', 'ark', 'jons', 'sot', 'ice', 'wind', 'shining', 'gleam', 'gleaming', 'red', 'james', 'erik', 'boulder', 'rapids',
	  'cliff', 'break']

	fooNames = ['Alis', 'Aldith', 'Aldreda', 'Aldus', 'Amice', 'Dionisia', 'Diot', 'Dye', 'Eda', 'Etheldreda', 'Ethel', 'Isabel', 
	'Ibb', 'Iseut', 'Isla', 'Jocosa', 'Joyce', 'Malle', 'Mary', 'Matty', 'Meggy', 'Rohese', 'Rose', 'Ada', 'Charolette', 'Jane', 
	'T-ten' ,'Layla' ,'Jill' ,'Alison' ,'Aki' ,'Maria' ,'Lauren' ,'Elizabeth' ,'Nazia' ,'Emily' ,'Willow' ,'Xin Xin' ,'Felicity' ,
	'Ariel' ,'Aisha' ,'Manon' ,'Emma' ,'Sophia' ,'Rebekah' ,'Lisandra' ,'Pipaluk' ,'Lana' ,'Noemi' ,'Valeriya' ,'Gracie' ,'Beth' ,
	'Debbie' ,'Kara','Harley','Imogene','Olyvia','Norah','Síomha','Brielle','Etna','Ora','Audrey','Johanna','Ríonach','Sienna',
	'Randi','Prissy','Ursula','Miracle','Mindy','Kathy','Caprice','Simonette','Patsy','Cameron','Frankie','Trixie','Carly',
	'Guendolen','Fanny','Diane','Ailís','Sharron','Fíona','Pattie','Biddy','Joselyn','Johnie','Parris','Lillie','Juno','Kaylyn',
	'Kaylee','Tawnie','Siofra','Izabelle','Josceline','Jacinda','Lesia', 'Addy', 'Aldus', 'Amis', 'Bate', 'Col', 'David', 'Daw', 
	'Dicun', 'Richard', 'Elis', 'Elric', 'Etheldred', 'Hamo', 'Hankin', 'Jon', 'Henry', 'Herry', 'Hob', 'Rob', 'Jordan', 'Judd', 
	'Laurence', 'Law', 'Mack', 'Magnus', 'Nicol', 'Noll', 'Ode', 'Stace', 'Tenney', 'William', 'Wilkin', 'Wilky', 'Wilmot', 
	'Wybert', 'Wyot', 'Atreyu' ,'Bryan' ,'Zas' ,'Bigby', 'Aeron','Ívarr','Bran','Ingimárr','Leofdæg','Cyneweard','Geirr','Halli',
	'Lugos','Gunnarr','Knútr','Stígandr','Herleifr','Fedelmid','Ealdræd','Njord','Sigmundr','Hróarr','Snorri','Guðfriðr','Arnþórr',
	'Ealdwine','Oswald','Hróðólfr', 'Dagný', 'Ragnfríðr', 'Sigrún', 'Unnr', 'Myrgjöl', 'Auðrhildr', 'Signý', 'Æðelflæd', 'Bergljót',
	'Þórfríðr', 'Gyða', 'Gunnhildr', 'Siv', 'Svanhildr', 'Hjördís', 'Muirenn', 'Ragna', 'Unnr', 'Vígdís', 'Ælfswiþ', 'Ness', 'Medb', 
	'Guðrún', 'Verdandi', 'Maja', 'Henriette', 'Franka', 'Martine', 'Sibylle', 'Hanna', 'Susann', 'Fenna', 'Gertie', 'Lisa', 'Helga',
	 'Magda', 'Hedy', 'Eveline', 'Jasmijn', 'Leonie', 'Mariele', 'Charlotte', 'Michi', 'Magdalene', 'Annika', 'Helene', 'Nicole',
	  'Claudia', 'Jonathan' ,'Arjan' ,'Sven' ,'Jeppe' ,'Joord' ,'Jelle' ,'Bernhard' ,'Mikkel' ,'Wessel' ,'Leonard' ,'Hagen' ,
	  'Joachim' ,'Gillis' ,'Funske' ,'Xaver' ,'Kaj' ,'Rupert' ,'Urs' ,'Sebastian' ,'Peder' ,'Arthur' ,'Hermanus' ,'Horst' ,'Meint']

	endings = ['bach' ,'beck' ,'batch' ,'brook' ,'brooke' ,'bech' ,'beach' ,'broke' ,'bek' ,'brock' ,'bach' ,'bekk' ,'baek' ,'bec' ,
	'bais' ,'bergh' ,'berrow' ,'barrow' ,'berry' ,'berge' ,'bear' ,'berg' ,'bergen' ,'bridge' ,'brigg' ,'brugge' ,'brucken' ,'bruck' ,
	'bro' ,'bru' ,'burg' ,'bury' ,'burgh' ,'borg' ,'bourg' ,'felth' ,'field' ,'fold' ,'veld' ,'feld' ,'felde' ,'filde' ,'foort' ,'voort' ,
	'voorde' ,'ford' ,'fordt' ,'forde' ,'vorde' ,'furt' ,'forth' ,'fjorden' ,'fjord' ,'haven' ,'avon' ,'hafen' ,'hamn' ,'havm' ,'om' ,'em' ,
	'gem' ,'hem' ,'en' ,'um' ,'heim' ,'ain' ,'hope' ,'hop' ,'op' ,'hove' ,'hof' ,'hoven' ,'hove' ,'hof' ,'hoft' ,'holm' ,'holme' ,'hulme' ,
	'kirk' ,'kerk' ,'kirche' ,'church' ,'land' ,'royd' ,'rode' ,'rod' ,'rith' ,'road' ,'royde' ,'rade' ,'ray' ,'rooi' ,'rath' ,'roth' ,
	'rith' ,'rud' ,'ryd' ,'stan' ,'stam' ,'stein' ,'stone' ,'steen' ,'stein' ,'sten' ,'etan' ,'thorp' ,'thorpe' ,'throp' ,'trop' ,'thrup' ,
	'drup' ,'drop' ,'arp' ,'rup' ,'troff' ,'wich' ,'wijk' ,'wig' ,'wich' ,'wig' ,'wiek' ,'wal' ,'wall' ,'gal' ,'gaul']

	zerothPart = random.choice(foo1)
	firstPart = random.choice(foo1)
	#the generator always generates 2 variables but can choose to only use some
	x = random.randint(1,10)
	if x == 1:
		name = random.choice(foo1) + random.choice(foo1andHalf) + random.choice(foo2)
	elif x == 2:
		name = random.choice(foo1) + random.choice(foo2)
	elif 3 <= x <= 6:
		name = random.choice(foo1) + random.choice(endings)
	elif 7 <= x <= 8:
		name = random.choice(foo1) + random.choice(foo1andHalf) + random.choice(endings)
	elif x == 9:
		name = random.choice(foo1) + random.choice(foo1andHalf) + random.choice(endings) + random.choice(foo2)
	else:
		x = random.randint(0,2)
		if x == 0:
			name = random.choice(fooNames) + random.choice(foo2)
		elif x == 1:
			name = random.choice(fooNames) + random.choice(endings)
		else:
			name = random.choice(fooNames) + random.choice(endings) + random.choice(foo2)

	#this is where the generator makes a random superstition
	superstitionType = random.randint(0,3)
	if superstitionType == 0:
		superstitionPart1a = ['Eat', 'Speak about', 'Cross the path of', 'Walk near', 'Walk over', 'Jump over', 'Spot', 'Utter a word about']
		superstitionPart2a = ['a certain mushroom', 'a certain flower', 'clover', 'a bridge', 'a tunnel', 'on a farm', 'meat', 'lotus', 'cow', 'sheep', 'roses', 'the years harvest', 'a tree', '3 white butterflies', '1 yellow butterfly', 'a robin on the ground', 'a frog in the forest', 'a bear', 'a friend', 'an enemy', 'a stranger', 'a family member', 'a wolf', 'a mountain lion', 'a farm animal']	
		superstitionPart3a = ['near', 'next to', 'while eating', 'under a bed of', 'on top a of bed', 'while indoors', 'while in bed', 'on the first day of the year', 'at sunrise', 'at sunset', 'after noon', 'after dark', 'at dusk', 'during a new moon', 'during a full moon', 'while drinking', 'with your friend', 'with your sibling', 'on your birthday', 'during a feast']
		superstitionPart4a = ["and you'll put your home in danger", "and you'll meet a new friend", "and you're in for an unfortunate time", "and throw a lucky trinket over your shoulder to cancel the bad luck"]
		superstition = random.choice(superstitionPart1a) + ' ' + random.choice(superstitionPart2a) + ' ' + random.choice(superstitionPart3a) + ' ' + random.choice(superstitionPart4a)
	
	elif superstitionType == 1:
		superstitionPart1aN = ['Never eat', 'Never speak about', 'Never cross the path of', 'Never walk near', 'Never walk over', 'Never jump under', 'Never Spot', 'Never utter a word about']
		superstitionPart2aN = ['a certain mushroom', 'a certain flower', 'clover', 'a bridge', 'a tunnel', 'on a farm', 'meat', 'lotus', 'cow', 'sheep', 'roses', 'the years harvest', 'a tree', '3 white butterflies', '1 yellow butterfly', 'a robin on the ground', 'a frog in the forest', 'a bear', 'a friend', 'an enemy', 'a stranger', 'a family member', 'a wolf', 'a mountain lion', 'a farm animal']	
		superstitionPart3aN = ['while eating', 'under a bed of', 'on top a of bed', 'while indoors', 'while in bed', 'on the first day of the year', 'at sunrise', 'at sunset', 'after noon', 'after dark', 'at dusk', 'during a new moon', 'during a full moon', 'while drinking', 'with your friend', 'with your sibling', 'on your birthday', 'during a feast']
		superstition = random.choice(superstitionPart1aN) + ' ' + random.choice(superstitionPart2aN) + ' ' + random.choice(superstitionPart3aN)
	
	else:
		superstitionPart1b = ['Eating', 'Speaking about', 'Crossing the path of', 'Walking near', 'Walking over', 'Jumping over', 'Spotting', 'Uttering a word about']
		superstitionPart2b = ['a certain mushroom', 'a certain flower', 'clover', 'a bridge', 'a tunnel', 'on a farm', 'meat', 'lotus', 'cow', 'sheep', 'roses', 'the years harvest', 'a tree', '3 white butterflies', '1 yellow butterfly', 'a robin on the ground', 'a frog in the forest', 'a bear', 'a friend', 'an enemy', 'a stranger', 'a family member', 'a wolf', 'a mountain lion', 'a farm animal']	
		superstitionPart4b = ['brings good luck', 'fortells a small fortune', 'is bad luck', 'portends a happy marriage', 'causes an illness', 'will kill them', 'will cause them to appear', 'will prevent them from appearing', 'brings them good luck', 'brings them bad luck']
		superstitionPart3b = ['near', 'next to', 'while eating', 'under a bed of', 'on top a of bed', 'while indoors', 'while in bed', 'on the first day of the year', 'at sunrise', 'at sunset', 'after noon', 'after dark', 'at dusk', 'during a new moon', 'during a full moon', 'while drinking', 'with your friend', 'with your sibling', 'on your birthday', 'during a feast']
		superstition = random.choice(superstitionPart1b) + ' ' + random.choice(superstitionPart2b) + ' ' + random.choice(superstitionPart3b) + ' ' + random.choice(superstitionPart4b)

	# this part of the code lays out what random aspects a City could have
	foo3 = ['The City grew up around a coastal harbor.', 'The City grew up around a calm, coastal bay.', 'The City grew up around a large freshwater lake.', 'The City grew up around a wide navigable river.', 'The City grew up around a river navigable by small craft.', 'The City grew up around where two rivers met.', 'The City grew up around a river delta.', 'The City grew up around a series of natural springs.', 'The City grew up around a well traveled crossroads.', 'The City grew up around a water source on a well traveled road.', 'The city grew up in a valley', 'The city grew up in a shallow canyon', 'The city grew up on the beach of a series of tital ponds', 'The city grew up at the base of a mountain']
	foo4 = ['The City is near a region known for its prominent amounts of iron ore.', 'The City is near a region known for its prominent amounts of copper ore.', 'The City is near a region known for its prominent amounts of gold.', 'The City is near a region known for its prominent amounts of silver.', 'The City is near a region known for its prominent amounts of platinum.', 'The City is near a region known for its prominent amounts of electrum.', 'The City is near a region known for its prominent amounts of tin.', 'The City is near a region known for its prominent amounts of spices.', 'The City is near a region known for its prominent amounts of clay.', 'The City is near a region known for its prominent amounts of granite.', 'The City is near a region known for its prominent amounts of quarts.', 'The City is near a region known for its prominent amounts of salt.', 'The City is near a region known for its prominent amounts of peat.', 'The City is near a region known for its prominent amounts of bituminous coal.', 'The City is near a region known for its prominent amounts of anthracite coal.', 'The City is near a region known for its prominent amounts of pine trees.', 'The City is near a region known for its prominent amounts of oak trees.', 'The City is near a region known for its prominent amounts of birch trees.', 'The City is near a region known for its prominent amounts of hardwood lumber.', 'The City is near a region known for its prominent amounts of barley.', 'The City is near a region known for its prominent amounts of oats.', 'The City is near a region known for its prominent amounts of beans.', 'The City is near a region known for its prominent amounts of corn.', 'The City is near a region known for its prominent amounts of squash.', 'The City is near a region known for its prominent amounts of nuts.', 'The City is near a region known for its prominent amounts of olives.', 'The City is near a region known for its prominent amounts of rice.', 'The City is near a region known for its prominent amounts of wheat.', 'The City is near a region known for its prominent amounts of potatoes.', 'The City is near a region known for its prominent amounts of leaks.', 'The City is near a region known for its prominent amounts of sugar cane.', 'The City is near a region known for its prominent amounts of tobacco.', 'The City is near a region known for its prominent amounts of cotton.', 'The City is near a region known for its prominent amounts of grapes.', 'The City is near a region known for its prominent amounts of apples.', 'The City is near a region known for its prominent amounts of citrus fruits.', 'The City is near a region known for its prominent amounts of pears.', 'The City is near a region known for its prominent amounts of plums.', 'The City is near a region known for its prominent amounts of peaches.', 'The City is near a region known for its prominent amounts of fruit trees.', 'The City is near a region known for its prominent amounts of berries.', 'The City is near a region known for its prominent amounts of cabbage.', 'The City is near a region known for its prominent amounts of beets.', 'The City is near a region known for its prominent amounts of cattle.', 'The City is near a region known for its prominent amounts of sheep.', 'The City is near a region known for its prominent amounts of dairy cows']
	foo5 = ['The City is known for its architectural style.', 'The City is known for its architectural feats.', 'The City is known for its artists and poets.', 'The City is known for its cuisine.', 'The City is known for its suggestive dancing.', 'The City is known for its gladitorial games.', 'The City is known for its horse races.', 'The City is known for its scholars.', 'The City is known for its sages.', 'The City is known for its music.', 'The City is known for its romance.', 'The City is known for its jousting.', 'The City is known for its superior soldiers.', 'The City is known for its street festivals.', 'The City is known for its religious feasts.', 'The City is known for its reiligous fervor.', 'The City is known for its traditional dress.', 'The City is known for its theater.', 'The City is known for its wine.', 'The City is known for its ale']
	foo6 = ['The City is ruled by the head of a noble family.', 'The City is ruled by a concil of distinguished nobles.', 'The City is ruled by a council of wealthy merchants.', 'The City is ruled by a council of elected officials.', 'The City is ruled by an elected mayor.', 'The City is ruled by a benevolent sovereign.', 'The City is ruled by a wicked tyrant.', 'The City is ruled by a brutal warlord.', 'The City is ruled by a cabal of witches and wizards.', 'The City is ruled by the leaders of a religious order']
	foo7 = ['The City has experienced mass conversions.', 'The City has experienced an earthquake.', 'The City has experienced an age of exploration.', 'The City has experienced a terrible famine.', 'The City has experienced a disastrous flood.', 'The City has experienced a legendary storm.', 'The City has experienced an assassination.', 'The City has experienced a series of riots.', 'The City has experienced a serial killer.', 'The City has experienced a great discovery.', 'The City has experienced a vermin infestation.', 'The City has experienced a destructive fire.', 'The City has experienced a deadly plague.', 'The City has experienced a bloody rebellion.', 'The City has experienced a lengthy seige.', 'The City has experienced religious wars.', 'The City has experienced territorial wars.', 'The City has experienced a foreign occupation.', 'The City has experienced an economic boom.', 'The City has experienced a great depression.', 'The City has experienced a dragon attack']
	foo8 = ['The people of the City are fearful of bandits and outlaws.', 'The people of the City are fearful of barbarian invasions.', 'The people of the City are fearful of a crime lord.', 'The people of the City are fearful of disease outbreaks.', 'The people of the City are fearful of a dragon or legendary beast.', 'The people of the City are fearful of destructive flooding.', 'The people of the City are fearful of food shortages.', 'The people of the City are fearful of occupation by a foreign empire.', 'The people of the City are fearful of the wrath of a vengeful god.', 'The people of the City are fearful of magic.', 'The people of the City are fearful of new inventions.', 'The people of the City are fearful of pirates.', 'The people of the City are fearful of smugglers.', 'The people of the City are fearful of a new religion.', 'The people of the City are fearful of a rival City']
	foo9 = ['The City is defended by a disciplined military guard.', 'The City is defended by a standing army of devoted soldiers.', 'The City is defended by a company of sellswords and knaves.', 'The City is defended by an order of holy knights.', 'The City is defended by little; the City has been sacked many times.', 'The City is defended by a huge fortress within the City.', 'The City is defended by a series of watch towers and forts throughout the region.', 'The City is defended by thick stone walls.', 'The City is defended by high stone walls.', 'The City is defended by catapults, scorpions.', 'The City is defended by a powerful magical ward']
	foo10 = ['The laws are enforced by a strict, orderly City watch.', 'The laws are enforced by a corrupt roguish City watch.', 'The laws are not enforced among wealthy elite.', 'The laws are enforced in a haphazard fashion, incomrehensible to visitors.', 'The laws are not enforced by those who pay bribes.', 'The laws are more like guidelines.', 'The laws are enforced by a secret society of assassins, mages, and priests.', 'The laws are enforced by a company of mercenaries.', 'The laws are simple easy to learn and follow.', 'The laws are extensive and complicated.', 'The laws are nonsensical.', 'The laws are enforced by a cheery drunken sheriff.', 'The laws are enforced by a rigid soldier-turned sheriff']
	foo11 = ['Outside the government, power is held by a ruthless assassin guild.', 'Outside the government, power is held by a populist demagogue.', 'Outside the government, power is held by a captain of a mercenary company.', 'Outside the government, power is held by a champion knight or arena figher.', 'Outside the government, power is held by one or more crafting guilds.', 'Outside the government, power is held by a dangerous crime boss.', 'Outside the government, power is held by one or more criminal gangs.', 'Outside the government, power is held by a charismatic cult leader.', 'Outside the government, power is held by one or more merchant guilds.', 'Outside the government, power is held by a scheming noble lord or lady.', 'Outside the government, power is held by an outspoken philosopher or scholar.', 'Outside the government, power is held by a celebrated poet and playwright.', 'Outside the government, power is held by a popular priest or priestess.', 'Outside the government, power is held by a secret societty of lore keepers.', 'Outside the government, power is held by smugglers and black market dealers.', 'Outside the government, power is held by the son or daughter of a deposed foriegn ruler.', 'Outside the government, power is held by a wealthy trader of exotic goods.', 'Outside the government, power is held by a conniving vampire or fiend.', 'Outside the government, power is held by a bold war hero.', 'Outside the government, power is held by a clever witch or wizard']
	foo12 = ['dry winters', 'wet winters', 'dark winters', 'cool winters', 'cold winters', 'frigid winters', 'windy winters', 'long winters', 'short winters', 'no winterts']
	foo13 = ['dry summers', 'wet summers', 'cool summers', 'warm summers', 'hot summers', 'blistering summers', 'windy summers', 'long summers', 'short summers', 'no summers']
	foo15 = ['is unplanned', 'has an unplanned center but regulated outskirts', 'is a rough grid', 'is arranged in an H', 'has many broad avenues', 'has many back alleys', 'was planned by a master architect', 'is concentric circles', 'has few major roads']
	foo99 = ['The aurora are visible from the City.', '', 'The majority of buildings in the city are connected underground by tunnels and basements from the days it was a fort', 'The majority of buildings in the city have well furnished basements and streets underneath the ground level ones because a landslide buried most of the city.', 'Gambling and betting is seen as a part of everyday life to the populous', 'There is a city wide ban on alcohol', 'The locals have the superstition: {}'.format(superstition), 'other miscellaneous fact']

	uniqueFact = random.choice(foo99)

	#this part of the code chooses from those and assigns them to the appropriate variables
	x0 = random.choice(foo3)
	x1 = random.choice(foo4)
	x2 = random.choice(foo5)
	x3 = random.choice(foo6)
	x4 = random.choice(foo7)
	x5 = random.choice(foo8)
	x6 = random.choice(foo9)
	x7 = random.choice(foo10)
	x8 = random.choice(foo11)
	x9 = random.choice(foo12)
	x10 = random.choice(foo13)
	x11 = random.choice(foo15)

	#this is where i generate the random names for people
	#the first group are their first name, the second part is their title 
	#the last is their job
	foo17 = ['Alis', 'Aldith', 'Aldreda', 'Aldus', 'Amice', 'Dionisia', 'Diot', 'Dye', 'Eda', 'Etheldreda', 'Ethel', 'Isabel', 'Ibb', 'Iseut', 'Isla', 'Jocosa', 'Joyce', 'Malle', 'Mary', 'Matty', 'Meggy', 'Rohese', 'Rose', 'Ada', 'Charolette', 'Jane', 'T-ten' ,'Layla' ,'Jill' ,'Alison' ,'Aki' ,'Maria' ,'Lauren' ,'Elizabeth' ,'Nazia' ,'Emily' ,'Willow' ,'Xin Xin' ,'Felicity' ,'Ariel' ,'Aisha' ,'Manon' ,'Emma' ,'Sophia' ,'Rebekah' ,'Lisandra' ,'Pipaluk' ,'Lana' ,'Noemi' ,'Valeriya' ,'Gracie' ,'Beth' ,'Debbie' ,'Kara','Harley','Imogene','Olyvia','Norah','Síomha','Brielle','Etna','Ora','Audrey','Johanna','Ríonach','Sienna','Randi','Prissy','Ursula','Miracle','Mindy','Kathy','Caprice','Simonette','Patsy','Cameron','Frankie','Trixie','Carly','Guendolen','Fanny','Diane','Ailís','Sharron','Fíona','Pattie','Biddy','Joselyn','Johnie','Parris','Lillie','Juno','Kaylyn','Kaylee','Tawnie','Siofra','Izabelle','Josceline','Jacinda','Lesia']
	foo18 = ['Addy', 'Aldus', 'Amis', 'Bate', 'Col', 'David', 'Daw', 'Dicun', 'Richard', 'Elis', 'Elric', 'Etheldred', 'Hamo', 'Hankin', 'Jon', 'Henry', 'Herry', 'Hob', 'Rob', 'Jordan', 'Judd', 'Laurence', 'Law', 'Mack', 'Magnus', 'Nicol', 'Noll', 'Ode', 'Stace', 'Tenney', 'William', 'Wilkin', 'Wilky', 'Wilmot', 'Wybert', 'Wyot', 'Alex Rigopulos' ,'Mort' ,'Mortraven' ,'Steven' ,'Wai-Shing' ,'Kadreal' ,'Starger' ,'Andrew Fenn' ,'Mr Buga' ,'Borman' ,'Scott Kletzkin' ,'Fleischy' ,'Joel' ,'Shelton' ,'Tach' ,'Logan Johnson' ,'Enzo Martin' ,'Jax' ,'Jeff Baars' ,'Ohm' ,'Ihlay Caris' ,'Gumpo' ,'Zerimar' ,'Bomfy M' ,'Nekose' ,'Scoops' ,'Remo' ,'Berko' ,'Jorlack' ,'Hassifa' ,'Magmaros' ,'Butters' ,'Josh Cubbin' ,'Vitas Varnas' ,'Monsvik' ,'Grozoly' ,'Sean ORegan' ,'Tom Banks' ,'Nikmi' ,'Mullett' ,'Vivimord' ,'Craig Dolan' ,'Dre Kozar' ,'Nick Lanng' ,'Giles' ,'CY Heng' ,'Narthollis' ,'Norwyn Schultze' ,'Christoph Z ' ,'Bruce Geryk' ,'Chris Phillips' ,'Mikael Olofsson' ,'James Pomeroy' ,'Mike Weston' ,'Jason Bovee' ,'Xemu' ,'Nick Breckon' ,'Kapalka' ,'Stick' ,'Roper' ,'Frederic', 'Frederick ' ,'Henrik Aasted' ,'Firedihm ' ,'Triko' ,'Maradine ' ,'Swampson' ,'Arries' ,'Elnubnub' ,'Ken' ,'Randy Walker' ,'Declan' ,'Luaan Ti' ,'Kirkner' ,'Lombard' ,'Feras' ,'Yeoz' ,'Ryan Maniscalco' ,'GM Faux' ,'O. Williams' ,'Yevon Si' ,'Johnny Maloney' ,'Will' ,'Maxwell' ,'Thomas Bloch' ,'Rynhart' ,'Cremity' ,'AJ Hager' ,'Stephen Eckman' ,'Jan Magne' ,'Jack Shirai' ,'Julian Rafn' ,'Markand' ,'Steven Dengler' ,'Nelis' ,'Chris Malott' ,'Davion' ,'Jon Caldwell' ,'Kusy' ,'Lagardi' ,'Vincent' ,'Kevin Fish' ,'Turing' ,'Stelly' ,'Teldarin' ,'Kirby' ,'Ma Fan' ,'Jon' ,'Bjorn' ,'Justin' ,'Matt' ,'Oni' ,'Jack' ,'Markus' ,'Adnan' ,'Hector' ,'Liu Jun' ,'Jose' ,'Liam' ,'Eoin' ,'Markel' ,'Nathan' ,'Tomas' ,'Filip' ,'Nikola' ,'Maxim' ,'Artyom' ,'Mikhail' ,'Tai Yi' ,'Junpeng' ,'Steven' ,'Ferry' ,'Sem' ,'Tee Lek' ,'Matthieu' ,'King' ,'Graffin' ,'Hutz' ,'Atreyu' ,'Bryan' ,'Zas' ,'Bigby']
	namesMaleNorth = ['Aeron','Ívarr','Bran','Ingimárr','Leofdæg','Cyneweard','Geirr','Halli','Lugos','Gunnarr','Knútr','Stígandr','Herleifr','Fedelmid','Ealdræd','Njord','Sigmundr','Hróarr','Snorri','Guðfriðr','Arnþórr','Ealdwine','Oswald','Hróðólfr']
	namesFemaleNorth = ['Dagný', 'Ragnfríðr', 'Sigrún', 'Unnr', 'Myrgjöl', 'Auðrhildr', 'Signý', 'Æðelflæd', 'Bergljót', 'Þórfríðr', 'Gyða', 'Gunnhildr', 'Siv', 'Svanhildr', 'Hjördís', 'Muirenn', 'Ragna', 'Unnr', 'Vígdís', 'Ælfswiþ', 'Ness', 'Medb', 'Guðrún', 'Verdandi']
	namesFemaleHigh = ['Maja', 'Henriette', 'Franka', 'Martine', 'Sibylle', 'Hanna', 'Susann', 'Fenna', 'Gertie', 'Lisa', 'Helga', 'Magda', 'Hedy', 'Eveline', 'Jasmijn', 'Leonie', 'Mariele', 'Charlotte', 'Michi', 'Magdalene', 'Annika', 'Helene', 'Nicole', 'Claudia']
	namesMaleHigh = ['Jonathan' ,'Arjan' ,'Sven' ,'Jeppe' ,'Joord' ,'Jelle' ,'Bernhard' ,'Mikkel' ,'Wessel' ,'Leonard' ,'Hagen' ,'Joachim' ,'Gillis' ,'Funske' ,'Xaver' ,'Kaj' ,'Rupert' ,'Urs' ,'Sebastian' ,'Peder' ,'Arthur' ,'Hermanus' ,'Horst' ,'Meint']

	foo19 = ['Count ', 'Lord ', 'Mr. ', 'Master ', 'Sir']
	foo20 = ['Countess', 'Lady ', 'Mrs.', 'Ms.', 'Miss', 'Madam ']

	#these are their occupations
	agricultureJobs = ['Shepherd', 'Cowherd', 'Goatherd', 'Swinherd', 'Ackerman', 'Crofter', 'Dairymaid', 'Dung Carter', 'Gardener', 'Hawker', 'Hayward', 'Hostler', 'Tiller', 'Vintner', 'Woodcutter', 'Woolman', 'Thresher', 'Horsetrainer', 'Falconer', 'Fewterer', 'Forester', 'Fowler', 'Gamekeeper', 'Trapper', 'Hunter', 'Hawker', 'Fisherman', 'Oyster Raker', 'Seaweed Harvester']
	artistJobs = ['Artisan', 'Fresco Painter', 'Illuminator', 'Limner', 'Playwright', 'Poet', 'Writer', 'Sculptur']
	craftsmanJobs = ['Bottelier', 'Cobbler', 'Cordwainer', 'Currier', 'Girdler', 'Lorimer', 'Malemaker', 'Saddler', 'Scabbard Maker', 'Shoemaker', 'Tanner', 'Thonger', 'Vaginarius', 'Armorsmith', 'Arrowsmith', 'Blacksmith', 'Bladesmith', 'Bowyer', 'Fletcher', 'Grinder', 'Gunsmith', 'Gunstocker', 'Knifesmith', 'Lancier', 'Linen-Armorer', 'Mailmaker', 'Merchant Taylor', 'Poleturner', 'Scythesmith', 'Stringer', 'Swordsmith', 'Vaginarius', 'Weaponsmith', 'Accoutrement Maker', 'Alabasterer', 'Architect', 'Arkwright', 'Artisan', 'Baker', 'Balancemaker', 'Basketmaker', 'Beekeeper', 'Beerbrewer', 'Bellfounder', 'Bellmaker', 'Besom Maker', 'Billier', 'Bleacher', 'Blockcutter', 'Bodger', 'Bonecarver', 'Bookbinder', 'Bookprinter', 'Brazier', 'Brewer', 'Bricker', 'Bricklayer', 'Broderer', 'Broom-Dasher', 'Brushbinder', 'Builder', 'Butcher', 'Buttonmaker', 'Cabinetmaker', 'Calligrapher', 'Campaner', 'Canvasser', 'Carder', 'Cardmaker', 'Carpenter', 'Cartographer', 'Cartwright', 'Chainmaker', 'Chandler', 'Charcoalburner', 'Cheesemaker', 'Chicken Butcher', 'Clockmaker', 'Clothier', 'Coiner', 'Combmaker', 'Compasssmith', 'Confectioner', 'Cooper', 'Corsetier', 'Cutler', 'Delver', 'Diamantaire', 'Disher', 'Draper', 'Drycooper', 'Drywaller', 'Dyer', 'Embroiderer', 'Engraver', 'Fabricshearer', 'Feltmaker', 'Fewtrer', 'Fuller', 'Furniture Maker', 'Furrier', 'Gemcutter', 'Gilder', 'Glassblower', 'Glazier', 'Glover', 'Gravedigger', 'Grinder', 'Guild Master', 'Hacker', 'Harness Maker', 'Hatmaker', 'Hatter', 'Horner', 'Ivorist', 'Jeweler', 'Joiner', 'Knacker', 'Knapper', 'Lacemaker', 'Lampwright', 'Lanternmaker', 'Lapidary', 'Latoner', 'Leadworker', 'Limner', 'Linen-Armorer', 'Linener', 'Linenspinner', 'Lutemaker', 'Luthier', 'Mailer', 'Mapmaker', 'Marler', 'Marleywoman', 'Mason', 'Master Builder', 'Meat Butcher', 'Miller', 'Milliner', 'Miner', 'Miniaturist', 'Minter', 'Mintmaster', 'Moneyer', 'Mirrorer', 'Nailmaker', 'Nedeller', 'Netmaker', 'Oilmaker', 'Papermaker', 'Parchmenter', 'Pasteler', 'Pattenmaker', 'Perfumer', 'Pewterer', 'Physician', 'Pinmaker', 'Plasterer', 'Plattner', 'Plumber', 'Pointer', 'Pot Mender', 'Potter', 'Printer', 'Purser', 'Purse Maker', 'Quarryman', 'Quilter', 'Rectifier', 'Reedmaker', 'Roofer', 'Roper', 'Ropemaker', 'Rugmaker', 'Rugweaver', 'Sailmaker', 'Saltboiler', 'Salter', 'Sawyer', 'Seamstress', 'Shingler', 'Shipwright', 'Siever', 'Silkmaid', 'Silk-Dresser', 'Silk-Maker', 'Silk-Mercer', 'Silk-Dyer', 'Silk-Carder', 'Spinner', 'Stonecarver', 'Stonecutter', 'Stonemason', 'Tailor', 'Tallowchandler', 'Tapestrymaker', 'Tapicer', 'Tasseler', 'Thacker', 'Threadmaker', 'Tile-Burner', 'Tile-Theeker', 'Tile Maker', 'Treen Maker', 'Turner', 'Typefounder', 'Upholder', 'Vintner', 'Waxchandler', 'Weaver', 'Webber', 'Wheeler', 'Wheelwright', 'Wiredrawer', 'Woodcarver', 'Woodcutter', 'Woodturner']
	smithingJobs = ['Armorsmith', 'Arrowsmith', 'Blacksmith', 'Bladesmith', 'Bowyer', 'Fletcher', 'Gunsmith', 'Gunstocker', 'Knifesmith', 'Lancier', 'Linen-Armorer', 'Mailmaker', 'Merchant Taylor', 'Poleturner', 'Scythesmith', 'Stringer', 'Swordsmith', 'Vaginarius', 'Weaponsmith','Blacksmith', 'Blacksmiths Striker', 'Brightsmith', 'Bronzefounder', 'Buckle Maker', 'Coppersmith', 'Farrier', 'Foundryman', 'Goldbeater', 'Knifesmith', 'Locksmith', 'Redsmith', 'Scythesmith', 'Silversmith', 'Smelter', 'Smith', 'Swordsmith', 'Spooner', 'Spurrer', 'Tinker', 'Tinsmith, Weaponsmith']
	criminalJobs = ['Bandit', 'Boothaler', 'Burglar', 'Charlatan', 'Conman', 'Cutpurse', 'Fence (Criminal)', 'Footpad', 'Pickpocket', 'Poacher', 'Quack', 'Shill', 'Silk-Snatcher', 'Thimblerigger', 'Bawd', 'Camp Follower', 'Courtesan', 'Prostitute', 'Stewsman']
	governmentJobs = ['Ale-Conner', 'Bailiff', 'Captain Of The Guard', 'Catchpole', 'Chamberlain', 'Chancellor', 'Chancery Clerk', 'Cofferer', 'Constable', 'Diplomat', 'Emperor', 'Exchequer', 'Hayward', 'Herald', 'Jailer', 'Judge', 'Keeper Of The Privy Seal', 'Keeper Of The Rolls', 'Keeper Of The Wardrobe', 'King', 'Knight', 'Lady', 'Liner', 'Lord High Steward', 'Master Of The Revels', 'Pinder', 'Noble', 'Nobleman', 'Prince', 'Pursuivant', 'Reeve', 'Seneschal', 'Sheriff', 'Steward', 'Summoner (Law)', 'Tax Collector', 'Toll Keeper', 'Town Crier', 'Treasurer', 'Watchman', 'Woodward']
	merchantJobs = ['Acater', 'Alewife', 'Apothecary', 'Banker', 'Beer Seller', 'Boothman', 'Chapman', 'Collier', 'Colporteur', 'Costermonger', 'Drover', 'Eggler', 'Fishmonger', 'Fruiterer', 'Fruitier', 'Fueller', 'Glass Seller', 'Greengrocer', 'Grocer', 'Guild Master', 'Harberdasher', 'Hay Merchant', 'Hetheleder', 'Innkeeper', 'Ironmonger', 'Lighterman', 'Linen-Draper', 'Mercer', 'Milkmaid', 'Oil Merchant', 'Old-Clothes Dealer', 'Oynter', 'Peddler', 'Pie Seller', 'Plumer', 'Poulter', 'Ragpicker', 'Shrimper', 'Skinner', 'Spice Merchant', 'Spicer', 'Stationer', 'Taverner', 'Thresher', 'Unguentary', 'Waferer', 'Waterseller', 'Weirkeeper', 'Wine Seller', 'Wood Seller', 'Woodmonger', 'Wool Stapler']
	religionJobs = ['Abbess', 'Abbot', 'Almoner', 'Anchorite', 'Archbishop', 'Beadle', 'Beguine', 'Bishop', 'Canon', 'Cantor', 'Cardinal', 'Cathar Perfect', 'Chantry Priest', 'Chaplain', 'Clark', 'Clerk', 'Colporteur', 'Curate', 'Friar', 'Metropolitan Bishop', 'Monk', 'Nun', 'Ostiary', 'Palmer', 'Pardoner', 'Parish Priest', 'Pilgrim', 'Pope', 'Priest', 'Primate (Religion)', 'Sacristan', 'Sexton', 'Theologian']
	serviceJobs = ['Maidservant', 'Barber-Chirurgeon', 'Restaurateur', 'Water Carrier', 'Laundress', 'Porter', 'Doctor', 'Bather', 'Copyist']
	entertainmentJobs = ['Actor', 'Bard', 'Barker', 'Bear-Ward', 'Dancer', 'Fool', 'Jester', 'Juggler', 'Mummer', 'Actor', 'Playwright', 'Poet', 'Skald', 'Storyteller', 'Trobairitz', 'Troubadour', 'Tumbler']
	militaryJobs = ['Arbalestier', 'Archer', 'Argolet', 'Bodyguard', 'Bowman', 'Captain', 'Captain Of The Guard', 'Crossbowman', 'Drummer', 'Guardsman', 'Halberdier', 'Knifeman', 'Knight', 'Mercenary', 'Militia', 'Pikeman', 'Scout', 'Sergeant', 'Sergeant-At-Arms', 'Spearman', 'Spy', 'Squire, Viking', 'Watchman','Cannoneer', 'Pioneer', 'Sapper', 'Siege Engineer']
	noJobs = ['Beggar', 'Buffoon', 'Crofter', 'Gardner', 'Hermit', 'Housewife', 'Landed Gentry', 'Landlord', 'Noble', 'Pilgrim', 'Spinster', 'Tenter', 'Transient', 'Urchin', 'Vagabond']
	colonialJobs = ['Acater', 'Accipitrary', 'Accompant', 'Accoucheur', 'Accoucheus', 'Accountant', 'Accoutre', 'Accoutrement Maker', 'Ackerman', 'Actuary', 'Agent', 'Agriculturist', 'Alabasterer', 'Alchemist', 'Ale Draper', 'Ale Taster', 'Ale Tunner', 'Alewife', 'All Spice', 'Almoner', 'Almsman', 'Alnager', 'Amanuensis', 'Amber Cutter', 'Ananuensis', 'Anchor Smith', 'Anchoress', 'Anchorite', 'Ankle Beater', 'Annatto Maker', 'Antigropelos Maker', 'Anvil Smith', 'Apiariana', 'Apothecary', 'Apprentice', 'Apronman', 'Aquavita Seller', 'Arbiter', 'Archiator', 'Archivist', 'Arkwright', 'Armiger', 'Armourer', 'Arpenteur', 'Artificer', 'Artisan', 'Ashman', 'Assay Master', 'Assayer', 'Astronomer', 'Auger Maker', 'Aulnager', 'Aurifaber', 'Aurifex', 'Avenator', 'Avowry', 'Axle Tree Turner', 'Backus Boy', 'Backmaker', 'Backster', 'Badger', 'Badgy Fiddler', 'Bagman', 'Bagniokeeper', 'Bailiff', 'Bairman', 'Balancer', 'Baler', 'Ballad Monger', 'Ballast Heaver', 'Baller Up', 'Band Filer', 'Bandster', 'Bang Beggar', 'Banker', 'Banks Man', 'Banqueter', 'Barber-Chirurgeon', 'Bargeman', 'Barkeeper', 'Barker', 'Barkman', 'Barm Brewer', 'Barrel Filer', 'Bartoner', 'Basil Worker', 'Basketman', 'Bathing Machine Proprietor', 'Batman', 'Battledore Maker', 'Bawd', 'Baxter', 'Bayweaver', 'Beadle', 'Beamster', 'Beaver', 'Bedder', 'Bedman', 'Bedweaver', 'Beekeeper', 'Beeskepmaker', 'Bell Founder', 'Bell Hanger', 'Bell Ringer', 'Bellman', 'Bellowfarmer', 'Bellows Maker', 'Belly Builder', 'Bender', 'Berner', 'Besom Maker', 'Bibliothecary', 'Bid-Stand', 'Biddy', 'Bill Poster', 'Binder', 'Bird Boy', 'Bird Catcher', 'Birds Nest Seller', 'Black Borderer', 'Blacking Maker', 'Blacksmith-Armorer', 'Blacksmith', 'Bladesmith', 'Blemmere', 'Block Maker', 'Block Printer', 'Blockcutter', 'Bloodletter', 'Bloomer', 'Blower (Glass)', 'Blower (Smith)', 'Blower (Textile)', 'Bluestocking', 'Bluffer', 'Boarding Officer', 'Boardwright', 'Boatman', 'Boatswain', 'Bobber (Fisherman)', 'Bobber (Metalworker)', 'Bocher', 'Bodeys Maker', 'Bodger', 'Boiler Plater', 'Boilermaker', 'Bolter', 'Bondager', 'Bondman', 'Bone Button Turner', 'Bone Lace Maker', 'Bone Picker', 'Bonesetter', 'Boniface', 'Book Guilder', 'Bookbinder', 'Boonmaster', 'Boot Closer', 'Boot-Catcher', 'Bootbinder', 'Boothman', 'Borlera', 'Botcher', 'Bottiler', 'Bottle Boy', 'Bowler', 'Bowlman', 'Brabener', 'Brachygrapher', 'Brakesman', 'Brasiator', 'Brass Cutter', 'Brass Finisher', 'Brass Founder', 'Brayer', 'Brazier', 'Breach Maker', 'Breechesmaker', 'Brewster', 'Brickburner', 'Brickmaker', 'Brickman', 'Bridewell Keeper', 'Bridgeman', 'Brightsmith', 'Broad Cooper', 'Broadcloth Weaver', 'Brogger', 'Broiderer', 'Broom Dasher', 'Broom Squire', 'Browderer', 'Brownsmith', 'Buck Washer', 'Buckle Tongue Maker', 'Bucklesmith', 'Bullwhacker', 'Bumboat Man', 'Bunter', 'Burgomaster', 'Burler', 'Burmaiden', 'Buryeman', 'Busheler', 'Busker', 'Buss Maker', 'Butner', 'Button Burnisher', 'Cabbie', 'Cabinetmaker', 'Cad', 'Caddy Butcher', 'Cadger', 'Cainer', 'Calciner', 'Calender', 'Cambist', 'Cambric Maker', 'Camerist', 'Candler', 'Candy Man', 'Caner', 'Cannonsmith', 'Canter', 'Canting Caller', 'Canvaser', 'Cape Merchant', 'Caper', 'Captain', 'Carder', 'Cardmaker (Playing Cards)', 'Cardmaker (Wooler)', 'Carnifex', 'Carpenter-Joiner', 'Carriage Driver', 'Cart Wheeler', 'Carter', 'Cartographer', 'Cartwright', 'Castor', 'Castrator', 'Cattle Jobber', 'Caulker', 'Cellarman', 'Chafferer', 'Chaise Maker', 'Chaloner', 'Chamberlain', 'Chambermaid', 'Chambermaster', 'Chandler', 'Chanty Man', 'Chapeler', 'Chapman', 'Charcoal Burner', 'Charwoman', 'Chaser', 'Cheese Monger', 'Chiffonier', 'Chronologist', 'Civil Engineer', 'Clicker', 'Clod-Hopper', 'Clogger', 'Clothier', 'Clower', 'Coachmaker', 'Coachman', 'Coal Heaver', 'Coalman', 'Coaly', 'Cobbler', 'Cockfeeder', 'Codman', 'Cogmen', 'Coillor', 'Collar Maker', 'Collier', 'Colporteur', 'Composer', 'Coney Catcher', 'Confectioner', 'Confectionery', 'Connor', 'Cooper', 'Copeman', 'Coper', 'Coppersmith', 'Corder', 'Cordwainer', 'Cork Cutter', 'Corn Cutter', 'Costermonger', 'Cotyler', 'Couper', 'Couranteer', 'Courtier', 'Cowherd', 'Cowper', 'Cracker Boy', 'Craftiman', 'Cramer', 'Crate Man', 'Crimpet Maker', 'Crocker', 'Crofter', 'Crookmaker', 'Cropper', 'Crowner', 'Curer', 'Currier', 'Cutler', 'Dairyman', 'Damster', 'Day Laborer', 'Decoyman', 'Delver', 'Diamantaire', 'Diker', 'Dish Thrower', 'Dish Turner', 'Distiller', 'Dock Master', 'Docker', 'Doctor', 'Dog Breaker', 'Dog Leech', 'Domesman', 'Door-Keeper', 'Dowser', 'Drainer', 'Draper', 'Drawer', 'Drayman', 'Dresser', 'Dressmaker', 'Driver', 'Drover', 'Drysalter', 'Duffer', 'Dustman', 'Dyer', 'Earer', 'Eggler', 'Elymaker', 'Embosser', 'Empresario', 'Emptor', 'Engraver', 'Enumerator', 'Eremite', 'Essence Peddler', 'Etcher', 'Exciseman', 'Explorer', 'Eyer', 'Factor', 'Fagetter', 'Fanner', 'Farrier', 'Fashioner', 'Feather-Beater', 'Feather-Dresser', 'Featherman', 'Feller', 'Fellmonger', 'Felter', 'Fence Viewer', 'Ferrer', 'First Mate', 'Fish Fag', 'Flax Dresser', 'Flesher', 'Fleshmonger', 'Floater', 'Florist', 'Flusherman', 'Flying Stationer', 'Fogger', 'Foot-Boy', 'Foot-Maiden', 'Footman', 'Forestaller', 'Forger', 'Fossetmaker', 'Frame Spinner', 'Fringemaker', 'Fripperer', 'Friseur', 'Fruiterer', 'Fruitestere', 'Fulker', 'Fuller', 'Furbisher', 'Furner', 'Furrier', 'Fustian Weaver', 'Gaffer', 'Gangrel', 'Ganneker', 'Gaoler', 'Garcion', 'Gater', 'Gatward', 'Gaunter', 'Gelder', 'Gelder', 'Gilder', 'Ginour', 'Girdler', 'Glazier', 'Goldsmith', 'Goose Herd', 'Goose Herder', 'Governor', 'Grace Wife', 'Graffer', 'Grainer', 'Granger', 'Graver', 'Graverobber', 'Grazier', 'Green Grocer', 'Greensmith', 'Grenadier', 'Grinder', 'Gummer', 'Gunner', 'Gunsmith', 'Haberdasher', 'Hackner', 'Hackney Man', 'Hairweaver', 'Hand Woman', 'Harlot', 'Harper', 'Hatcheler', 'Hatcheler', 'Hatter', 'Hawker', 'Haymonger', 'Hayward', 'Hedger', 'Heelmaker', 'Henchman', 'Hewer', 'Higger', 'Highwayman', 'Hind', 'Hobbler', 'Hod', 'Hodman', 'Hoggard', 'Hooper', 'Horner', 'Horse Coper', 'Horse Courser', 'Horse Leech', 'Horse-Capper', 'Hosier', 'Hosteler', 'Hostler', 'House Joiner', 'Housewright', 'Hoyman', 'Huckster', 'Iceman', 'Infirmarian', 'Innholder', 'Intelligencer', 'Intendant', 'Interfactor', 'Iron Smith', 'Ironmaster', 'Ironmonger', 'Ivory Worker', 'Jack', 'Jacksmith', 'Jagger', 'Jakes-Farmer', 'Jobber', 'Jobmaster', 'Joiner', 'Journeyman', 'Jouster', 'Kedger', 'Keelman', 'Kempster', 'Kiddier', 'Knacker', 'Kneller', 'Knockknobbler', 'Knoller', 'Laceman', 'Lacewoman', 'Lagger', 'Land Waiter', 'Lands Jobber', 'Landsman', 'Laster', 'Lattener', 'Launderer', 'Lavendar', 'Leather Dresser', 'Leech', 'Leightonward', 'Lensgrinder', 'Lighterman', 'Limner', 'Linener', 'Linkerman', 'Lister', 'Litster', 'Loblolly Boy', 'Lock Keeper', 'Lodesman', 'Longshoreman', 'Loresman', 'Lorimer', 'Maderer', 'Malemaker', 'Malender', 'Malster', 'Manciple', 'Mangle Keeper', 'Mantuamaker', 'Mason', 'Master Mariner', 'Master Of The Rolls', 'Master', 'Matchet Forger', 'Meader', 'Mealman', 'Mechanic', 'Medicine Peddler', 'Melder', 'Menage-Man', 'Mercator', 'Mercer', 'Merchant', 'Messenger', 'Metalman', 'Meterer', 'Midshipman', 'Midwife', 'Miller', 'Milleress', 'Milliner', 'Millwright', 'Miner', 'Mint Master', 'Mintmaster', 'Mixer', 'Money-Schrivener', 'Moulder', 'Mudlark', 'Muffin Man', 'Muleskinner', 'Muleteer', 'Multurer', 'Music Teacher', 'Musiker', 'Musketeer', 'Mustarder', 'Natural Philosopher', 'Navigator', 'Navigator', 'Necessary Woman', 'Necker', 'Nedeller', 'Netter', 'Night Magistrate', 'Night Soilman', 'Nightwalker', 'Nimgimmer', 'Nob-Thatcher', 'Occupier', 'Oilman', 'Olitor', 'Orderly', 'Ordinary Keeper', 'Orfever', 'Ostler', 'Ostreger', 'Out-Crier', 'Owler', 'Packer', 'Packman', 'Paintress', 'Paling Man', 'Pan Smith', 'Panter', 'Parker', 'Passage Keeper', 'Pasteler', 'Pastor', 'Pastrycook', 'Paver', 'Pavyler', 'Pawnbroker', 'Peager', 'Pedaile', 'Peddler', 'Pelterer', 'Perchemear', 'Peregrinator', 'Perfumer', 'Periwig Maker', 'Peruker', 'Perukier', 'Pessoner', 'Peterman', 'Pettifogger', 'Petty Chapman', 'Pew Opener', 'Pharmaopoeist', 'Philosophical Instrument Maker', 'Picaroon', 'Piece Broker', 'Pigmaker', 'Pigman', 'Pikelet Maker', 'Pikeman', 'Piker', 'Pill Box Lidder', 'Piller', 'Pilot', 'Pinder', 'Piner', 'Pinner Up', 'Pinner', 'Piper', 'Pirate', 'Pitman', 'Plain Worker', 'Plaiter', 'Planker', 'Plough Jogger', 'Plowman', 'Plowright', 'Plumassier / Plumer', 'Plumbum Man', 'Pointer', 'Poleman', 'Ponderator', 'Portable Soup Maker', 'Porter', 'Post Rider', 'Postillion', 'Pot Boy', 'Potato Badger', 'Potter Carrier', 'Potter', 'Pouch Maker', 'Poulter', 'Poynter', 'Prestidigitator', 'Pricker', 'Printer (Profession)', 'Publican', 'Pugger', 'Pulleymaker', 'Pumbum', 'Pumpmaker', 'Quarrier', 'Quarryman', 'Quiller', 'Quilter', 'Quister', 'Rag And Bone Man', 'Rag Cutter', 'Rag Gatherer', 'Rag Man', 'Rag Picker', 'Ratoner', 'Rattlewatch', 'Redsmith', 'Revenuer', 'Rigger', 'Ripper', 'Riverman', 'Rodman', 'Ropemaker', 'Roper', 'Rover', 'Rugman', 'Runner', 'Rustler', 'Saddle Tree Maker', 'Saddler', 'Saloonist', 'Salter', 'Sandesman', 'Sapper', 'Sartor', 'Sawbones', 'Sawyer', 'Say Weaver', 'Sayer', 'Scavelman', 'Schoolmaster', 'Schrimpschonger', 'Scribe', 'Scrimer', 'Scripture Reader', 'Scrivener', 'Scrutineer', 'Scullery Maid', 'Scullion', 'Sea Captain', 'Sealer', 'Seamstress', 'Searcher', 'Seedsman', 'Semi Lorer', 'Sempstress', 'Sewster', 'Shanty-Man', 'Sharecropper', 'Shearer', 'Sheargrinder', 'Shearman', 'Sheath Maker', 'Sheepman', 'Shepster', 'Shingler', 'Ship Master', 'Shipwright', 'Shoe-Finder', 'Shoe-Wiper', 'Shoemaker', 'Shoesmith', 'Shoresman', 'Shrager', 'Shrieve', 'Silk Throwster', 'Silver Smith', 'Skepper', 'Skinker', 'Skinner', 'Slater', 'Slop Seller', 'Smelter', 'Smith', 'Smuggler', 'Snobber', 'Snobscat', 'Snow Warden', 'Snuffer Maker', 'Soapboiler', 'Sojourner Clothier', 'Sortor', 'Souter', 'Spallier', 'Spectaclesmaker', 'Sperviter', 'Spicer', 'Spinner', 'Splitter', 'Spooner', 'Spurrier', 'Spy', 'Stampman', 'Stapler', 'Stationary Tender', 'Stationer', 'Stay Maker', 'Steersman', 'Step Boy', 'Stevedore', 'Steward', 'Stitcher', 'Stockinger', 'Stoker', 'Stone Cutter', 'Stone Picker', 'Stone Worker', 'Stoner', 'Stonewarden', 'Straw Joiner', 'Streaker (Mortuary)', 'Street Cleaner', 'Student', 'Stuffgownsman', 'Sucksmith', 'Surveyor', 'Sutler', 'Swain', 'Swamper', 'Sweep', 'Swineherder', 'Sword Cutler', 'Tabler', 'Tailor', 'Tallow Chandler', 'Tally-Clerk', 'Tallyman', 'Tankard Bearer', 'Tanner', 'Taper Weaver', 'Tapiser', 'Tapper', 'Tapster', 'Tavern Keeper', 'Taverner', 'Tawer', 'Teamster', 'Tenter', 'Thacker', 'Thatcher', 'Theologist', 'Thresher', 'Throwster', 'Tickney Man', 'Tide Gauger', 'Tide Waiter', 'Tiemaker', 'Tiler', 'Tiller', 'Tillman', 'Tiltmaker', 'Timekeeper', 'Times Ironer', 'Tinctor', 'Tinker', 'Tinner', 'Tinsmith', 'Tinter', 'Tipper', 'Tippler', 'Tipstaff', 'Tirewoman', 'Tobacco Spinner', 'Toller', 'Tollgate Keeper', 'Tonsor', 'Tool Helver', 'Topman', 'Topsman', 'Town Crier', 'Tradesman', 'Tramper', 'Trampler', 'Tranqueter', 'Tranter', 'Traunter', 'Treen Maker', 'Treenail Maker', 'Trenchermaker', 'Trencherman', 'Truchman', 'Trugger', 'Tubber', 'Tubedrawer', 'Tunist', 'Turner', 'Turnkey', 'Upholder', 'Upholsterer', 'Upright Worker', 'Valet', 'Vatman', 'Verge Maker', 'Verrier', 'Verser', 'Victualler', 'Vintager', 'Vintner', 'Virginal Player', 'Vulcan (Profession)', 'Waferer', 'Wagoner', 'Wainwright', 'Waitman', 'Wakeman', 'Walker', 'Waller', 'Wantcatcher', 'Warden', 'Warder', 'Warper (Boating)', 'Warper (Weaving)', 'Warrener', 'Washman', 'Watch Finisher', 'Watchman', 'Water Bailiff', 'Water Carrier', 'Water Gilder', 'Water Leader', 'Waterman', 'Wattle Hurdle Maker', 'Way Man', 'Way-Maker', 'Weatherspy', 'Weaver', 'Webber', 'Webster', 'Weeder', 'Weigher', 'Well Sinker', 'Wellmaster', 'Wellwright', 'Wet Glover', 'Wet Nurse', 'Wetter', 'Whacker', 'Whaler', 'Wharfinger', 'Wheeler', 'Wheelwright', 'Wheeryman', 'Whipcord Maker', 'Whipperin', 'Whit Cooper', 'White Limer', 'White Smith', 'White Tawer', 'Whitear', 'Whitener', 'Whitening Roll Maker', 'Whitesmith', 'Whitewing', 'Whittawer', 'Wigmaker', 'Willow Plaiter', 'Winder', 'Windster', 'Wire Drawer', 'Wood Reeve', 'Woodbreaker', 'Woodranger', 'Wool Driver', 'Wool Grower', 'Wool Sorter', 'Wool Winder', 'Woolcomber', 'Woolsted Man', 'Worsted Manufacturer', 'Wright', 'Yardman', 'Yatman', 'Yearman']
	
	#now the generator is going to generate random amounts of professions for the City
	randomJobs = ['Shepherd', 'Cowherd', 'Goatherd', 'Swinherd', 'Ackerman', 'Crofter', 'Dairymaid', 'Dung Carter', 'Gardener', 'Hawker', 'Hayward', 'Hostler', 'Tiller', 'Vintner', 'Woodcutter', 'Woolman', 'Thresher', 'Horsetrainer', 'Falconer', 'Fewterer', 'Forester', 'Fowler', 'Gamekeeper', 'Trapper', 'Hunter', 'Hawker', 'Fisherman', 'Oyster Raker', 'Seaweed Harvester', 'Artisan', 'Fresco Painter', 'Illuminator', 'Limner', 'Playwright', 'Poet', 'Writer', 'Sculptur', 'Bottelier', 'Cobbler', 'Cordwainer', 'Currier', 'Girdler', 'Lorimer', 'Malemaker', 'Saddler', 'Scabbard Maker', 'Shoemaker', 'Tanner', 'Thonger', 'Vaginarius', 'Armorsmith', 'Arrowsmith', 'Blacksmith', 'Bladesmith', 'Bowyer', 'Fletcher', 'Grinder', 'Gunsmith', 'Gunstocker', 'Knifesmith', 'Lancier', 'Linen-Armorer', 'Mailmaker', 'Merchant Taylor', 'Poleturner', 'Scythesmith', 'Stringer', 'Swordsmith', 'Vaginarius', 'Weaponsmith', 'Accoutrement Maker', 'Alabasterer', 'Architect', 'Arkwright', 'Artisan', 'Baker', 'Balancemaker', 'Basketmaker', 'Beekeeper', 'Beerbrewer', 'Bellfounder', 'Bellmaker', 'Besom Maker', 'Billier', 'Bleacher', 'Blockcutter', 'Bodger', 'Bonecarver', 'Bookbinder', 'Bookprinter', 'Brazier', 'Brewer', 'Bricker', 'Bricklayer', 'Broderer', 'Broom-Dasher', 'Brushbinder', 'Builder', 'Butcher', 'Buttonmaker', 'Cabinetmaker', 'Calligrapher', 'Campaner', 'Canvasser', 'Carder', 'Cardmaker', 'Carpenter', 'Cartographer', 'Cartwright', 'Chainmaker', 'Chandler', 'Charcoalburner', 'Cheesemaker', 'Chicken Butcher', 'Clockmaker', 'Clothier', 'Coiner', 'Combmaker', 'Compasssmith', 'Confectioner', 'Cooper', 'Corsetier', 'Cutler', 'Delver', 'Diamantaire', 'Disher', 'Draper', 'Drycooper', 'Drywaller', 'Dyer', 'Embroiderer', 'Engraver', 'Fabricshearer', 'Feltmaker', 'Fewtrer', 'Fuller', 'Furniture Maker', 'Furrier', 'Gemcutter', 'Gilder', 'Glassblower', 'Glazier', 'Glover', 'Gravedigger', 'Grinder', 'Guild Master', 'Hacker', 'Harness Maker', 'Hatmaker', 'Hatter', 'Horner', 'Ivorist', 'Jeweler', 'Joiner', 'Knacker', 'Knapper', 'Lacemaker', 'Lampwright', 'Lanternmaker', 'Lapidary', 'Latoner', 'Leadworker', 'Limner', 'Linen-Armorer', 'Linener', 'Linenspinner', 'Lutemaker', 'Luthier', 'Mailer', 'Mapmaker', 'Marler', 'Marleywoman', 'Mason', 'Master Builder', 'Meat Butcher', 'Miller', 'Milliner', 'Miner', 'Miniaturist', 'Minter', 'Mintmaster', 'Moneyer', 'Mirrorer', 'Nailmaker', 'Nedeller', 'Netmaker', 'Oilmaker', 'Papermaker', 'Parchmenter', 'Pasteler', 'Pattenmaker', 'Perfumer', 'Pewterer', 'Physician', 'Pinmaker', 'Plasterer', 'Plattner', 'Plumber', 'Pointer', 'Pot Mender', 'Potter', 'Printer', 'Purser', 'Purse Maker', 'Quarryman', 'Quilter', 'Rectifier', 'Reedmaker', 'Roofer', 'Roper', 'Ropemaker', 'Rugmaker', 'Rugweaver', 'Sailmaker', 'Saltboiler', 'Salter', 'Sawyer', 'Seamstress', 'Shingler', 'Shipwright', 'Siever', 'Silkmaid', 'Silk-Dresser', 'Silk-Maker', 'Silk-Mercer', 'Silk-Dyer', 'Silk-Carder', 'Spinner', 'Stonecarver', 'Stonecutter', 'Stonemason', 'Tailor', 'Tallowchandler', 'Tapestrymaker', 'Tapicer', 'Tasseler', 'Thacker', 'Threadmaker', 'Tile-Burner', 'Tile-Theeker', 'Tile Maker', 'Treen Maker', 'Turner', 'Typefounder', 'Upholder', 'Vintner', 'Waxchandler', 'Weaver', 'Webber', 'Wheeler', 'Wheelwright', 'Wiredrawer', 'Woodcarver', 'Woodcutter', 'Woodturner', 'Armorsmith', 'Arrowsmith', 'Blacksmith', 'Bladesmith', 'Bowyer', 'Fletcher', 'Gunsmith', 'Gunstocker', 'Knifesmith', 'Lancier', 'Linen-Armorer', 'Mailmaker', 'Merchant Taylor', 'Poleturner', 'Scythesmith', 'Stringer', 'Swordsmith', 'Vaginarius', 'Weaponsmith','Blacksmith', 'Blacksmiths Striker', 'Brightsmith', 'Bronzefounder', 'Buckle Maker', 'Coppersmith', 'Farrier', 'Foundryman', 'Goldbeater', 'Knifesmith', 'Locksmith', 'Redsmith', 'Scythesmith', 'Silversmith', 'Smelter', 'Smith', 'Swordsmith', 'Spooner', 'Spurrer', 'Tinker', 'Tinsmith, Weaponsmith', 'Bandit', 'Boothaler', 'Burglar', 'Charlatan', 'Conman', 'Cutpurse', 'Fence (Criminal)', 'Footpad', 'Pickpocket', 'Poacher', 'Quack', 'Shill', 'Silk-Snatcher', 'Thimblerigger', 'Bawd', 'Camp Follower', 'Courtesan', 'Prostitute', 'Stewsman', 'Ale-Conner', 'Bailiff', 'Captain Of The Guard', 'Catchpole', 'Chamberlain', 'Chancellor', 'Chancery Clerk', 'Cofferer', 'Constable', 'Diplomat', 'Emperor', 'Exchequer', 'Hayward', 'Herald', 'Jailer', 'Judge', 'Keeper Of The Privy Seal', 'Keeper Of The Rolls', 'Keeper Of The Wardrobe', 'King', 'Knight', 'Lady', 'Liner', 'Lord High Steward', 'Master Of The Revels', 'Pinder', 'Noble', 'Nobleman', 'Prince', 'Pursuivant', 'Reeve', 'Seneschal', 'Sheriff', 'Steward', 'Summoner (Law)', 'Tax Collector', 'Toll Keeper', 'Town Crier', 'Treasurer', 'Watchman', 'Woodward', 'Acater', 'Alewife', 'Apothecary', 'Banker', 'Beer Seller', 'Boothman', 'Chapman', 'Collier', 'Colporteur', 'Costermonger', 'Drover', 'Eggler', 'Fishmonger', 'Fruiterer', 'Fruitier', 'Fueller', 'Glass Seller', 'Greengrocer', 'Grocer', 'Guild Master', 'Harberdasher', 'Hay Merchant', 'Hetheleder', 'Innkeeper', 'Ironmonger', 'Lighterman', 'Linen-Draper', 'Mercer', 'Milkmaid', 'Oil Merchant', 'Old-Clothes Dealer', 'Oynter', 'Peddler', 'Pie Seller', 'Plumer', 'Poulter', 'Ragpicker', 'Shrimper', 'Skinner', 'Spice Merchant', 'Spicer', 'Stationer', 'Taverner', 'Thresher', 'Unguentary', 'Waferer', 'Waterseller', 'Weirkeeper', 'Wine Seller', 'Wood Seller', 'Woodmonger', 'Wool Stapler', 'Abbess', 'Abbot', 'Almoner', 'Anchorite', 'Archbishop', 'Beadle', 'Beguine', 'Bishop', 'Canon', 'Cantor', 'Cardinal', 'Cathar Perfect', 'Chantry Priest', 'Chaplain', 'Clark', 'Clerk', 'Colporteur', 'Curate', 'Friar', 'Metropolitan Bishop', 'Monk', 'Nun', 'Ostiary', 'Palmer', 'Pardoner', 'Parish Priest', 'Pilgrim', 'Pope', 'Priest', 'Primate (Religion)', 'Sacristan', 'Sexton', 'Theologian', 'Maidservant', 'Barber-Chirurgeon', 'Restaurateur', 'Water Carrier', 'Laundress', 'Porter', 'Doctor', 'Bather', 'Copyist', 'Actor', 'Bard', 'Barker', 'Bear-Ward', 'Dancer', 'Fool', 'Jester', 'Juggler', 'Mummer', 'Actor', 'Playwright', 'Poet', 'Skald', 'Storyteller', 'Trobairitz', 'Troubadour', 'Tumbler', 'Arbalestier', 'Archer', 'Argolet', 'Bodyguard', 'Bowman', 'Captain', 'Captain Of The Guard', 'Crossbowman', 'Drummer', 'Guardsman', 'Halberdier', 'Knifeman', 'Knight', 'Mercenary', 'Militia', 'Pikeman', 'Scout', 'Sergeant', 'Sergeant-At-Arms', 'Spearman', 'Spy', 'Squire, Viking', 'Watchman','Cannoneer', 'Pioneer', 'Sapper', 'Siege Engineer']
	numberOfJobs = random.randint(0,7)
	randomJobsNumber = [.0001, .0002, .0003, .0004, .0005, .0006, .00066, .0007, .00075, .0008, .0009, .001, .002, .003, .004, .005, .006, .007, .008, .009, .01, .015, .02, .033, .035, .03, .04, .045, .05, .075, .06, .08, .066, .025, .055, .065, .085, .09, .012, .013, .014, .021, .022, .023, .024]
	if numberOfJobs == 0:
		job0, job1, job2, job3, job4 = random.sample(randomJobs, 5)
		job0n, job1n, job2n, job3n, job4n = random.sample(randomJobsNumber, 5)
			
		job0n = str(int(round(job0n * j,0) + 1))
		job1n = str(int(round(job1n * j,0) + 1))
		job2n = str(int(round(job2n * j,0) + 1))
		job3n = str(int(round(job3n * j,0) + 1))
		job4n = str(int(round(job4n * j,0) + 1))

		jobsPrintValue = 'Notable professions in the City are the ' + '\n' + str(job0n) + ' ' + str(job0) + 's' + '\n' + str(job1n) + ' ' + str(job1) + 's' + '\n' + str(job2n) + ' ' + str(job2) + 's' + '\n' + str(job3n) + ' ' + str(job3) + 's' + '\n' + str(job4n) + ' ' + str(job4) + 's'

	elif numberOfJobs == 1:
		job0, job1, job2, job3, job4, job5 = random.sample(randomJobs, 6)
		job0n, job1n, job2n, job3n, job4n, job5n = random.sample(randomJobsNumber, 6)
			
		job0n = str(int(round(job0n * j,0) + 1))
		job1n = str(int(round(job1n * j,0) + 1))
		job2n = str(int(round(job2n * j,0) + 1))
		job3n = str(int(round(job3n * j,0) + 1))
		job4n = str(int(round(job4n * j,0) + 1))
		job5n = str(int(round(job5n * j,0) + 1))

		jobsPrintValue = 'Notable professions in the City are the ' + '\n' +  str(job0n) + ' ' + str(job0) + 's' + '\n' + str(job1n) + ' ' + str(job1) + 's' + '\n' + str(job2n) + ' ' + str(job2) + 's' + '\n' + str(job3n) + ' ' + str(job3) + 's' + '\n' + str(job4n) + ' ' + str(job4) + 's' + '\n' + str(job5n) + ' ' + str(job5) + 's'

	elif numberOfJobs == 2:
		job0, job1, job2, job3, job4, job5, job6, job7 = random.sample(randomJobs, 8)
		job0n, job1n, job2n, job3n, job4n, job5n, job6n, job7n = random.sample(randomJobsNumber, 8)
			
		job0n = str(int(round(job0n * j,0) + 1))
		job1n = str(int(round(job1n * j,0) + 1))
		job2n = str(int(round(job2n * j,0) + 1))
		job3n = str(int(round(job3n * j,0) + 1))
		job4n = str(int(round(job4n * j,0) + 1))
		job5n = str(int(round(job5n * j,0) + 1))
		job6n = str(int(round(job6n * j,0) + 1))
		job7n = str(int(round(job7n * j,0) + 1))

		jobsPrintValue = 'Notable professions in the City are the ' + '\n' +  str(job0n) + ' ' + str(job0) + 's' + '\n' + str(job1n) + ' ' + str(job1) + 's' + '\n' + str(job2n) + ' ' + str(job2) + 's' + '\n' + str(job3n) + ' ' + str(job3) + 's' + '\n' + str(job4n) + ' ' + str(job4) + 's' + '\n' + str(job5n) + ' ' + str(job5) + 's' + '\n' + str(job6n) + ' ' + str(job6) + 's' + '\n' + str(job7n) + ' ' + str(job7) + 's'

	elif numberOfJobs == 3:
		job0, job1, job2, job3, job4, job5, job6, job7, job8, job9 = random.sample(randomJobs, 10)
		job0n, job1n, job2n, job3n, job4n, job5n, job6n, job7n, job8n, job9n = random.sample(randomJobsNumber, 10)
			
		job0n = str(int(round(job0n * j,0) + 1))
		job1n = str(int(round(job1n * j,0) + 1))
		job2n = str(int(round(job2n * j,0) + 1))
		job3n = str(int(round(job3n * j,0) + 1))
		job4n = str(int(round(job4n * j,0) + 1))
		job5n = str(int(round(job5n * j,0) + 1))
		job6n = str(int(round(job6n * j,0) + 1))
		job7n = str(int(round(job7n * j,0) + 1))
		job8n = str(int(round(job8n * j,0) + 1))
		job9n = str(int(round(job9n * j,0) + 1))

		jobsPrintValue = 'Notable professions in the City are the ' + '\n' +  str(job0n) + ' ' + str(job0) + 's' + '\n' + str(job1n) + ' ' + str(job1) + 's' + '\n' + str(job2n) + ' ' + str(job2) + 's' + '\n' + str(job3n) + ' ' + str(job3) + 's' + '\n' + str(job4n) + ' ' + str(job4) + 's' + '\n' + str(job5n) + ' ' + str(job5) + 's' + '\n' + str(job6n) + ' ' + str(job6) + 's' + '\n' + str(job7n) + ' ' + str(job7) + 's' + '\n' + str(job8n) + ' ' + str(job8) + 's' + '\n' + str(job9n) + ' ' + str(job9) + 's'

	elif numberOfJobs == 4:
		job0, job1, job2, job3, job4, job5, job6, job7, job8, job9, job10 = random.sample(randomJobs, 11)
		job0n, job1n, job2n, job3n, job4n, job5n, job6n, job7n, job8n, job9n, job10n = random.sample(randomJobsNumber, 11)
			
		job0n = str(int(round(job0n * j,0) + 1))
		job1n = str(int(round(job1n * j,0) + 1))
		job2n = str(int(round(job2n * j,0) + 1))
		job3n = str(int(round(job3n * j,0) + 1))
		job4n = str(int(round(job4n * j,0) + 1))
		job5n = str(int(round(job5n * j,0) + 1))
		job6n = str(int(round(job6n * j,0) + 1))
		job7n = str(int(round(job7n * j,0) + 1))
		job8n = str(int(round(job8n * j,0) + 1))
		job9n = str(int(round(job9n * j,0) + 1))
		job10n = str(int(round(job10n * j,0) + 1))

		jobsPrintValue = 'Notable professions in the City are the ' + '\n' +  str(job0n) + ' ' + str(job0) + 's' + '\n' + str(job1n) + ' ' + str(job1) + 's' + '\n' + str(job2n) + ' ' + str(job2) + 's' + '\n' + str(job3n) + ' ' + str(job3) + 's' + '\n' + str(job4n) + ' ' + str(job4) + 's' + '\n' + str(job5n) + ' ' + str(job5) + 's' + '\n' + str(job6n) + ' ' + str(job6) + 's' + '\n' + str(job7n) + ' ' + str(job7) + 's' + '\n' + str(job8n) + ' ' + str(job8) + 's' + '\n' + str(job9n) + ' ' + str(job9) + 's' + '\n' + str(job10n) + ' ' + str(job10) + 's'
	
	elif numberOfJobs == 5:
		job0, job1, job2, job3, job4, job5, job6, job7, job8, job9, job10, job11, job12 = random.sample(randomJobs, 13)
		job0n, job1n, job2n, job3n, job4n, job5n, job6n, job7n, job8n, job9n, job10n, job11n, job12n = random.sample(randomJobsNumber, 13)
			
		job0n = str(int(round(job0n * j,0) + 1))
		job1n = str(int(round(job1n * j,0) + 1))
		job2n = str(int(round(job2n * j,0) + 1))
		job3n = str(int(round(job3n * j,0) + 1))
		job4n = str(int(round(job4n * j,0) + 1))
		job5n = str(int(round(job5n * j,0) + 1))
		job6n = str(int(round(job6n * j,0) + 1))
		job7n = str(int(round(job7n * j,0) + 1))
		job8n = str(int(round(job8n * j,0) + 1))
		job9n = str(int(round(job9n * j,0) + 1))
		job10n = str(int(round(job10n * j,0) + 1))
		job11n = str(int(round(job11n * j,0) + 1))
		job12n = str(int(round(job12n * j,0) + 1))

		jobsPrintValue = 'Notable professions in the City are the ' + '\n' +  str(job0n) + ' ' + str(job0) + 's' + '\n' + str(job1n) + ' ' + str(job1) + 's' + '\n' + str(job2n) + ' ' + str(job2) + 's' + '\n' + str(job3n) + ' ' + str(job3) + 's' + '\n' + str(job4n) + ' ' + str(job4) + 's' + '\n' + str(job5n) + ' ' + str(job5) + 's' + '\n' + str(job6n) + ' ' + str(job6) + 's' + '\n' + str(job7n) + ' ' + str(job7) + 's' + '\n' + str(job8n) + ' ' + str(job8) + 's' + '\n' + str(job9n) + ' ' + str(job9) + 's' + '\n' + str(job10n) + ' ' + str(job10) + 's' + '\n' + str(job11n) + ' ' + str(job11) + 's' + '\n' + str(job12n) + ' ' + str(job12) + 's'

	
	elif numberOfJobs == 6:
		job0, job1, job2, job3, job4, job5, job6, job7, job8, job9, job10, job11, job12, job13, job14, job15 = random.sample(randomJobs, 16)
		job0n, job1n, job2n, job3n, job4n, job5n, job6n, job7n, job8n, job9n, job10n, job11n, job12n, job13n, job14n, job15n = random.sample(randomJobsNumber, 16)
		
		job0n = str(int(round(job0n * j,0) + 1))
		job1n = str(int(round(job1n * j,0) + 1))
		job2n = str(int(round(job2n * j,0) + 1))
		job3n = str(int(round(job3n * j,0) + 1))
		job4n = str(int(round(job4n * j,0) + 1))
		job5n = str(int(round(job5n * j,0) + 1))
		job6n = str(int(round(job6n * j,0) + 1))
		job7n = str(int(round(job7n * j,0) + 1))
		job8n = str(int(round(job8n * j,0) + 1))
		job9n = str(int(round(job9n * j,0) + 1))
		job10n = str(int(round(job10n * j,0) + 1))
		job11n = str(int(round(job11n * j,0) + 1))
		job12n = str(int(round(job12n * j,0) + 1))
		job13n = str(int(round(job13n * j,0) + 1))
		job14n = str(int(round(job14n * j,0) + 1))
		job15n = str(int(round(job15n * j,0) + 1))

		jobsPrintValue = 'Notable professions in the City are the ' + '\n' +  str(job0n) + ' ' + str(job0) + 's' + '\n' + str(job1n) + ' ' + str(job1) + 's' + '\n' + str(job2n) + ' ' + str(job2) + 's' + '\n' + str(job3n) + ' ' + str(job3) + 's' + '\n' + str(job4n) + ' ' + str(job4) + 's' + '\n' + str(job5n) + ' ' + str(job5) + 's' + '\n' + str(job6n) + ' ' + str(job6) + 's' + '\n' + str(job7n) + ' ' + str(job7) + 's' + '\n' + str(job8n) + ' ' + str(job8) + 's' + '\n' + str(job9n) + ' ' + str(job9) + 's' + '\n' + str(job10n) + ' ' + str(job10) + 's' + '\n' + str(job11n) + ' ' + str(job11) + 's' + '\n' + str(job12n) + ' ' + str(job12) + 's' + '\n' + str(job13n) + ' ' + str(job13) + 's' + '\n' + str(job14n) + ' ' + str(job14) + 's' + '\n' + str(job15n) + ' ' + str(job15) + 's'
	
	else:
		job0, job1, job2 = random.sample(randomJobs, 3)
		job0n, job1n, job2n = random.sample(randomJobsNumber, 3)
		
		job0n = str(int(round(job0n * j,0) + 1))
		job1n = str(int(round(job1n * j,0) + 1))
		job2n = str(int(round(job2n * j,0) + 1))
		jobsPrintValue = 'Notable professions in the City are the ' + '\n' +  str(job0n) + ' ' + str(job0) + 's' + '\n' + str(job1n) + ' ' + str(job1) + 's' + '\n' + str(job2n) + ' ' + str(job2) + 's'
		
	#now the generator is going to make a random local. it starts be choosing their gender. 0 for girl, 1 for boy
	localGender = random.randint(0,1)
	if localGender == 0:
		localNameType = random.randint(0,2)
		if localNameType == 0:
			localName = random.choice(foo17)
			#now it's going to see if she gets a title
			hasTitle = random.randint(0,25)
			if hasTitle == 0:
				localTitle = random.choice(foo20)
				localFullName = localTitle, localName 
			else:
				fuckIt = 0
			localFullName = localName 
		elif localNameType == 1:
			localName = random.choice(namesFemaleNorth)
			#now it's going to see if she gets a title
			hasTitle = random.randint(0,25)
			if hasTitle == 0:
				localTitle = random.choice(foo20)
				localFullName = localTitle, localName 
			else:
				fuckIt = 0
			localFullName = localName 
		else:
			localName = random.choice(namesFemaleHigh)
			#now it's going to see if she gets a title
			hasTitle = random.randint(0,25)
			if hasTitle == 0:
				localTitle = random.choice(foo20)
				localFullName = localTitle, localName 
			else:
				fuckIt = 0
			localFullName = localName
	else:
		localNameType = random.randint(0,2)
		if localNameType == 0:
			localName = random.choice(foo18)
			#now it's going to see if she gets a title
			hasTitle = random.randint(0,25)
			if hasTitle == 0:
				localTitle = random.choice(foo19)
				localFullName = localTitle, localName 
			else:
				fuckIt = 0
			localFullName = localName 
		elif localNameType == 1:
			localName = random.choice(namesMaleNorth)
			#now it's going to see if she gets a title
			hasTitle = random.randint(0,25)
			if hasTitle == 0:
				localTitle = random.choice(foo19)
				localFullName = localTitle, localName 
			else:
				fuckIt = 0
			localFullName = localName 
		else:
			localName = random.choice(namesMaleHigh)
			#now it's going to see if she gets a title
			hasTitle = random.randint(0,25)
			if hasTitle == 0:
				localTitle = random.choice(foo19)
				localFullName = localTitle, localName 
			else:
				fuckIt = 0
			localFullName = localName
	
	#now the generator will pick a random number from 0 to 12 to choose what professions they will be
	jobType = random.randint(0,12)
	if jobType == 0:
		localJob = random.choice(agricultureJobs)
	elif jobType == 1:
		localJob = random.choice(artistJobs)
	elif jobType == 2:
		localJob = random.choice(craftsmanJobs)
	elif jobType == 3:
		localJob = random.choice(smithingJobs)
	elif jobType == 4:
		localJob = random.choice(criminalJobs)
	elif jobType == 5:
		localJob = random.choice(governmentJobs)
	elif jobType == 6:
		localJob = random.choice(merchantJobs)
	elif jobType == 7:
		localJob = random.choice(religionJobs)
	elif jobType == 8:
		localJob = random.choice(serviceJobs)
	elif jobType == 9:
		localJob = random.choice(entertainmentJobs)
	elif jobType == 10:
		localJob = random.choice(militaryJobs)
	elif jobType == 11:
		localJob = random.choice(militaryJobs)
	else:
		localJob = random.choice(noJobs)
	#now it chooses an interesting fact about them
	localFactList = [' has a family history in this City since its founding', ' is leader of a secret society', ' is the richest landlord in the City', ' is having an affair with 3 other people', ' is cheating on their spouse', ' is investigating a robbery', ' is investigating a murder', ' is secretly a serial killer', ' has the largest family in town', ' likes pie', ' owns a share in almost all businesses in their profession', ' is a bastard and proud', ' is a bastard', ' is responsible for a cover up', ' spends their spare time hanging out at the pier', ' has no spare time and devotes themselves to their work', ' is not very sociable', ' is the talk of the town', ' designed all of the City architecture', ' has a secret base in the sewer', ' desgined the sewer', ' heard a rumor of a ghost in the windmill', ' heard a rumor of a ghost in the sewers', ' heard a rumor of a ghost in the horse stables', ' heard a rumor of a ghost in the nearest tavern', ' heard a rumor that the leader of the City is actually dead', ' heard a rumor that the banks in the City actually have no money', ' heard a rumor of a zombie in the windmill', ' heard a rumor of a zombie in the sewers', ' heard a rumor of a zombie in the horse stables', ' heard a rumor of a zombie in the nearest tavern', ' is very skilled at their craft' ]
	localFact = random.choice(localFactList)

	#now it will generate random locals without jobs but different descriptions
	local2Gender = random.randint(0,1)
	if local2Gender == 0:
		local2Name = random.choice(foo17)
		#now it's going to see if she gets a title
		hasTitle = random.randint(0,25)
		if hasTitle == 0:
			local2Title = random.choice(foo20)
			local2FullName = local2Title, local2Name 
		else:
			fuckIt = 0
		local2FullName = local2Name 
	else:
		local2Name = random.choice(foo18)
		#now it's going to see if he gets a title
		hasTitle = random.randint(0,25)
		if hasTitle == 0:
			local2Title = random.choice(foo19)
			local2FullName = local2Title, local2Name 
		else:
			fuckIt = 0
		local2FullName = local2Name 
	#now the generator will pick a random number from 0 to 12 to choose what professions they will be
	job2Type = random.randint(0,12)
	if job2Type == 0:
		local2Job = random.choice(agricultureJobs)
	elif job2Type == 1:
		local2Job = random.choice(artistJobs)
	elif job2Type == 2:
		local2Job = random.choice(craftsmanJobs)
	elif job2Type == 3:
		local2Job = random.choice(smithingJobs)
	elif job2Type == 4:
		local2Job = random.choice(criminalJobs)
	elif job2Type == 5:
		local2Job = random.choice(governmentJobs)
	elif job2Type == 6:
		local2Job = random.choice(merchantJobs)
	elif job2Type == 7:
		local2Job = random.choice(religionJobs)
	elif job2Type == 8:
		local2Job = random.choice(serviceJobs)
	elif job2Type == 9:
		local2Job = random.choice(entertainmentJobs)
	elif job2Type == 10:
		local2Job = random.choice(militaryJobs)
	elif job2Type == 11:
		local2Job = random.choice(militaryJobs)
	else:
		local2Job = random.choice(noJobs)
	#now it chooses an interesting fact about them
	local2FactList = [' has a family history in this City since its founding', ' is leader of a secret society', ' is the richest landlord in the City', ' is having an affair with 3 other people', ' is cheating on their spouse', ' is investigating a robbery', ' is investigating a murder', ' is secretly a serial killer', ' has the largest family in town', ' likes pie', ' owns a share in almost all businesses in their profession', ' is a bastard and proud', ' is a bastard', ' is responsible for a cover up', ' spends their spare time hanging out at the pier', ' has no spare time and devotes themselves to their work', ' is not very sociable', ' is the talk of the town', ' designed all of the City architecture', ' has a secret base in the sewer', ' desgined the sewer', ' heard a rumor of a ghost in the windmill', ' heard a rumor of a ghost in the sewers', ' heard a rumor of a ghost in the horse stables', ' heard a rumor of a ghost in the nearest tavern', ' heard a rumor that the leader of the City is actually dead', ' heard a rumor that the banks in the City actually have no money', ' heard a rumor of a zombie in the windmill', ' heard a rumor of a zombie in the sewers', ' heard a rumor of a zombie in the horse stables', ' heard a rumor of a zombie in the nearest tavern', ' is very skilled at their craft' ]
	local2Fact = random.choice(local2FactList)
	

	#this is where i want to generate random percentages for the races that inhabit the City
	humans = random.randint(25,70)
	mixed = random.randint(10,35)
	dwarves = random.randint(5,50)
	elves = random.randint(1,15)
	kobolds = random.randint(0,3)

	#now i'm totaling thing
	totalInhabitants = (humans + mixed + dwarves + elves + kobolds)

	#now i'm finding the percentages
	f0 = humans/totalInhabitants*100
	g0 = mixed/totalInhabitants*100
	h0 = dwarves/totalInhabitants*100
	i0 = elves/totalInhabitants*100
	j0 = kobolds/totalInhabitants*100

	#now i'm finding the raw number for each race within the City
	f1 = humans/totalInhabitants*j
	g1 = mixed/totalInhabitants*j
	h1 = dwarves/totalInhabitants*j
	i1 = elves/totalInhabitants*j
	j1 = kobolds/totalInhabitants*j

	#this is where the age of the City is generated
	foo16 = [1337, 2337, 1000, 2000, 4000, 500]
	baseCityAge = 80
	cityAgeVariant = random.betavariate(2,5) * random.choice(foo16)
	cityAge = int(round(baseCityAge + cityAgeVariant,0))

	#TESTING DO NOT KEEP IN
	if iteration % 20 == 0:
		timeSecond = time.time()
		timeElapsed = (timeSecond - timeInitial)
		timeEstimate = round((timeElapsed * (times - iteration) / 5))
		timeInitial = time.time()

	#this is where it chooses how many facts to give about the City
	z = random.randint(2,6)

	foo14 = [x0, x1, x2, x3, x4, x5, x6, x7, x8]

	if z == 2:
		fact0, fact1 = random.sample(foo14, 2)

		with open("Cities.txt", "a") as text_file:
			print(name, ' Pop:',j, file=text_file)
			print("-----------------------------", file=text_file)
			print(fact0, fact1, file=text_file)
			print(uniqueFact, file=text_file)
			print('-----------------------------' +
				'\n' 'It has' ,x10 + ' and' ,x9 + 
				'\n' + 'Its street layout',x11 +
				'\n' + 'The City was founded {} years ago'.format(cityAge) + '\n' + '-----------------------------' +
				'\n' + 'A local {}'.format(localJob), 'named {}'.format(localFullName) + '{}'.format(localFact) +
				'\n' + 'A local {}'.format(local2Job), 'named {}'.format(local2FullName) + '{}'.format(local2Fact) +
				'\n' + '-----------------------------' + '\n' + jobsPrintValue + '\n' + '-----------------------------' + 
				'\n' + 'The demographics of the City:' + 
				'\n' 'Humans {}%'.format(round(f0,1)), 
				' mixed {}%'.format(round(g0,1)), 
				' Dwarves {}%'.format(round(h0,1)), 
				' Elves {}%'.format(round(i0,1)), 
				"Kobolds {}%".format(round(j0,1)), 
				'\n' + 'Humans:', int(round(f1)) ,
				' mixed:', int(round(g1)), 
				' Dwarves:', int(round(h1)), 
				' Elves:', int(round(i1,0)),
				' Kobolds:', int(round(j1,0)), 
				'\n' + '\n', file=text_file)
			if iteration % 1 == 0:
				print( round((iteration + 1) / times * 100, 1), '%', barImage, end="\r")
				
			iteration = iteration + 1

	elif z == 3:
		fact0, fact1, fact2 = random.sample(foo14, 3)

		with open("Cities.txt", "a") as text_file:
			print(name, ' Pop:',j, file=text_file)
			print("-----------------------------", file=text_file)
			print(fact0, fact1, fact2, file=text_file)
			print(uniqueFact, file=text_file)
			print('-----------------------------' +
				'\n' 'It has' ,x10 + ' and' ,x9 + 
				'\n' + 'Its street layout',x11 +
				'\n' + 'The City was founded {} years ago'.format(cityAge) + '\n' + '-----------------------------' +
				'\n' + 'A local {}'.format(localJob), 'named {}'.format(localFullName) + '{}'.format(localFact) + 
				'\n' + 'A local {}'.format(local2Job), 'named {}'.format(local2FullName) + '{}'.format(local2Fact) +
				'\n' + '-----------------------------' + '\n' + jobsPrintValue + '\n' + '-----------------------------' + 
				'\n' + 'The demographics of the City:' + 
				'\n' 'Humans {}%'.format(round(f0,1)), ' mixed {}%'.format(round(g0,1)),' Dwarves {}%'.format(round(h0,1)), ' Elves {}%'.format(round(i0,1)), "Kobolds {}%".format(round(j0,1)), '\n' + 'Humans:', int(round(f1)) ,' mixed:', int(round(g1)),' Dwarves:', int(round(h1)),' Elves:', int(round(i1,0)),' Kobolds:', int(round(j1,0)), '\n' + '\n', file=text_file)
			if iteration % 1 == 0:
				print( round((iteration + 1) / times * 100, 1), '%', barImage, end="\r")
				
			iteration = iteration + 1

	elif z == 4:
		fact0, fact1, fact2, fact3 = random.sample(foo14, 4)

		with open("Cities.txt", "a") as text_file:
			print(name, ' Pop:',j, file=text_file)
			print("-----------------------------", file=text_file)
			print(fact0, fact1, fact2, fact3, file=text_file)
			print(uniqueFact, file=text_file)
			print('-----------------------------' +
				'\n' 'It has' ,x10 + ' and' ,x9 + 
				'\n' + 'Its street layout',x11 +
				'\n' + 'The City was founded {} years ago'.format(cityAge) + '\n' + '-----------------------------' +
				'\n' + 'A local {}'.format(localJob), 'named {}'.format(localFullName) + '{}'.format(localFact) + 
				'\n' + 'A local {}'.format(local2Job), 'named {}'.format(local2FullName) + '{}'.format(local2Fact) +
				'\n' + '-----------------------------' + '\n' + jobsPrintValue + '\n' + '-----------------------------' + 
				'\n' + 'The demographics of the City:' + 
				'\n' 'Humans {}%'.format(round(f0,1)), ' mixed {}%'.format(round(g0,1)),' Dwarves {}%'.format(round(h0,1)), ' Elves {}%'.format(round(i0,1)), "Kobolds {}%".format(round(j0,1)), '\n' + 'Humans:', int(round(f1)) ,' mixed:', int(round(g1)),' Dwarves:', int(round(h1)),' Elves:', int(round(i1,0)),' Kobolds:', int(round(j1,0)), '\n' + '\n', file=text_file)
			if iteration % 1 == 0:
				print( round((iteration + 1) / times * 100, 1), '%', barImage, end="\r")
				
			iteration = iteration + 1

	elif z == 5:
		fact0, fact1, fact2, fact3, fact4 = random.sample(foo14, 5)

		with open("Cities.txt", "a") as text_file:
			print(name, ' Pop:',j, file=text_file)
			print("-----------------------------", file=text_file)
			print(fact0, fact1, fact2, fact3, fact4, file=text_file)
			print(uniqueFact, file=text_file)
			print('-----------------------------' +
				'\n' 'It has' ,x10 + ' and' ,x9 + 
				'\n' + 'Its street layout',x11 +
				'\n' + 'The City was founded {} years ago'.format(cityAge) + '\n' + '-----------------------------' +
				'\n' + 'A local {}'.format(localJob), 'named {}'.format(localFullName) + '{}'.format(localFact) +
				'\n' + 'A local {}'.format(local2Job), 'named {}'.format(local2FullName) + '{}'.format(local2Fact) +
				'\n' + '-----------------------------' + '\n' + jobsPrintValue + '\n' + '-----------------------------' + 
				'\n' + 'The demographics of the City:' + 
				'\n' 'Humans {}%'.format(round(f0,1)), ' mixed {}%'.format(round(g0,1)),' Dwarves {}%'.format(round(h0,1)), ' Elves {}%'.format(round(i0,1)), "Kobolds {}%".format(round(j0,1)), '\n' + 'Humans:', int(round(f1)) ,' mixed:', int(round(g1)),' Dwarves:', int(round(h1)),' Elves:', int(round(i1,0)),' Kobolds:', int(round(j1,0)), '\n' + '\n', file=text_file)
			if iteration % 1 == 0:
				print( round((iteration + 1) / times * 100, 1), '%', barImage, end="\r")
				
			iteration = iteration + 1

	else:
		fact0, fact1, fact2, fact3, fact4, fact5 = random.sample(foo14, 6)

		with open("Cities.txt", "a") as text_file:
			print(name, ' Pop:',j, file=text_file)
			print("-----------------------------", file=text_file)
			print(fact0, fact1, fact2, fact3, fact4, fact5, file=text_file)
			print(uniqueFact, file=text_file)
			print('-----------------------------' +
				'\n' 'It has' ,x10 + ' and' ,x9 + 
				'\n' + 'Its street layout',x11 +
				'\n' + 'The City was founded {} years ago'.format(cityAge) + '\n' + '-----------------------------' + 
				'\n' + 'A local {}'.format(localJob), 'named {}'.format(localFullName) + '{}'.format(localFact) +
				'\n' + 'A local {}'.format(local2Job), 'named {}'.format(local2FullName) + '{}'.format(local2Fact) +
				'\n' + '-----------------------------' + '\n' + jobsPrintValue + '\n' + '-----------------------------' + 
				'\n' + 'The demographics of the City:' + 
				'\n' 'Humans {}%'.format(round(f0,1)), ' mixed {}%'.format(round(g0,1)),' Dwarves {}%'.format(round(h0,1)), ' Elves {}%'.format(round(i0,1)), "Kobolds {}%".format(round(j0,1)), '\n' + 'Humans:', int(round(f1)) ,' mixed:', int(round(g1)),' Dwarves:', int(round(h1)),' Elves:', int(round(i1,0)),' Kobolds:', int(round(j1,0)), '\n' + '\n', file=text_file)
			if iteration % 1 == 0:
				print( round((iteration + 1) / times * 100, 1), '%', barImage, end="\r")
				
				iteration = iteration + 1