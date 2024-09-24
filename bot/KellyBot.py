import discord
from discord.ext import commands

from prisma import Prisma


class KellyBot(commands.Bot):
    def __init__(self, *, prisma: Prisma, reaction_manager, aiosession, config):
        # Initialize custom vars
        self.prisma = prisma
        self.reaction_manager = reaction_manager
        self._session = aiosession
        self.config = config
