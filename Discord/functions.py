from dotenv import load_dotenv
import os

from datetime import datetime
import requests
import discord


load_dotenv(os.path.join(os.getcwd(), '.env\.env'))


async def send_discord_webhook(swap_infos: dict):
    """
    Posts a Discord message containing all the swap informations using Webhook URL specificed in specificed in .env/.env
    
    Parameters:
        ``swap_infos (dict)``: dictionnary containing all the informations from the swap, e.g. tokens names, amounts swapped, transaction link...
    """
    embed = discord.Embed(
        title=f":sparkles: {swap_infos['CHAIN']} - {swap_infos['MAKER_INFOS']['SHORT_ADDRESS']}",
        color=discord.Color.green(),
        timestamp=datetime.now(),
        url=swap_infos['LINKS']['SCAN']['TRANSACTION'],
        description=(
            f"**:bust_in_silhouette: [{swap_infos['MAKER_INFOS']['SHORT_ADDRESS']}]({swap_infos['LINKS']['SCAN']['MAKER']})\n" +
            f":scroll: [TX]({swap_infos['LINKS']['SCAN']['TRANSACTION']})**"
        )
    )
    
    for swap_id, swap_infos in swap_infos['SWAPS'].items():
        emoji_swap_id = await get_emoji_swap_id(swap_id=swap_id)
        swap_title = (
            "\n\u200B\n" +
            f"{emoji_swap_id} SWAP {swap_infos['SYMBOLS']['TOKEN0']} » {swap_infos['SYMBOLS']['TOKEN1']}"
        )
        swap_content = (
            f"**> :dollar: {swap_infos['AMOUNTS']['TOKEN0']} ${swap_infos['SYMBOLS']['TOKEN0']} » {swap_infos['AMOUNTS']['TOKEN1']} ${swap_infos['SYMBOLS']['TOKEN1']}\n" +
            f"> :bar_chart: [CHART/TRADING]({swap_infos['LINKS']['CHART']})\n**"
        ) 
        embed.add_field(
            name=swap_title,
            value=swap_content,
            inline=False
        )
    
    try:
        requests.post(os.getenv("DISCORD_WEBHOOK_URL"), json={"embeds": [embed.to_dict()]}, headers={'Content-Type': 'application/json'})
    except:
        print("[!] Couldn't send discord webhook message.")
        

async def get_emoji_swap_id(swap_id: int) -> str:
    """
    Returns an emoji for the swap ID.
    
    Parameters:
        ``swap_id (int)``: id of the swap
    """
    
    swap_id_emoji = (
        ":one:" if swap_id == 1 else
        ":two:" if swap_id == 2 else
        ":three:" if swap_id == 3 else
        ":four:" if swap_id == 4 else
        ":five:" if swap_id == 5 else
        ":six:" if swap_id == 6 else
        ":seven:" if swap_id == 7 else
        ":eight:" if swap_id == 8 else
        ":nine:" if swap_id == 9 else
        ":one::zero:" if swap_id == 10 else
        ":one::one:" if swap_id == 11 else
        ":one::two:" if swap_id == 12 else
        ":one::three:" if swap_id == 13 else
        ":one::four:" if swap_id == 14 else
        ":one::five:" if swap_id == 15 else
        ":one::six:" if swap_id == 16 else
        ":one::seven:" if swap_id == 17 else
        ":one::eight:" if swap_id == 18 else
        ":one::nine:" if swap_id == 19 else
        ":two::zero:" if swap_id == 20 else
        ":1234:"
    )
    return swap_id_emoji