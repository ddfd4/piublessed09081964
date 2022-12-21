import os
import discord
from discord.ext import commands
import asyncio
from asyncio import sleep
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import random

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)

global p 
p = 1

@bot.command()
@has_permissions(administrator = True)
async def tour_comanda(ctx, member1: discord.Member = None,member2: discord.Member= None, member3:discord.Member= None,*, nameCommand):
    role = await ctx.guild.create_role(name=nameCommand)
    await member1.add_roles(role)
    await member2.add_roles(role)
    await member3.add_roles(role)
    await ctx.send(embed = discord.Embed(title = "Готово", colour=1752220))
    
@bot.command()
@has_permissions(administrator = True)
async def tour(ctx,time = None, role1: discord.Role = None,role2: discord.Role = None,role3: discord.Role = None,role4: discord.Role = None,role5: discord.Role = None,role6: discord.Role = None, role7: discord.Role = None, role8: discord.Role = None,role9: discord.Role = None,role10: discord.Role = None,role11: discord.Role = None,role12: discord.Role = None,role13: discord.Role = None,role14: discord.Role = None,role15: discord.Role = None,role16: discord.Role = None):
    global p 
    p+=1
    cat = await ctx.guild.create_category(f"Tourney №{p}")
    time = int(time)
    t1 = await ctx.guild.create_text_channel('╭⟦🥑⟧-𝐂𝐡𝐚𝐭', category=cat)
    t2 = await ctx.guild.create_text_channel('┊⟦📗⟧-𝐓𝐚𝐜𝐭𝐢𝐜', category=cat)
    v1 = await ctx.guild.create_voice_channel('╰⟦🦄⟧-𝐕𝐨𝐢𝐜𝐞', category=cat)
    ever = discord.utils.get(ctx.message.guild.roles, name = "@everyone")
    try:
        await cat.set_permissions(role1, view_channel = True)
        await cat.set_permissions(role2, view_channel = True)
        await cat.set_permissions(role3, view_channel = True)
        await cat.set_permissions(role4, view_channel = True)
        await cat.set_permissions(role5, view_channel = True)
        await cat.set_permissions(role6, view_channel = True)
        await cat.set_permissions(role7, view_channel = True)
        await cat.set_permissions(role8, view_channel = True)
        await cat.set_permissions(role9, view_channel = True)
        await cat.set_permissions(role10, view_channel = True)
        await cat.set_permissions(role11, view_channel = True)
        await cat.set_permissions(role12, view_channel = True)
        await cat.set_permissions(role13, view_channel = True)
        await cat.set_permissions(role14, view_channel = True)
        await cat.set_permissions(role15, view_channel = True)
        await cat.set_permissions(role16, view_channel = True)
    except:
        pass
    await cat.set_permissions(ever, view_channel = False)
    await ctx.send(discord.Embed(title = "Готово", colour=1752220))
    await asyncio.sleep(time*3600)
    try:
        await cat.delete()
        await t1.delete()
        await t2.delete()
        await v1.delete()
        await role1.delete()
        await role2.delete()
        await role3.delete()
        await role4.delete()
        await role5.delete()
        await role6.delete()
        await role7.delete()
        await role8.delete()
        await role9.delete()
        await role10.delete()
        await role11.delete()
        await role12.delete()
        await role13.delete()
        await role14.delete()
        await role15.delete()
        await role16.delete()
        await ctx.send(embed = discord.Embed(title = "Время турнира истекло", colour=1752220))
    except:
        pass
    
        

bot.run("MTAyMDY2Mjg3Mzc5MTQwNjE2Mw.G0qcvj.HEms9M4zJgsYtFo4hhIj6INGYM6yg5NaEQbdaQ")