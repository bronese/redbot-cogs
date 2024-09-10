from .ddinstagram import ddinstagram


async def setup(bot):
    await bot.add_cog(ddinstagram(bot))
