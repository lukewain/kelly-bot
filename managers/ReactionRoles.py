from __future__ import annotations

import discord
from discord.ext import commands

from prisma import Prisma
from prisma.models import ReactionRoles, BlacklistedUsers
from typing import Tuple, TypeAlias, Dict

from logging import getLogger

__all__: Tuple[str, ...] = ("ReactionRoleManager",)

GuildID: TypeAlias = int
UserID: TypeAlias = int
MessageID: TypeAlias = int

log = getLogger(__name__)

class ReactionRoleView(discord.ui.View):
    def __init__(self, *, ReactionRoleID: int, manager: ReactionRoleManager):
        super().__init__(timeout=None)
        self.manager = manager
        self.reaction_role_id = ReactionRoleID
        self.


class ReactionRoleManager:
    def __init__(self, prisma: Prisma) -> None:
        self._prisma: Prisma = prisma

        self._reaction_roles: Dict[MessageID, ReactionRoles] = {}
        self._active_reaction_roles: Dict[MessageID, ReactionRoles] = {}
        self._blacklisted_users: Dict[MessageID, BlacklistedUsers] = {}

        self.started: bool = False

    async def __aenter__(self):
        try:
            await self.start()
        except Exception as e:
            log.error(
                "Could not start reaction role manager. Reaction roles will not work as intended",
                exc_info=e,
            )

        return self

    async def __aexit__(self, *_):
        pass

    async def start(self):
        """Start the reaction role manager."""

        # * Get all blacklisted users
        blacklisted_users: list[BlacklistedUsers] = (
            await self._prisma.blacklistedUsers.find_many()
        )
        self._blacklisted_users = {
            blacklisted_user.id: blacklisted_user
            for blacklisted_user in blacklisted_users
        }

        # * Get all reaction roles
        reaction_roles: list[ReactionRoles] = (
            await self._prisma.reactionRoles.find_many()
        )
        self._reaction_roles = {
            reaction_role.message_id: reaction_role for reaction_role in reaction_roles
        }

        # * Filter all active views
        self._active_reaction_roles = {
            rr.id: rr for rr in self._reaction_roles.values() if rr.active
        }

    async def register_views(self, client: commands.Bot):
        for reaction_role in self._active_reaction_roles.values():
            # TODO: Create reaction role view
            await client.add_view()
