from __future__ import annotations

import discord
from discord.ext import commands

from bot.KellyBot import KellyBot


class MembershipBase(commands.Cog):

    def __init__(self, bot: KellyBot):
        self.bot: KellyBot = bot

    async def interaction_check(
        self, interaction: discord.Interaction[KellyBot]
    ) -> bool:
        # ! Check if user has modify_memberships permission

        if not interaction.user:
            
        
        userPermissions = await self.bot.prisma.membership.find_unique(where={'id': interaction.user.id})
