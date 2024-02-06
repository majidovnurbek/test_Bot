import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command
from config import Tokens
from button import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=Tokens)
dp = Dispatcher()
a=0
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(f"xush kelibsiz bizning test botimizga bu yerda siz\npython dasturlash tilidan test yechasiz! ")


@dp.message(Command("first_test"))
async def cmd_start(message: Message):
    await message.answer(f"pythonda nima orqali ekranga chop etamiz ", reply_markup=catalog)


###############################################################################################
@dp.callback_query(F.data == "c")
async def check_button(callback: CallbackQuery):
    await callback.message.answer("Siz to'g'ri topdingiz ✅!", )
    for x in callback.message.text.split():
        x+=a
        await callback.message.answer(f"{a}")



#####################################################################################
@dp.callback_query(F.data == "b" or F.data == "a" or F.data == "d")
async def check_button(callback: CallbackQuery):
    await callback.message.answer("Siz no'g'ri topdingiz ❗️!")



##################################2-SAVOL#############################################
@dp.callback_query(F.data == "e")
async def check_button(callback: CallbackQuery):
    await callback.message.answer("2.	Venv ni qanday yaratish mumkin?",reply_markup=test2)

###############################################################

@dp.callback_query(F.data == "t")
async def check_button(callback: CallbackQuery):
    await callback.message.answer("Siz to'g'ri topdingiz ✅!", )
##########################################################################
@dp.callback_query(F.data == "d" or F.data == "h" or F.data == "test1")
async def check_button(callback: CallbackQuery):
    await callback.message.answer("Siz no'g'ri topdingiz ❗️!")
######################################################################
@dp.callback_query(F.data == "r")
async def check_button(callback: CallbackQuery):
    await callback.message.answer("3.Serverdagi ma'lumot olish uchun qanday URL so'rov ishlatiladi",reply_markup=test3)
#########################################################################################################################
@dp.callback_query(F.data == "de")
async def check_button(callback: CallbackQuery):
    await callback.message.answer("Siz to'g'ri topdingiz ✅!", )
##############################################################################################################
@dp.callback_query(F.data == "test3" or F.data == "he" or F.data == "te")
async def check_button(callback: CallbackQuery):
    await callback.message.answer("Siz no'g'ri topdingiz ❗️!")
################################################################
@dp.callback_query(F.data == "l")
async def check_button(callback: CallbackQuery):
    await callback.message.answer("4.	 HTTP status 200 kodi nima degani",reply_markup=test4)
########################################################
@dp.callback_query(F.data == "test4")
async def check_button(callback: CallbackQuery):
    await callback.message.answer("Siz to'g'ri topdingiz ✅!", )
#####################################################################################
@dp.callback_query(F.data == "ded" or F.data == "heh" or F.data == "tet")
async def check_button(callback: CallbackQuery):
    await callback.message.answer("Siz no'g'ri topdingiz ❗️!")
#############################################################################
@dp.callback_query(F.data == "p")
async def check_button(callback: CallbackQuery):
    await callback.message.answer("11.	Fayllarni ochish qanday funksiyasi bilan amalga oshadi?",reply_markup=test5)
#################################################################################
@dp.callback_query(F.data == "dedd")
async def check_button(callback: CallbackQuery):
    await callback.message.answer("Siz to'g'ri topdingiz ✅!", )
###################################################################################
@dp.callback_query(F.data == "tett" or F.data == "hehh" or F.data == "test45")
async def check_button(callback: CallbackQuery):
    await callback.message.answer("Siz no'g'ri topdingiz ❗️!")

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
