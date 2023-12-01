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
            return
        if any(url.startswith(("https://twitter.com", "https://x.com")) for url in message.content.split()):   
            new_content = message.content
            for url in message.content.split():
                if url.startswith("twitter.com") or url.startswith("x.com"):
                    new_url = url.replace(url.split(".com")[0], "vxtwitter")
                    new_content = new_content.replace(url, new_url)
                    await message.channel.send(new_content)
                    webhooks = await message.channel.webhooks()
                    webhook = next((wh for wh in webhooks if wh.name == "vxtwitter"), None)
                    if webhook is None:
                        webhook = await message.channel.create_webhook(name="vxtwitter")
                        await message.channel.send("webhook created")
                    await webhook.send(new_content, username=message.author.name, avatar_url=message.author.avatar_url)
def setup(bot):
    bot.add_cog(vxtwitter(bot))