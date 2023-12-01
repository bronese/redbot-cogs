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
                if url.startswith(("https://twitter.com", "https://x.com")):
                    await message.channel.send("link found")
                    new_url = url.replace("twitter.com", "vxtwitter.com").replace("x.com", "vxtwitter.com")
                    new_content = new_content.replace(url, new_url)
                    webhooks = await message.channel.webhooks()
                    webhook = next((wh for wh in webhooks if wh.name == "vxtwitter"), None)
                    if webhook is None:
                        webhook = await message.channel.create_webhook(name="vxtwitter")
                    try:
                        await webhook.send(new_content, username=message.author.name, avatar_url=message.author.avatar)
                        await message.delete(message)  # delete the original message
                    except Exception as e:
                       await message.channel.send(f"Failed to send message: {e}")
def setup(bot):
    bot.add_cog(vxtwitter(bot))