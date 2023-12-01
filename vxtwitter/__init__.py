from .vxtwitter import vxtwitter


async def setup(bot):
    await bot.add_cog(vxtwitter(bot))
