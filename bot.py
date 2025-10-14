import discord
from discord.ext import commands
from discord.ui import Select, View

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# IDs dos cargos
role_ids = {
    "owner": 1417591421954818280,
    "astral_guardian": 1417591421954818278,
    "galactic_emissary": 1417591421954818276,
    "administrator": 1417591421954818272,
    "senior_moderator": 1417591421954818271,
    "moderator": 1417591421946298397,
    "junior_moderator": 1417591421946298396,
    "helper": 1417591421946298391,
    "content_creator": 1417591421946298388,
    "cc_plus": 1418941145488035911,
    "level_10": 1417591421912875238,
    "level_20": 1417591421925462116,
    "level_30": 1417591421925462117,
    "level_40": 1417591421925462118,
    "level_50": 1417591421925462120,
    "vip": 1417591421925462122,
}

# Imagens
small_img = "https://cdn.discordapp.com/attachments/1373309766788710510/1418984759459053588/image_12.png"
large_img = "https://cdn.discordapp.com/attachments/1373309766788710510/1418985301837348874/Group_457_1.png"

# Mensagens (PT e EN)
staff_info_pt = f"""
🌌 **FAQ da Equipe**  
👑 <@&{role_ids['owner']}> — O dono oficial do Anime Revolution: Ultimate e de sua equipe de desenvolvimento.
🌠 <@&{role_ids['astral_guardian']}> — Gerencia a comunidade e aplica as regras.
🌟 <@&{role_ids['galactic_emissary']}> — Supervisiona toda a equipe de staff, orientando os Admins e garantindo que tudo seja feito de forma eficaz.
💫 <@&{role_ids['administrator']}> — Auxilia o Community Manager na orientação e supervisão dos Moderadores, garantindo profissionalismo e punições justas.
⚡ <@&{role_ids['senior_moderator']}> — Orienta os Moderadores e supervisiona a equipe de Helpers.
🛡️ <@&{role_ids['moderator']}> — Lida com denúncias, tickets e aplicação das regras.
📜 <@&{role_ids['junior_moderator']}> — Moderadores em período de teste.
🤝 <@&{role_ids['helper']}> — Auxiliam os Moderadores e ajudam a comunidade com dúvidas.
"""

staff_info_en = f"""
🌌 **Staff FAQ**  
👑 <@&{role_ids['owner']}> — The official owner of Anime Revolution: Ultimate and its development team.
🌠 <@&{role_ids['astral_guardian']}> — Manages the community and enforces the rules.
🌟 <@&{role_ids['galactic_emissary']}> — Supervises staff and guides Admins.
💫 <@&{role_ids['administrator']}> — Assists the Community Manager and ensures professionalism.
⚡ <@&{role_ids['senior_moderator']}> — Guides Moderators and supervises Helpers.
🛡️ <@&{role_ids['moderator']}> — Handles reports, tickets, and rules.
📜 <@&{role_ids['junior_moderator']}> — Trial moderators assisting with enforcement.
🤝 <@&{role_ids['helper']}> — Help with moderation and community support.
"""

level_info_pt = f"""
✨ **Cargos de Nível**  
🎖️ <@&{role_ids['level_10']}> — Emojis externos  
🎖️ <@&{role_ids['level_20']}> — Figurinhas externas  
🎖️ <@&{role_ids['level_30']}> — Imagens e apelido  
🎖️ <@&{role_ids['level_40']}> — Reações  
👑 <@&{role_ids['level_50']}> — Cargo personalizado (para os 5 primeiros)

🌟 **FAQ de Cargos Especiais**  
💎 <@&{role_ids['vip']}> — Confiáveis, amigos da staff ou colaboradores recentes
"""

level_info_en = f"""
✨ **Level Roles**  
🎖️ <@&{role_ids['level_10']}> — External emojis  
🎖️ <@&{role_ids['level_20']}> — External stickers  
🎖️ <@&{role_ids['level_30']}> — Images, GIFs, nickname  
🎖️ <@&{role_ids['level_40']}> — Add reactions  
👑 <@&{role_ids['level_50']}> — Custom role for first 5

🌟 **Special Roles FAQ**  
💎 <@&{role_ids['vip']}> — Trusted members, staff friends, recent contributors
"""

creator_info_pt = f"""
🌟 **Requisitos para Criador de Conteúdo**  

🌟 <@&{role_ids['content_creator']}>  
YouTube: 1k inscritos, 300+ views/vídeo, 2 vídeos de gameplay (8 min+)  
TikTok: 5k seguidores, 2k+ views, 4 shorts de jogos  
Twitch: 500 seguidores, 4 lives/mês, 10–20 viewers

🌟 <@&{role_ids['cc_plus']}>  
YouTube: 10k inscritos, 2k+ views/vídeo, 3 vídeos/semana  
TikTok: 25k seguidores, 5k+ views, 6 shorts  
Twitch: 1k seguidores, 4 lives/mês, 50+ viewers
"""

creator_info_en = f"""
🌟 **Content Creator Requirements**  

🌟 <@&{role_ids['content_creator']}>  
YouTube: 1k subs, 300+ views/video, 2 gameplay videos (8 min+)  
TikTok: 5k followers, 2k+ views, 4 game shorts  
Twitch: 500 followers, 4 streams/month, 10–20 viewers

🌟 <@&{role_ids['cc_plus']}>  
YouTube: 10k subs, 2k+ views/video, 3 videos/week  
TikTok: 25k followers, 5k+ views, 6 shorts  
Twitch: 1k followers, 4 streams/month, 50+ viewers
"""

# Dropdown
class InfoDropdown(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Staff Roles / Cargos da Equipe", description="Informações sobre a equipe / Staff info", emoji="🌌"),
            discord.SelectOption(label="Level Roles / Cargos de Nível", description="Informações sobre os níveis / Level info", emoji="✨"),
            discord.SelectOption(label="Content Creator / Criador de Conteúdo", description="Informações sobre criadores / Creator info", emoji="🌟"),
        ]
        super().__init__(
            placeholder="Selecione uma categoria / Select a category",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="info_dropdown"  # Necessário para persistência
        )

    async def callback(self, interaction: discord.Interaction):
        selected = self.values[0]
        if "Staff" in selected:
            embed = discord.Embed(title="🌌 AR: Ultimate – Staff Roles", color=discord.Color.purple())
            embed.description = f"{staff_info_pt}\n\n{staff_info_en}"
        elif "Level" in selected:
            embed = discord.Embed(title="✨ AR: Ultimate – Level Roles", color=discord.Color.purple())
            embed.description = f"{level_info_pt}\n\n{level_info_en}"
        elif "Content" in selected:
            embed = discord.Embed(title="🌟 AR: Ultimate – Content Creator", color=discord.Color.purple())
            embed.description = f"{creator_info_pt}\n\n{creator_info_en}"

        embed.set_thumbnail(url=small_img)
        embed.set_image(url=large_img)
        await interaction.response.send_message(embed=embed, ephemeral=True)

# View persistente
class InfoView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(InfoDropdown())

@bot.event
async def on_ready():
    print(f"🤖 Bot conectado como {bot.user}")
    
    # Registrar a View persistente
    bot.add_view(InfoView())

    # Mensagem de confirmação no canal
    guild = bot.get_guild(1417591421518610505)  # substitua pelo ID do seu servidor
    if guild:
        canal = guild.get_channel(1418941828954194002)  # substitua pelo ID do seu canal
        if canal:
            await canal.send("🔄 Bot reiniciado e pronto! Dropdowns estão ativos 24/7. ✅")

# Comando !info
@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="AR: Ultimate – Server Information",
        description=(
            "✨ Welcome to our Server Information! Here you’ll find essential guidance about our hierarchy, perks, and opportunities.\n"
            "Whether you’re a new member or a longtime supporter, this resource will help you navigate and grow within Anime Revolution Ultimate. ✨\n\n"
            "**📌 Server Staff Roles**\n"
            "Info about Community Manager, Admin, Moderator, and Trial Moderator.\n\n"
            "**📌 Level Roles**\n"
            "Details about our leveling system and rewards as you become more active.\n\n"
            "**📌 Content Creator**\n"
            "Requirements and benefits of becoming an official Content Creator in AR: Ultimate.\n\n"
            "💡 Need help? Go to ⁠⌈📰・ticket-support for assistance.\n\n"
            "---\n\n"
            "**AR: Ultimate – Informações do Servidor**\n"
            "✨ Aqui você encontrará informações essenciais sobre nossa hierarquia, benefícios e oportunidades.\n"
            "Seja você novo ou veterano, este guia ajuda a crescer dentro do Anime Revolution Ultimate. ✨\n\n"
            "**📌 Cargos da Equipe**\n"
            "Informações sobre Community Manager, Admin, Moderador e Trial Moderador.\n\n"
            "**📌 Cargos de Nível**\n"
            "Detalhes sobre o sistema de níveis e recompensas por atividade.\n\n"
            "**📌 Criador de Conteúdo**\n"
            "Requisitos e benefícios para se tornar Criador de Conteúdo oficial.\n\n"
            "💡 Precisa de ajuda? Vá até ⁠⌈📰・ticket-support."
        ),
        color=discord.Color.purple()
    )
    embed.set_thumbnail(url=small_img)
    embed.set_image(url=large_img)

    await ctx.send(embed=embed, view=InfoView())
bot.run("MTQyNjc3ODEzNzI1MzExODA2Mw.GLFNt4.XOqdnRi_rVmyO1Mu_6dHIjNviQ5GreIBb8-LNI")
