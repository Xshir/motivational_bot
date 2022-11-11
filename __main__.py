import hikari
import lightbulb
import random
from credentials import token # imports secret variables from another .py file
from constants import prefix, motivational_quotes # imports a variable from another .py file

bot = lightbulb.BotApp(prefix=prefix, token=token, intents=hikari.Intents.ALL)

@bot.listen(hikari.ShardReadyEvent) # decorator
async def ready_listener(_):
    print("The bot is ready!")


@bot.command()
@lightbulb.command("ping", "Checks that the bot is alive")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:
    """Checks that the bot is alive"""
    await ctx.respond("Pong!")

@bot.command()
@lightbulb.command("motivation", "Sends motivational quotes")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:
    message = random.choice(motivational_quotes)
    await ctx.respond(message) #coroutine


bot.run()