import discord
import os
from discord import app_commands
from discord.ext import commands

# إعدادات البوت
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'تم تشغيل البوت بنجاح: {bot.user}')

@bot.tree.command(name="say", description="نشر قوانين السيرفر بتنسيق عصري واحترافي")
async def say(interaction: discord.Interaction):
    # إنشاء Embed بتنسيق متطور
    embed = discord.Embed(
        title="🛡️ نظام وقوانين السيرفر",
        description="أهلاً بك في سيرفرنا! نحن نضمن بيئة آمنة وممتعة للجميع. يرجى قراءة القوانين التالية بعناية لأن الالتزام بها أمر إلزامي.",
        color=discord.Color.from_rgb(47, 49, 54) # لون غامق مودرن (Dark Theme)
    )
    
    # إضافة صورة مصغرة (Thumbnails) تزيد من جمالية التصميم
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1C5sVTxubD9p2gSo-yBhU_hVaL4-f2IJNPd9o7KlE2A&s=10") # ضع رابط شعار سيرفرك هنا

    # استخدام الحقول (Fields) بدلاً من النص الطويل لجعل التصميم منظم
    embed.add_field(name="1️⃣ السلوك والاحترام", value="الاحترام المتبادل أساس السيرفر. يمنع منعاً باتاً الهجوم الشخصي أو خطاب الكراهية.", inline=False)
    embed.add_field(name="2️⃣ إرشادات المحتوى", value="يمنع نشر المحتوى غير اللائق أو الإزعاج (Spam) أو الإشارات العشوائية.", inline=False)
    embed.add_field(name="3️⃣ الإعلانات", value="يمنع الترويج لأي سيرفرات أو منتجات خارجية بدون إذن مسبق من الإدارة.", inline=False)
    embed.add_field(name="4️⃣ الخصوصية", value="أنت مسؤول عن أمن حسابك، ويمنع مشاركة المعلومات الحساسة أو الحسابات.", inline=False)
    embed.add_field(name="5️⃣ العقوبات", value="مخالفة القوانين تعرضك للتحذير، الطرد، أو الحظر الدائم حسب نوع المخالفة.", inline=False)

    # إضافة تذييل (Footer) احترافي
    embed.set_footer(text="شكراً لالتزامك بقوانيننا | نعتز بوجودك معنا", icon_url=interaction.guild.icon.url if interaction.guild.icon else None)

    # إرسال الرسالة
    await interaction.response.send_message(embed=embed)

# ضع التوكن هنا
bot.run(os.environ['TOKEN'])
