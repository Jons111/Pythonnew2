from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.tasdiqlash import tasdiq
from loader import dp, bot
from states.holatlar import Murojat

# Echo bot
@dp.message_handler(text='Murojat')
async def bot_echo(message: types.Message):
    await message.answer(text='Ismni kiriting')
    await Murojat.ism_qabul_qilish_holat.set()
@dp.message_handler(state=Murojat.ism_qabul_qilish_holat)
async def bot_echo(message: types.Message,state:FSMContext):
    ism = message.text
    await state.update_data({'name':ism})
    await message.answer(text='Familyani kiriting ')
    await Murojat.fam_qabul_qilish_holat.set()

@dp.message_handler(state=Murojat.fam_qabul_qilish_holat)
async def bot_echo(message: types.Message,state:FSMContext):
    familya = message.text
    await state.update_data({'fam':familya})
    await message.answer(text='Yoshni kiriting ')
    await Murojat.yosh_qabul_qilish_holat.set()


@dp.message_handler(state=Murojat.yosh_qabul_qilish_holat)
async def bot_echo(message: types.Message,state:FSMContext):
    yosh = message.text
    await state.update_data({'age':yosh})
    await message.answer(text='manzili kiriting ')
    await Murojat.manzil_qabul_qilish_holat.set()

@dp.message_handler(state=Murojat.manzil_qabul_qilish_holat)
async def bot_echo(message: types.Message,state:FSMContext):
    manzil= message.text
    await state.update_data({'shaxar':manzil})
    await message.answer(text='Adminga murojatingizni  kiriting ')
    await Murojat.murojat_qabul_qilish_holat.set()

@dp.message_handler(state=Murojat.murojat_qabul_qilish_holat)
async def bot_echo(message: types.Message,state:FSMContext):
    matn= message.text
    await state.update_data({'matn':matn})
    malumotlar = await state.get_data()
    ism = malumotlar.get('name')
    fam = malumotlar.get('fam')
    yosh = malumotlar.get('age')
    manzil = malumotlar.get('shaxar')

    s = f"🏅 Ism : {ism}\n" \
        f"👤 Famila : {fam}\n" \
        f"👨‍💻 Yosh : {yosh}\n" \
        f"🌐 Manzil : {manzil}\n" \
        f"🔎 Murojat : {matn}"
    await message.answer(text=s,reply_markup=tasdiq)
    await Murojat.tasdiqlashni_qabul_qilish_holat.set()

@dp.message_handler(text ='Tasdiqlash',state=Murojat.tasdiqlashni_qabul_qilish_holat)
async def bot_echo(message: types.Message,state:FSMContext):
    malumotlar = await state.get_data()
    ism = malumotlar.get('name')
    fam = malumotlar.get('fam')
    yosh = malumotlar.get('age')
    manzil = malumotlar.get('shaxar')
    matn = malumotlar.get('matn')
    s ='Ushbu foydalanuvchi quyidagi habarni yubordi\n '
    s += f"🏅 Ism : {ism}\n" \
        f"👤 Famila : {fam}\n" \
        f"👨‍💻 Yosh : {yosh}\n" \
        f"🌐 Manzil : {manzil}\n" \
        f"🔎 Murojat : {matn}"

    await bot.send_message(chat_id=1892438581,text=s)
    await state.finish()