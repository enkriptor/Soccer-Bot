import discord, random

client = discord.Client()
sieve = []
humanScore, botScore, botChance, humanChance, chance, matchStarter, matchDecider = 0, 0, False, True, 0, False, ["heads", "tails"]

@client.event
async def on_ready():
	print("We logged in as {0.user}".format(client))

@client.event
async def on_message(message):
	global humanScore, botScore, botChance, humanChance, chance, matchStarter, matchDecider, sieve
	if(message.author == client.user):
		return

	if(message.content == '!soccerrules'):
		await message.channel.send('Simple rules: \n type \'!soccerplay\' to start the play! \n type 0 for left-side kick\n type 1 for center kick\n type 2 for right-side kick')
	if(message.content == '!soccerplay'):
		await message.channel.send('Let\'s start the play!')
		await message.channel.send('Type heads or tails for toss!')
	if(message.content in matchDecider):
		if(message.content == matchDecider[random.randint(0,1)]):
			matchStarter = True
			botChance = False
			humanChance = True
			await message.channel.send("match started! you won the toss")
		else:
			matchStarter = True
			botChance = True
			humanChance = False
			await message.channel.send("match started! bot won the toss")
	if(matchStarter):
		if(not botChance and humanChance):
			if(message.content=="1" or message.content=="2" or message.content=="0"):
				botAnswer = str(random.randint(0,2))
				sieve.append(botAnswer)
				if(botAnswer == message.content):
					await message.channel.send(botAnswer+'I stopped the ball!')
				else:
					humanScore += 1
					await message.channel.send(botAnswer+' What a goal!')
			if(len(sieve) == 5):
				chance += 1
				await message.channel.send('Well played! Your score '+str(humanScore))
				if(humanChance and chance != 2):
					await message.channel.send('Now your turn to stop me!')
					sieve = []
					botChance = True
					humanChance = False
		else:
			if(message.content=="1" or message.content=="2" or message.content=="0"):
				botAnswer = str(random.randint(0,2))
				sieve.append(botAnswer)
				if(botAnswer == message.content):
					await message.channel.send(botAnswer+"Nice stop!")
				else:
					botScore += 1
					await message.channel.send(botAnswer+'Champ goal!')
			if(len(sieve) == 5):
				chance += 1
				await message.channel.send('My score '+str(botScore))
				if(botChance and chance!=2):
					await message.channel.send('Now your turn to shoot!')
					await message.channel.send('Enter the side to dive!')
					sieve = []
					botChance = False
					humanChance = True
		if(chance == 2):
			if(humanScore > botScore):
				await message.channel.send("You win!")
			elif(humanScore == botScore):
				await message.channel.send("Match draw!")
			else:
				await message.channel.send("You lose!")
			matchStarter = False

client.run('DISCORD_TOKEN')