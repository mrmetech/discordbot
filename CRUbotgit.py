# Crubot by dest
# trollboxbot by dest
import requests
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Game

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
    embed.add_field(name="!cru", value="Get the price of Curium", inline=False)
    embed.add_field(name="!cruinfo", value="information on the curium network", inline=False)
    embed.add_field(name="!btc", value="Get the price of bitcoin", inline=False)
    embed.add_field(name="!ltc", value="Get the price of Litecoin", inline=False)
    embed.add_field(name="!balance", value="Get the balance of a curium address !balance address", inline=False)
    embed.add_field(name="!installguide", value="Get the Masternode install guide ", inline=False)
    embed.add_field(name="which coin gunna do goddest", value="type CRU", inline=False)
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
    stockapi = 'https://api.coingecko.com/api/v3/coins/curium.json'
    stockprice = requests.get(stockapi)
    stockvalue = stockprice.json()['tickers'][0]['converted_last']['btc']
    sxcvalue = stockprice.json()['tickers'][1]['converted_last']['btc']
    chanvalue = stockprice.json()['tickers'][2]['converted_last']['btc']
    stockvol = stockprice.json()['tickers'][0]['volume']  
    sxcvol = stockprice.json()['tickers'][1]['volume']
    chanvol = stockprice.json()['tickers'][2]['volume']
    cruusdvalue = stockprice.json()['market_data']['current_price']['usd']
    volvalue = stockprice.json()['market_data']['total_volume']['usd']
    bvolvalue = stockprice.json()['market_data']['total_volume']['btc']
    
    embed = discord.Embed(title="Here is price information for Curium", color=0x42f4cb)
    embed.add_field(name="Price USD", value="The price is $" + str(cruusdvalue), inline=False)
    embed.add_field(name="Price BTC On Stock.exchange", value="Price BTC " + str(stockvalue) + " Volume in CRU " + str(stockvol), inline=False)
    embed.add_field(name="Price BTC On Crypto Hub", value="Price BTC " + str(chanvalue) + " Volume in CRU " + str(chanvol), inline=False)
    embed.add_field(name="Price BTC On SouthXchange", value="Price BTC " + str(sxcvalue) + " Volume in CRU " + str(sxcvol), inline=False)
    embed.add_field(name="Volume in USD ", value="This is the volume $" + str(volvalue), inline=False)
    embed.add_field(name="Volume in BTC ", value="This is the volume BTC " + str(bvolvalue), inline=False)
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
    await bot.say(embed=embed)



@bot.command(pass_context=True)
async def balance(ctx, bal : str):
    btcapi = 'http://explorer.curiumofficial.com/ext/getbalance/' 
    abtcapi = btcapi + bal
    btcprice = requests.get(abtcapi).json()
    value = btcprice
   
    embed = discord.Embed(title="Here is the amount of curium in a address", color=0x42f4cb)
    embed.add_field(name="Balance ", value= "The Balance of that address is " + str(value) + " CRU", inline=False)

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
        await client.change_presence(game=discord.Game(name="CRU: " + price))
        await asyncio.sleep(60)






        
bot.loop.create_task(updateprice())
bot.run("")
