from .vxtiktok import Vxtiktok


async def setup(bot):
    await bot.add_cog(vxtiktok(bot))
