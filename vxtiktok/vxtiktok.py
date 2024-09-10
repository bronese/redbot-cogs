from redbot.core import commands
import discord

class vxtiktok(commands.Cog):
    """replaces instagram.com with ddinstagram.com"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if "tiktok.com" in message.content:
            new_content = message.content
            responded = False  # Variable to track if we've already responded
            for url in message.content.split():
                if url.startswith("https://tiktok.com") or url.startswith("http://tiktok.com"):
                    new_url = url.replace("tiktok.com", "vxtiktok.com")
                    new_content = new_content.replace(url, new_url)
                    responded = True

            if responded:
                webhooks = await message.channel.webhooks()
                webhook = next((wh for wh in webhooks if wh.user == self.bot.user), None)
                if webhook is None:
                    webhook = await message.channel.create_webhook(name="vxtiktok")

                try:
                    await webhook.send(
                        new_content,
                        username=message.author.display_name,
                        avatar_url=message.author.display_url,
                        wait=True
                    )
                    await message.delete()  # delete the original message
                except discord.HTTPException as e:
                    await message.channel.send(f"Failed to send message: {e}")

def setup(bot):
    bot.add_cog(vxtiktok(bot))
