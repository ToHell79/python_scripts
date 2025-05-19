import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command

#формируем заказ
order = []

# Вставь сюда токен от @BotFather
API_TOKEN = '7690934306:AAE1M_trc0I0lTs2LrjnQrsF9DKpiySuT50'

# Создаем бота и диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Кнопки
onStartMenu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Пироги 👋", callback_data="pies")],
    [InlineKeyboardButton(text="Суши 👋", callback_data="sushi")],
    [InlineKeyboardButton(text="Пицца 👋", callback_data="pizza")]
])

onPiesMenu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Сытные 👋", callback_data="satisfying")],
    [InlineKeyboardButton(text="Сладкие 👋", callback_data="sweet")]
])

onSatisfyingPies = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="С мясом 👋", callback_data="pie_meat")],
    [InlineKeyboardButton(text="С кроликом", callback_data="pie_rabbit")],
    [InlineKeyboardButton(text="С капустой", callback_data="pie_cabbage")],
    [InlineKeyboardButton(text="С рыбой", callback_data="pie_fish")],
    [InlineKeyboardButton(text="С картошкой", callback_data="pie_potato")]
])

onSweetPies = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="С творогом", callback_data="pie_curd")],
    [InlineKeyboardButton(text="С ягодой", callback_data="pie_berry")],
    [InlineKeyboardButton(text="С лимоном", callback_data="pie_lemon")],
    [InlineKeyboardButton(text="С яблоками", callback_data="pie_apple")]
])

onPizzaMenu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Маргарита 👋", callback_data="margarita")],
    [InlineKeyboardButton(text="Пеперони", callback_data="peperonni")],
    [InlineKeyboardButton(text="4 Сезона", callback_data="4sezon")],
    [InlineKeyboardButton(text="Гавайская", callback_data="hawaiy")]
])

onNamePizza = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Маленькая 👋", callback_data="small")],
    [InlineKeyboardButton(text="Среднияя 👋", callback_data="middle")],
    [InlineKeyboardButton(text="Большая 👋", callback_data="big")]
])

onSushiMenu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Роллы 👋", callback_data="roll")],
    [InlineKeyboardButton(text="Супы 👋", callback_data="soup")],
    [InlineKeyboardButton(text="Коробочки 👋", callback_data="box")]
])

onRollSushi = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Филадельфия", callback_data="filadelfiya")],
    [InlineKeyboardButton(text="Калифорния", callback_data="californiya")],
    [InlineKeyboardButton(text="С огурцом", callback_data="cucumber")]
])

onSoupSushi = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Мисо", callback_data="miso")],
    [InlineKeyboardButton(text="Кимчи", callback_data="kimchi")],
    [InlineKeyboardButton(text="Куриный", callback_data="chicken")]
])

onBoxSushi = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Классический", callback_data="classic")],
    [InlineKeyboardButton(text="С рисом", callback_data="with_ris")],
    [InlineKeyboardButton(text="Вок Том Ян", callback_data="box_tom_yan")]
])

onOrderMenu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Подтвердить", callback_data="make_order")],
    [InlineKeyboardButton(text="Заново", callback_data="cancel_order")]
])

# Обработчик команды /start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Скатерть-Самобранка приветствует тебя! Что, изволите?!", reply_markup=onStartMenu)

# Обработчик команды /bla
"""@dp.message(Command("bla"))
async def start_handler(message: types.Message):
    await message.answer("Скатерть-Самобранка приветствует тебя! Что, изволите?!", reply_markup=keyboard)"""

# Обработчик кнопок
@dp.callback_query()
async def callback_handler(callback: types.CallbackQuery):
    data = callback.data

    if data == "pies":
        await callback.message.delete()
        await callback.message.answer("Вы выбрали пироги, теперь чуть конкретнее:👋", reply_markup=onPiesMenu)
        order.append("Пирог")
    elif data == "sushi":
        #await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.delete()
        await callback.message.answer("Вы выбрали суши, теперь чуть конкретнее:👋", reply_markup=onSushiMenu)
        order.append("Суши")
    elif data == "pizza":
        await callback.message.delete()
        await callback.message.answer("Вы выбрали пиццу, теперь чуть конкретнее:👋", reply_markup=onPizzaMenu)
        order.append("Пицца")
    elif data == "small":
        await callback.message.delete()
        order.append("маленькая")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "middle":
        await callback.message.delete()
        order.append("средняя")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "big":
        await callback.message.delete()
        order.append("большая")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "margarita":
        await callback.message.delete()
        await callback.message.answer("а размер:", reply_markup=onNamePizza)
        order.append("маргарита")
    elif data == "peperonni":
        await callback.message.delete()
        await callback.message.answer("а размер:", reply_markup=onNamePizza)
        order.append("пеперони")
    elif data == "4sezon":
        await callback.message.delete()
        await callback.message.answer("а размер:", reply_markup=onNamePizza)
        order.append("4 сезона")
    elif data == "hawaiy":
        await callback.message.delete()
        await callback.message.answer("а размер:", reply_markup=onNamePizza)
        order.append("Гавайская")
    elif data == "satisfying":
        await  callback.message.delete()
        await  callback.message.answer("ну какой же выбрать:", reply_markup=onSatisfyingPies)
    elif data == "sweet":
        await  callback.message.delete()
        await  callback.message.answer("ну какой же выбрать:", reply_markup=onSweetPies)
    elif data == "pie_meat":
        await callback.message.delete()
        order.append("с мясом")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "pie_rabbit":
        await callback.message.delete()
        order.append("с кроликом")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "pie_cabbage":
        await callback.message.delete()
        order.append("с капустой")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "pie_fish":
        await callback.message.delete()
        order.append("с рыбой")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "pie_potato":
        await callback.message.delete()
        order.append("с картошкой")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "pie_curd":
        await callback.message.delete()
        order.append("с творогом")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "pie_berry":
        await callback.message.delete()
        order.append("с ягодой")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "pie_lemon":
        await callback.message.delete()
        order.append("с лимоном")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "pie_apple":
        await callback.message.delete()
        order.append("С яблоками")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "roll":
        await  callback.message.delete()
        await  callback.message.answer("ну что же выбрать:", reply_markup=onRollSushi)
        order.append("ролл")
    elif data == "soup":
        await  callback.message.delete()
        await  callback.message.answer("ну что же выбрать:", reply_markup=onSoupSushi)
        order.append("суп")
    elif data == "box":
        await  callback.message.delete()
        await  callback.message.answer("ну что же выбрать:", reply_markup=onBoxSushi)
        order.append("вок")
    elif data == "filadelfiya":
        await callback.message.delete()
        order.append("калифорния")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "californiya":
        await callback.message.delete()
        order.append("филадельфия")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "cucumber":
        await callback.message.delete()
        order.append("с огурцом")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "miso":
        await callback.message.delete()
        order.append("мисо")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "kimchi":
        await callback.message.delete()
        order.append("кимчи")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "chicken":
        await callback.message.delete()
        order.append("куриный")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "classic":
        await callback.message.delete()
        order.append("классический")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "with_ris":
        await callback.message.delete()
        order.append("с рисом")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "box_tom_yan":
        await callback.message.delete()
        order.append("Том Ян")
        await callback.message.answer(" ".join(order), reply_markup=onOrderMenu)
    elif data == "make_order":
        await callback.message.delete()
        await callback.message.answer("Заказ оформлен! Может еще ;)", reply_markup=onStartMenu)
        order.clear()
    elif data == "cancel_order":
        await callback.message.delete()
        order.clear()
        await callback.message.answer("Выберу другое:", reply_markup=onStartMenu)
    await callback.answer()  # Обязательно, чтобы Telegram не крутил "часики"

# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())