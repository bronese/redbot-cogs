from redbot.core import commands
import discord
import aiohttp

class vxtwitter(commands.Cog):
    """replaces vxtwitter"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            await message.channel.send("bot ignored")
            return
        if any(url.startswith(("https://twitter.com", "https://x.com")) for url in message.content.split()):   
            await message.channel.send("triggered 2")
            new_content = message.content
            for url in message.content.split():
                if url.startswith("twitter.com") or url.startswith("x.com"):
                    new_url = url.replace(url.split(".com")[0], "vxtwitter")
                    new_content = new_content.replace(url, new_url)
            # Use the webhook to send the message
            webhooks = await message.channel.webhooks()
            if webhooks:
                webhook = webhooks[0]
            else:
                webhook = await message.channel.create_webhook(name="vxtwitter")
            async with aiohttp.ClientSession() as session:
                webhook = discord.Webhook.from_url(webhook.url, adapter=discord.AsyncWebhookAdapter(session))
                await webhook.send(new_content, username=message.author.name, avatar_url=message.author.avatar_url)

def setup(bot):
    bot.add_cog(vxtwitter(bot))