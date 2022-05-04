# import discord
# from secrets import discord_bot_token


# client = discord.Client()
#
# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))
#
#
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

# client.run(discord_bot_token)

if __name__ == '__main__':



    # from access import Access
    # access = Access()

    # 1
    # Obtain AH prices
    # auctions = access.get_auctions()

    # 1.5
    # print the AH lowest price
    # from item import Item

    from test import test_item
    test_item()

    # 2
    # calculate the amount of ingredients that are below the "break even price'

    # 2.1 calculate the "break even price" (BEP)

