import asyncio
from aiogram import Bot, types, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage

dp = Dispatcher(storage=MemoryStorage())
bot = Bot(token = "7078865117:AAH7of9ZvQ3KWREIGNvp2sEoe7rQtSrEHLM")

class Form(StatesGroup):
    name = State
    age = State

@dp.message(Command("start"))
async def handler(message: types.Message, state: FSMContext):
    await message.answer("Приветствую. Как дела?")
    await state.set_state(Form.name)

@dp.message(Form.name)
async def handler_name(message: types.Message, state: FSMContext):
    data = state.update_data(name= message.text)
    await message.answer(f"Привет, {data['name']}")

async def main():
    await dp.start_polling(bot)

if (__name__ == "__main__"):
    asyncio.run(main())