from __future__ import annotations

import discord
from discord.ext import commands


class DynamicReactionRoleButtons(
    discord.ui.DynamicItem[discord.ui.Button],
    template=r"button:reactionrole:(?P<id>[0-9]+)",
):
    def __init__(self, reaction_role_id: int):
        super().__init__()

    ...


class ReactionButton: ...
