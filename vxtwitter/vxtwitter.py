from redbot.core import commands

class vxtwitter(commands.Cog):
    """replaces vxtwitter"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if any(url.startswith(("twitter.com", "x.com")) for url in message.content.split()):
            await message.channel.send("hi")
            new_content = message.content
            for url in message.content.split():
                if url.startswith("twitter.com") or url.startswith("x.com"):
                    new_url = url.replace(url.split(".com")[0], "vxtwitter")
                    new_content = new_content.replace(url, new_url)
            # Use the channel object to send the message
            await message.channel.send(
                str(new_content), username=message.author.name, avatar_url=message.author.avatar_url
            )

def setup(bot):
    bot.add_cog(vxtwitter(bot))