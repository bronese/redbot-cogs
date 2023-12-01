from redbot.core import commands, Webhook

class vxtwitter(commands.Cog):
    """replaces vxtwitter"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if any(url.startswith(("twitter.com", "x.com")) for url in message.content.split()):
            new_content = message.content
            for url in message.content.split():
                if url.startswith("twitter.com") or url.startswith("x.com"):
                    new_url = url.replace(url.split(".com")[0], "vxtwitter")
                    new_content = new_content.replace(url, new_url)

                webhook = await message.channel.create_webhook(name=message.name)
                await webhook.send(
                    str(new_content), username=message.name, avatar_url=message.avatar_url)
                webhooks = await message.channel.webhooks()
                for webhook in webhooks:
                        await webhook.delete()

def setup(bot):
    bot.add_cog(vxtwitter(bot))