import discord
import os
from discord.ext import commands

# إعدادات البوت
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ البوت يعمل الآن باسم: {bot.user}')

@bot.command(name="say")
async def say(ctx):
    # إضافة المنشن في بداية الـ description بشكل عريض
    description_text = "**📢 تنبيه هام: @everyone | @here**\n\nأهلاً بك في سيرفرنا! نحن نضمن بيئة آمنة وممتعة للجميع.\nيرجى قراءة القوانين التالية بعناية لضمان تجربة مميزة."
    
    embed = discord.Embed(
        title="🛡️ نظام وقوانين السيرفر",
        description=description_text,
        color=discord.Color.from_rgb(47, 49, 54)
    )
    
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1C5sVTxubD9p2gSo-yBhU_hVaL4-f2IJNPd9o7KlE2A&s=10")
    
    embed.add_field(name="1️⃣ الاحترام والسلوك", value="الاحترام المتبادل أساس السيرفر.\nيمنع الهجوم الشخصي أو خطاب الكراهية.\n\n━━━━━━━━━━━━━━", inline=False)
    embed.add_field(name="2️⃣ إرشادات المحتوى", value="يمنع نشر المحتوى غير اللائق أو الإزعاج (Spam).\nأو الإشارات العشوائية لغير سبب.\n\n━━━━━━━━━━━━━━", inline=False)
    embed.add_field(name="3️⃣ الإعلانات", value="يمنع الترويج لأي سيرفرات أو منتجات خارجية.\nبدون إذن مسبق من الإدارة.\n\n━━━━━━━━━━━━━━", inline=False)
    embed.add_field(name="4️⃣ الخصوصية", value="أنت مسؤول عن أمن حسابك.\nويمنع مشاركة المعلومات الحساسة أو الشخصية.\n\n━━━━━━━━━━━━━━", inline=False)
    embed.add_field(name="5️⃣ العقوبات", value="مخالفة القوانين تعرضك للتحذير، الطرد، أو الحظر الدائم\nبناءً على شدة المخالفة.", inline=False)

    embed.set_footer(text=f"شكراً لتعاونكم | {ctx.guild.name}")

    await ctx.message.delete()
    await ctx.send(embed=embed)

# تأكد أن اسم المتغير في موقع الاستضافة هو TOKEN
bot.run(os.environ['TOKEN'])
