from .vxtwitter import MyCog


async def setup(bot):
    await bot.add_cog(vxtwitter(bot))
