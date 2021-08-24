import discord
import random
import os


#How you register an event with Discord
client = discord.Client()

#This is called when the bot is ready to be used
@client.event
async def on_ready():
  print('Pasta BOT; by narlock; has been logged in by {0.user}'.format(client))

#If the bot senses a message, then something will happen
@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  if msg.content.startswith("%hello"):
    await msg.channel.send("o/")

  if msg.content.startswith("%pasta"):
    await msg.channel.send(getPasta())

def getPasta():
  number = random.randint(0,3)

  if number == 0:
    return "Can we:pray:pretend:pensive:that airplanes:airplane:in the:disappointed:night skÿ:night_with_stars: aré likê:pray: sh00tíng stars:star2::stars::stars: I could :raised_hand: rlly use:muscle::muscle: a wish:pray:right now:pensive: wish :pray:right now:pensive:wish:smirk_cat:right now:broken_heart::broken_heart::broken_heart:"
  if number == 1:
    return "A slab is half a block. If you say \"half-slab,\" you're literally saying \"half half block,\" or in other words, \"quarter-block.\" A slab is not a quarter of a block. It is a half of a block. There is no such thing as a quarter block."
  if number == 2:
    return "Oni-chan, that's nOT what siblings do!!!"
  if number == 3:
    return "O-oooooooooo AAAAE-A-A-I-A-U- JO-oooooooooooo AAE-O-A-A-U-U-A- E-eee-ee-eee AAAAE-A-E-I-E-A-JO-ooo-oo-oo-oo EEEEO-A-AAA-AAA"

client.run(os.getenv("TOKEN"))
