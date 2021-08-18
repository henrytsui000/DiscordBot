from discord.ext import commands
from dotenv import load_dotenv
import os

bot = commands.Bot(command_prefix='!', help_command=None)

not_excute = {"reward.py", "receipt.py", "poetry.py", "initialize_database.py", "test_lene.py", "message.py"}

for dirname in os.listdir('./commands'):
    for filename in os.listdir(f'./commands/{dirname}'):
        print(filename)
        if filename.endswith('.py'):
            if(not (filename in not_excute)):
                bot.load_extension(f'commands.{dirname}.{filename[:-3]}')

load_dotenv()
bot.run(os.getenv("TOKEN"))
