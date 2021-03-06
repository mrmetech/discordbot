# Crubot by dest
# trollboxbot by dest
import requests
import discord
import asyncio
from decimal import *
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Game
import json

# "!" is the command trigger
bot = commands.Bot(command_prefix='!')
client = discord.Client()
bot.remove_command("help")
# on start up bot will print this data with its user name
@bot.event
async def on_ready():
    print ("011001100010001")
    print ("loading//.." + bot.user.name + ", Awaiting your command")

 # on member join will send a message to incoming user greeting them.. (still in progress may not work)
 # dont forget to put the channel id# in the code too
@bot.event
async def on_member_join(member):
    await bot.send_message(bot.get_channel('YOUNEEDCHANNELID#HERE'), " Welcome" + bot.user.name + " , at your service, type !help for a list of commands")

#embed list of commands
@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="The following are valid commands", color=0x42f4cb)
    embed.add_field(name="!help", value="Get help message", inline=False)
    embed.add_field(name="!ping", value="Get a bot responce", inline=False)
    embed.add_field(name="!<ticker>", value="Put a coins ticker for price info example !btc or !cru", inline=False)
    embed.add_field(name="!<ticker>info", value="information on the curium network", inline=False)


    embed.add_field(name="!<ticker>bal", value="Get the balance of a address !(thecoin)bal address", inline=False)
    embed.add_field(name="!installguide", value="Get the Masternode install guide ", inline=False)
    embed.add_field(name="Coin we Support", value="We Support cru and scriv", inline=False)
    embed.set_footer(text="curiumofficial.com | !help ", icon_url='https://i.imgur.com/WN3Z5lX.png')
    await bot.say(embed=embed)

# ping the bot command to test
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong:  " + bot.user.name + ", Awaiting your command $$$")

# get the latest masternode install guide
@bot.command(pass_context=True)
async def installguide(ctx):
    await bot.say("Here is the latest masternode install guide version https://e-rave.nl/curium-master-node-setup-cold-wallet")

# get the current price of btc
@bot.command(pass_context=True)
async def cru(ctx):
    with open('src/coinData/curium.json', 'r') as f:
        datastore = json.load(f)
    stockvalue = datastore["coinvalue"]
    stockvol = stockprice.json()['tickers'][0]['volume']  
    cruusdvalue = datastore["usdvalue"]
    volvalue = datastore["volvalue"]
    bvolvalue = datastore["bvolvalue"]
    
    embed = discord.Embed(title="Here is price information for Curium", color=0x42f4cb)
    embed.add_field(name="Price USD", value="The price is $" + str(cruusdvalue), inline=False)
    embed.add_field(name="Price BTC", value="The price is " + str(stockvalue) + " BTC", inline=False)
    embed.add_field(name="Volume in USD ", value="This is the volume $" + str(volvalue), inline=False)
    embed.add_field(name="Volume in BTC ", value="This is the volume BTC " + str(bvolvalue), inline=False)
    embed.set_footer(text="curiumofficial.com | !help ", icon_url='https://i.imgur.com/WN3Z5lX.png')
    await bot.say(embed=embed)
    
    
# get the current price of btc
@bot.command(pass_context=True)
async def scriv(ctx):
    gravapi = 'https://graviex.net/api/v2/tickers/scrivbtc.json'
    gravprice = requests.get(gravapi, verify=False)
    btcapi = 'https://api.coinmarketcap.com/v2/ticker/1/'
    btcprice = requests.get(btcapi)
    btcvalue = btcprice.json()['data']['quotes']['USD']['price']
    scrivvalue = gravprice.json()['ticker']['last']
    scrivbtcvol = gravprice.json()['ticker']['volbtc']
    scrivvol = gravprice.json()['ticker']['vol']
    scrivusdvol = float(scrivbtcvol) * float(btcvalue)
    scrivusdvalue = float(btcvalue) * float(scrivvalue)
    
    embed = discord.Embed(title="Here is price information for Scriv", color=0x42f4cb)
    embed.add_field(name="Price USD", value="The price is $ " + str(scrivusdvalue), inline=False)
    embed.add_field(name="Price BTC On Graviex", value="Price BTC " + str(scrivvalue) + " Volume in SCRIV " + str(scrivvol), inline=False)
    embed.add_field(name="Volume in USD ", value="This is the volume $" + str(scrivusdvol), inline=False)
    embed.add_field(name="Volume in BTC ", value="This is the volume BTC " + str(scrivbtcvol), inline=False)
    embed.set_footer(text="curiumofficial.com | !help ", icon_url='https://i.imgur.com/WN3Z5lX.png')
    await bot.say(embed=embed)
    
    
@bot.command(pass_context=True)
async def btc(ctx):
    btcapi = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    btcprice = requests.get(btcapi)
    value = btcprice.json()['bpi']['USD']['rate']
    await bot.say("Current Bitcoin price is: $" + value)

# get the current price of ltc
@bot.command(pass_context=True)
async def ltc(ctx):
    url = 'https://api.coinmarketcap.com/v1/ticker/litecoin/'
    response = requests.get(url)
    value = response.json()[0]['price_usd']
    await bot.say("Current Litecoin price is: $" + value)

# retun the current Currium difficulty
@bot.command(pass_context=True)
async def cruinfo(ctx):
    #difficulty api
    gdapi = 'https://explorer.curiumofficial.com/api/getdifficulty'
    gdresponse = requests.get(gdapi).json()
    gdvalue = str(gdresponse)
    #block count api
    gbcapi = 'https://explorer.curiumofficial.com/api/getblockcount'
    gbcresponse = requests.get(gbcapi).json()
    gbcvalue = str(gbcresponse)
    #get network hashps
    gnhapi = 'https://explorer.curiumofficial.com/api/getnetworkhashps'
    gnhresponse = requests.get(gnhapi).json()
    gnhvalue = str(gnhresponse)
    #getmoney supply
    gmsapi = 'https://explorer.curiumofficial.com/ext/getmoneysupply'
    gmsresponse = requests.get(gmsapi).json()
    gmsvalue = str(gmsresponse)
    
    
    embed = discord.Embed(title="Here is information on the Curium Network", color=0x42f4cb)
    embed.add_field(name="Current Network Diffculty", value="The Diffuclty is " + gdvalue, inline=False)
    embed.add_field(name="Total Blocks Mined", value="The amount of blocks mined " + gbcvalue, inline=False)
    embed.add_field(name="Network hash rate", value="The Total hashing power on the network " + gnhvalue, inline=False)
    embed.add_field(name="The Total amount of coins", value="The Total amount of coins that have ever been made  " + gmsvalue, inline=False)
    embed.set_footer(text="curiumofficial.com | !help ", icon_url='https://i.imgur.com/WN3Z5lX.png')
    await bot.say(embed=embed)

# retun the current Currium difficulty
@bot.command(pass_context=True)
async def scrivinfo(ctx):
    #difficulty api
    gdapi = 'http://185.243.112.220/api/getdifficulty'
    gdresponse = requests.get(gdapi).json()
    gdvalue = str(gdresponse)
    #block count api
    gbcapi = 'http://185.243.112.220/api/getblockcount'
    gbcresponse = requests.get(gbcapi).json()
    gbcvalue = str(gbcresponse)
    #get network hashps
    gnhapi = 'http://185.243.112.220/api/getnetworkhashps'
    gnhresponse = requests.get(gnhapi).json()
    gnhvalue = str(gnhresponse)
    #getmoney supply
    gmsapi = 'http://185.243.112.220/ext/getmoneysupply'
    gmsresponse = requests.get(gmsapi).json()
    gmsvalue = str(gmsresponse)
    
    
    embed = discord.Embed(title="Here is information on the Scrive Network", color=0x42f4cb)
    embed.add_field(name="Current Network Diffculty", value="The Diffuclty is " + gdvalue, inline=False)
    embed.add_field(name="Total Blocks Mined", value="The amount of blocks mined " + gbcvalue, inline=False)
    embed.add_field(name="Network hash rate", value="The Total hashing power on the network " + gnhvalue, inline=False)
    embed.add_field(name="The Total amount of coins", value="The Total amount of coins that have ever been made  " + gmsvalue, inline=False)
    embed.set_footer(text="curiumofficial.com | !help ", icon_url='https://i.imgur.com/WN3Z5lX.png')
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def crubal(ctx, bal : str):
    btcapi = 'http://explorer.curiumofficial.com/ext/getbalance/' 
    abtcapi = btcapi + bal
    btcprice = requests.get(abtcapi).json()
    value = btcprice
   
    embed = discord.Embed(title="Here is the amount of curium in a address", color=0x42f4cb)
    embed.add_field(name="Balance ", value= "The Balance of that address is " + str(value) + " CRU", inline=False)
    embed.set_footer(text="curiumofficial.com | !help ", icon_url='https://i.imgur.com/WN3Z5lX.png')
    await bot.say(embed=embed)
# get the current price of btc
@bot.command(pass_context=True)
async def scrivmn(ctx):
    with open('src/coinData/scriv.json', 'r') as f:
        datastore = json.load(f)
    roi = datastore["mnroi"]
    mncount = datastore["mncount"]
    dailyrewardcoin = datastore["dECOIN"]
    dailyrewardusd = datastore["dEUSD"]
    monthlyrewardcoin = datastore["mECOIN"]
    monthlyrewardusd = datastore["mEUSD"] 
    yearlyrewardcoin = datastore["yCOIN"]
    yearlyrewardusd = datastore["yEUSD"]   
    
    embed = discord.Embed(title="Here is Masternode information for Scriv", color=0x42f4cb)
    embed.add_field(name="ROI ", value="The roi is  " + str(roi) + " %", inline=False)
    embed.add_field(name="Daily Reward ", value="You will get " + str(dailyrewardcoin) + " coins a day and " + str(dailyrewardusd) + " USD a day", inline=False)
    embed.add_field(name="Monthly Reward ", value="You will get " + str(monthlyrewardcoin) + " coins a month and " + str(monthlyrewardusd) + " USD a month", inline=False)
    embed.add_field(name="Yearly Reward ", value="You will get " + str(yearlyrewardcoin) + " coins a year and " + str(yearlyrewardusd) + " USD a year", inline=False)
    embed.add_field(name="Masternode Count", value="There are " + str(mncount) + " masternodes", inline=False)
    embed.set_footer(text="curiumofficial.com | !help ", icon_url='https://i.imgur.com/WN3Z5lX.png')
    await bot.say(embed=embed)
    
@bot.command(pass_context=True)
async def scrivbal(ctx, bal : str):
    btcapi = 'http://185.243.112.220/ext/getbalance/' 
    abtcapi = btcapi + bal
    btcprice = requests.get(abtcapi).json()
    value = btcprice
   
    embed = discord.Embed(title="Here is the amount of SCRIV in the address", color=0x42f4cb)
    embed.add_field(name="Balance ", value= "The Balance of that address is " + str(value) + " SCRIV", inline=False)
    embed.set_footer(text="curiumofficial.com | !help ", icon_url='https://i.imgur.com/WN3Z5lX.png')
    await bot.say(embed=embed)
    
    
@bot.command(pass_context=True)
async def P(ctx, coin : str):
    btcapi = 'https://api.coinmarketcap.com/v2/ticker/?convert=BTC'
    seaapi_json = requests.get(btcapi)
    seaapi_res = seaapi_json.json()
    ethapi = 'https://api.coinmarketcap.com/v2/ticker/?convert=ETH'
    ethapi_json = requests.get(ethapi)
    ethapi_res = ethapi_json.json()
    price = 'Unknown'
    name = 'Unknown'
    rank = 'Unknown'
    usd = 'Unknown'
    btc = 'Unknown'
    eth = 'Unknown'
    mc = 'Unknown'
    vol = 'Unknown'
    sup = 'Unknown'
    c1h = 'Unknown'
    c24h = 'Unknown'
    c7d = 'Unknown'
    for pair in seaapi_res:
        if pair['symbol'] == str(coin):
            name = pair['name']
            rank = pair['rank']
            usd = pair['quotes']['USD']['price']
            btc = pair['quotes']['BTC']['price']
            mc = pair['quotes']['USD']['market_cap']
            vol = pair['quotes']['USD']['volume_24h']
            sup = pair['total_supply']
            c1h = pair['quotes']['USD']['percent_change_1h']
            c24h = pair['quotes']['USD']['percent_change_24h']
            c7d = pair['quotes']['USD']['percent_change_7d']  
    for pair in ethapi_res:
        if pair['symbol'] == str(coin):
            eth = pair['quotes']['ETH']['price']            

    embed = discord.Embed(title="Here is the amount of curium in a address", color=0x42f4cb)
    embed.add_field(name="Balance ", value= "The Balance of that address is " + str(value) + " CRU", inline=False)

    await bot.say(embed=embed)        

# listen for someone to say cru then message them 
@bot.listen()
async def on_message(message):
    if message.content.startswith('cru'):
        userID = message.author.id
        await bot.send_message(message.channel, "<@%s> cha ching :moneybag: :dollar:" % (userID))
        
# alt way to get latest install guide
@bot.listen()
async def on_message(message):
    if message.content.startswith('install-guide'):
        userID = message.author.id
        await bot.send_message(message.channel, "<@%s> Here is the latest Masternode install guide https://e-rave.nl/curium-master-node-setup-cold-wallet" % (userID))
 
async def updateprice():
    while True:
        seapi_url = 'https://stocks.exchange/api2/ticker/'
        seaapi_json = requests.get(seapi_url)
        seaapi_res = seaapi_json.json()
        price = 'Unknown'
        for pair in seaapi_res:
            if pair['market_name'] == 'CRU_BTC':
                price = pair['last']
        await change_presence(game=discord.Game(name='Skittlely\'s Fun House', type=0))
        await asyncio.sleep(60)






        
bot.loop.create_task(updateprice())
bot.run("NDQzNzc5NDU0MzE4MjgwNzE2.DfDHVQ.Yz9UYILOrFCJXYvqaRutpfMcuOs")
