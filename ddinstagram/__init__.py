from .ddinstagram import DdInstagram


async def setup(bot):
    await bot.add_cog(ddinstagram(bot))
