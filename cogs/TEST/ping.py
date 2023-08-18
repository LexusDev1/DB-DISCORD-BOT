import nextcord
from nextcord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="Ping")
    async def ping(self, interaction: nextcord.Interaction):
        interaction.response.send_message("Pong", ephemeral=True)

def setup(client):
    client.add_cog(Ping(client))