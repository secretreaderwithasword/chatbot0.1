from aiogram import Router, F, types
router = Router()
@router.message(F.text.lower() == "как дела")
async def answer_to_how(message: types.Message):
    await message.answer(f" {message.from_user.full_name}, всё отлично!")

