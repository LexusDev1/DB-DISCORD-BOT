import nextcord
import wavelink
from nextcord.ext import commands

class OpMusic(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="Ping")
    async def Play(self, interaction: nextcord.Interaction, * search: wavelink.YoutubeTrack):
        interaction.response.send_message("Pong", ephemeral=True)

def setup(client):
    client.add_cog(Ping(client))
