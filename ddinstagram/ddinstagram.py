from redbot.core import commands
import discord

class ddinstagram(commands.Cog):
    """replaces instagram.com with ddinstagram.com"""

    def __init__(self, bot):
        self.bot = bot

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if any("instagram.com" in url for url in message.content.split()):
            new_content = message.content
            replied_message = None  # Initialize variable to store replied message
            if message.reference and message.reference.message_id:
                replied_message = await message.channel.fetch_message(message.reference.message_id)
            for url in message.content.split():
                if "instagram.com" in url:
                    new_url = url.replace("instagram.com", "ddinstagram.com")
                    new_content = new_content.replace(url, new_url)
                    webhooks = await message.channel.webhooks()
                    webhook = next((wh for wh in webhooks if wh.name == "vxtiktok"), None)
                    # allowed_mentions = discord.AllowedMentions(users=False,everyone=False,roles=False)
                    if webhook is None:
                        webhook = await message.channel.create_webhook(name="vxtiktok")
                    try:
                        await webhook.send(new_content, username=message.author.display_name, avatar_url=message.author.avatar, wait=1)
                        await message.delete()  # delete the original message
                    except Exception as e:
                        await message.channel.send(f"Failed to send message: {e}")


def setup(bot):
    bot.add_cog(ddinstagram(bot))
