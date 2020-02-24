import discord
import time

client = discord.Client()

@client.event
async def on_ready():
    print('You have logged in as {0.user}'.format(client))


@client.event
async def on_guild_channel_create(ctx):
    channel = client.get_channel(ctx.name)
    if "ticket-" in ctx.name:
        time.sleep(1)
        embed = discord.Embed(title="Information:", description=" BTC/PAYPAL\nFirst and Last name:\nCountry:\nState:\nCity:\nAddress:\nZIP/Postal Code:\nCountry:\nPhone Number:\nProduct:\nSo I do payment upfront and if I fail the SE 3 times you can accept a refund or I can keep trying.\n\nMiddlemans are also accepted but you are paying fees.", colour=0x2ECC71)
        await ctx.send(embed=embed)
        embed = discord.Embed(title="Please fill out the Form", description="A staff member will get back to you.", colour=0x2ECC71)
        await ctx.send(embed=embed)

        
client.run('NjgxMjQzOTQ0OTk4NDA0MTg3.XlMFKw.A5gRXHnWynkInNdfXCj6TVhQj2w')
