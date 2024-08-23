from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router
import random

router = Router()
h = ['Hello', 'Hi', 'Good morning']
b = ['Bye', 'Take care', 'Goodbye']

@router.message(CommandStart())
async def cmd_star(message: Message):
    await message.answer(f"Hello {message.from_user.full_name}")

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("You can print Hello or Bye to get answer or send photo")

@router.message(F.photo)
async def get_photo(message: Message):
    await message.reply('Photo')

@router.message(F.text == "Hello")
async def answer_hello(message: Message):
    i = random.randint(0,2)
    await message.answer(h[i])

@router.message(F.text == "Good morning")
async def answer_hello(message: Message):
    i = random.randint(0,2)
    await message.answer(h[i])

@router.message(F.text == "Hi")
async def answer_hello(message: Message):
    i = random.randint(0,2)
    await message.answer(h[i])

@router.message(F.text == "Bye")
async def answer_hello(message: Message):
    i = random.randint(0,2)
    await message.answer(b[i])

@router.message(F.text == "Take care")
async def answer_hello(message: Message):
    i = random.randint(0,2)
    await message.answer(b[i])

@router.message(F.text == "Goodbye")
async def answer_hello(message: Message):
    i = random.randint(0,2)
    await message.answer(b[i])