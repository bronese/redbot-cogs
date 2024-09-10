from .vxtiktok import vxtiktok


async def setup(bot):
    await bot.add_cog(vxtiktok(bot))
