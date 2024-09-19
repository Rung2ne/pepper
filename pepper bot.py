import discord
from discord.ext import commands
from discord import app_commands

# 디스코드 봇 인스턴스 생성
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# 슬래시 명령어 등록
class MyBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 슬래시 명령어 정의
    @app_commands.command(name="서우는", description="서우는 누구인가요?")
    async def 서우는(self, interaction: discord.Interaction):
        await interaction.response.send_message("단순해")

async def setup(bot):
    await bot.add_cog(MyBot(bot))
    await bot.tree.sync()  # 슬래시 명령어를 동기화

# 봇 실행
bot.run("YMTI4NjI4MjMyNzk4MjM0NjMyNA.Gqd7Lo.ObTOnVsKqpfkGPdiGowg-XyjKorM6hyWCjaQlc")