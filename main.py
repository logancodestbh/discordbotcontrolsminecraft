import discord
from discord.ext import commands
import pyautogui
import pynput.mouse
import asyncio
import time
import math

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

mouse = pynput.mouse.Controller()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

def move_smooth(xm, ym, t, rotation_angle=5):
    angle_limit = min(rotation_angle, 5)

    initial_position = mouse.position

    for i in range(t):
        mouse.move(xm, ym)
        time.sleep(1/60)

    dx = mouse.position[0] - initial_position[0]
    dy = mouse.position[1] - initial_position[1]

    mouse.move(-dx, -dy)

    angle = math.radians(angle_limit)

    rotated_position = (
        initial_position[0] + dx * math.cos(angle) - dy * math.sin(angle),
        initial_position[1] + dx * math.sin(angle) + dy * math.cos(angle)
    )

    mouse.position = rotated_position

@bot.command()
async def look_left(ctx, times: int = 1):
    times = min(times, 10)
    for _ in range(times):
        move_smooth(-10, 0, 40, rotation_angle=5)

@bot.command()
async def look_right(ctx, times: int = 1):
    times = min(times, 10)
    for _ in range(times):
        move_smooth(10, 0, 40, rotation_angle=5)

@bot.command()
async def look_up(ctx, times: int = 1):
    times = min(times, 10)
    for _ in range(times):
        move_smooth(0, -10, 40, rotation_angle=5)

@bot.command()
async def look_down(ctx, times: int = 1):
    times = min(times, 10)
    for _ in range(times):
        move_smooth(0, 10, 40, rotation_angle=5)

@bot.command()
async def w(ctx):
    pyautogui.keyDown('w')
    await asyncio.sleep(0.5)
    pyautogui.keyUp('w')

@bot.command()
async def s(ctx):
    pyautogui.keyDown('s')
    await asyncio.sleep(0.5)
    pyautogui.keyUp('s')

@bot.command()
async def d(ctx):
    pyautogui.keyDown('d')
    await asyncio.sleep(0.5)
    pyautogui.keyUp('d')

@bot.command()
async def a(ctx):
    pyautogui.keyDown('a')
    await asyncio.sleep(0.5)
    pyautogui.keyUp('a')

@bot.command()
async def lclick(ctx):
    pyautogui.click(button='left')

@bot.command()
async def inv(ctx):
    pyautogui.press('e')

@bot.command()
async def mouse_right(ctx, times: int = 1):
    times = min(times, 10)  # Limit the number of repetitions to 10
    for _ in range(times):
        pyautogui.move(50, 0, duration=0.5)

@bot.command()
async def mouse_left(ctx, times: int = 1):
    times = min(times, 10)
    for _ in range(times):
        pyautogui.move(-50, 0, duration=0.5)

@bot.command()
async def mouse_up(ctx, times: int = 1):
    times = min(times, 10)
    for _ in range(times):
        pyautogui.move(0, -50, duration=0.5)

@bot.command()
async def mouse_down(ctx, times: int = 1):
    times = min(times, 10)
    for _ in range(times):
        pyautogui.move(0, 50, duration=0.5)

@bot.command()
async def rclick(ctx):
    pyautogui.click(button='right')

@bot.command()
async def keypress(ctx, key: str):
    if key.lower() == 'esc':
        await ctx.send("Im not pressing the fucking esc key YOU WONT ESCAPE ME")
    else:
        pyautogui.press(key)

@bot.command()
async def jump(ctx):
    pyautogui.keyDown('space')
    await asyncio.sleep(0.5)
    pyautogui.keyUp('space')

bot.run('bot token here')

