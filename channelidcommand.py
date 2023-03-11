import discord
import requests
import json

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('/channelinfo'):
        channel_id = message.content.split()[1]
        response = requests.get(f'https://banner.yt/channel/{channel_id}')
        data = json.loads(response.content)

        # Extract relevant information from data
        channel_name = data['name']
        subscribers = data['stats']['subscriberCount']

        # Format and send response message
        response_msg = f'```Channel Info found...\nName: {channel_name}\nSubscribers: {subscribers}```'
        await message.channel.send(response_msg)

    elif message.content.startswith('/userinfo'):
        user_id = message.content.split()[1]
        response = requests.get(f'https://banner.yt/user/{user_id}')
        data = json.loads(response.content)

        # Extract relevant information from data
        username = data['username']
        channel_count = data['stats']['channelCount']

        # Format and send response message
        response_msg = f'```User Info found...\nUsername: {username}\nChannel Count: {channel_count}```'
        await message.channel.send(response_msg)

    elif message.content.startswith('/handleinfo'):
        handle = message.content.split()[1]
        response = requests.get(f'https://banner.yt/{handle}')
        data = json.loads(response.content)

        # Extract relevant information from data
        channel_name = data['name']
        subscribers = data['stats']['subscriberCount']

        # Format and send response message
        response_msg = f'```Handle Info found...\nName: {channel_name}\nSubscribers: {subscribers}```'
        await message.channel.send(response_msg)

client.run('MTA4MDY1MDI1Mjc2NTM4NDc5NA.GXzHWw.i3nJcW8GNwo8Vlh7uQkEjhuIxw6mhWzicFoTRE')
