from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox
from math import*
import datetime
import calendar
import time
import webbrowser
# *********************************************
startCode = time.time()
def timing():
    current_time = time.strftime("%H : %M : %S")
    clock.config(text=current_time)
    clock.after(200, timing)
    
def telegrammbot(event):
    webbrowser.open_new(r"https://t.me/PocketCombatsbot")

def callback(event):
    webbrowser.open_new(r"https://t.me/pocketcombats_chat")
    
def exit2():
    choise = messagebox.askyesno("", "Вы точно хотите выйти?")
    if choise:
        root.destroy()
        
def bot():
    messagebox.showinfo("", "\nПо вопросам телеграмм-бота\nписать @PocketYa")
        
def firmado():
    messagebox.showinfo("", "\nВы можете найти\nменя в телеграмме\n@Firmado")

def version():
    messagebox.showinfo("", "\nВерсия 1.21\nот 01.05.2022")

def nuance():
    messagebox.showinfo("", """Нюансы работы калькулятора:\n◦Если вы свернули калькуля-\nтор, а потом возобновили работу,\nто для активации клавиатуры\nнеобходимо один раз нажать на\nкнопку ◀ на клавиатуре\nтелефона.\n◦Погрешность при вычислении\nуровня жизни.\n◦Погрешность при вычислении\n Исцеления.""")
        
def instruction():
    messagebox.showinfo("", """‌◦Внимание!!! Для рассчёта \nатрибутов все поля характерис-\nтик должны быть заполнены.\nЕсли нет необходимости рассчи-\nтывать характеристику, ставим\nпросто единицу.\n◦Для "Броска щитом"\nзаполняем интуицию, живучесть\nи уровень заточки щита, если \nщит без заточки, ставим ноль.\n◦Для "Исцеления" заполняем\nуровень, интуицию, мудрость,\nурон от Света, заточку посоха,\nмин. и макс. магический урон,\nи выбираем необходимый нам\nпосох.\n◦Для рассчёта жизни и маны\nзаполняем уровень, живучесть и \nмудрость.\n◦Для рассчёта уворота и мет-\nкости заполняем уровень,\nловкость,интуицию и удачу.\n◦Для благословения оружия\nзаполняем интуицию и мудрость.""")
# *********************************************
root=Tk()
mainmenu = Menu(root, font="Times 10 bold", activebackground="#59b5f2")
root.config(menu = mainmenu)
#*****
instructionmenu = Menu(mainmenu, activebackground="#59b5f2")
instructionmenu.add_separator()
instructionmenu.add_command(label="Как заполнять поля?",font="Times 9 bold", command = instruction)
instructionmenu.add_separator()
instructionmenu.add_command(label="Нюанс работы калькулятора", font="Times 9 bold", command = nuance)
#*****
infomenu = Menu(mainmenu, activebackground="#59b5f2")
infomenu.add_separator()
infomenu.add_command(label="Версия программы", font="Times 9 bold", command = version)
infomenu.add_separator()
infomenu.add_command(label="Об авторе", font="Times 9 bold", command = firmado)
infomenu.add_separator()
infomenu.add_command(label="Телеграмм-бот", font="Times 9 bold", command = bot)
#*****
exitmenu = Menu(mainmenu, activebackground="#59b5f2")
exitmenu.add_separator()
exitmenu.add_command(label="Выход", font="Times 9 bold", command = exit2)
#*****
mainmenu.add_cascade(label="Инструкция", menu = instructionmenu)
mainmenu.add_cascade(label=" О программе", menu = infomenu)
mainmenu.add_cascade(label="  Выход", menu = exitmenu)
#**********************************************
WIDTH=1080
HEIGHT=2400

POS_X=root.winfo_screenwidth()//2-WIDTH//2
POS_Y=root.winfo_screenheight()//2-HEIGHT//2
root.title("Калькулятор PocketCombats")
root.resizable( False, False)
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")
#****
labelStrength=Label(text="Сила: ")
labelStrength.place(x=20, y=360)

labelDexterity=Label(text="Ловкость:")
labelDexterity.place(x=20, y=430)

labelIntuition=Label(text="Интуиция:")
labelIntuition.place(x=20, y=500)

labelEndurance=Label(text="Живучесть: ")
labelEndurance.place(x=20, y=570)

labelWisdom=Label(text="Мудрость: ")
labelWisdom.place(x=20 , y=640)

labelLuck=Label(text="Удача: ")
labelLuck.place(x=20 , y=710)

labelLevel=Label(text="Ваш уровень: ")
labelLevel.place(x=20, y=100)

labelAttribute=Label(text="Нераспред. атрибуты: ", font="arial 6")
labelAttribute.place(x=20 , y=270)

restAttribute = Label(text="Осталось атрибутов: ", font="arial 6")
restAttribute.place(x=38, y=310)
# Выбор профессии
prof = IntVar()
prof.set(0)

mage = Radiobutton(text="Маг", variable = prof, value = 0)
mage.place(x=600, y=395)

warrior = Radiobutton(text="Воин", variable = prof, value = 1)
warrior.place(x=600, y=465)

hunter = Radiobutton(text="Охотник", variable = prof, value = 2)
hunter.place(x=600, y=535)

newbie = Radiobutton(text="Новичок", variable = prof, value = 3)
newbie.place(x=600, y=605)

stakanov = Radiobutton(text="Стаканов", variable = prof, value = 4, command = exit)
stakanov.place(x=600, y=675)
# Двуручное оружие союзника
twoHanded = IntVar()
twoHanded.set(0)

twoHanded_checkbutton = Checkbutton(text="Союзник с двуруч. оружием", font="arial 7", variable = twoHanded)
twoHanded_checkbutton.place(x=470, y=1695)
# Руна жизнетока
runeLifecurrent = IntVar()
runeLifecurrent.set(0)

runeLifecurrent_checkbutton = Checkbutton(text="Руна жизнетока", font="arial 8", variable = runeLifecurrent, bd=5)
runeLifecurrent_checkbutton.place(x=550, y=1255)
# Посох целителя
staffHealers = IntVar()
staffHealers.set(0)

staffHealers_checkbutton = Checkbutton(text="Посох целителя", font="arial 8", variable = staffHealers, bd= 5)
staffHealers_checkbutton.place(x=550, y=1320)
# Посох Благословение
staffBlessing = IntVar()
staffBlessing.set(0)

staffBlessing_checkbutton = Checkbutton(text="Благословение", font="arial 8", variable = staffBlessing, bd =5)
staffBlessing_checkbutton.place(x=550, y=1385)
# Бросок щита
shieldSharp = Label (text="Заточка щита:")
shieldSharp.place(x=20, y=900)
# Урон броска щита
damageShield = Label (text="Урон щита: ")
damageShield.place(x=20, y=970)
# maxHP
health = Label (text=": ")
health.place(x=785, y=915)
# maxMana
urMana = Label(text=": ")
urMana.place(x=785, y=1055)
# Уклонение
dodgeLabel = Label(text="Уклон/Меткость:", font = "arial 7" )
dodgeLabel.place(x=550, y=1170)
# Броня
armorLabel = Label(text="Физический урон\nуменьшен на, % :__", font="arial 7")
armorLabel.place(x=550, y=1935)
# УВС
uvsLabel = Label(text="Увеличивает урон в ___ раз.", font="arial 8")
uvsLabel.place(x=360, y=1855)
# Благословение оружием
blessingLabel = Label(text="Урон Светом увеличен на: __", font="arial 8")
blessingLabel.place(x=20, y=1770)
# Урон от света
lightLabel = Label(text="Урон от Света: ", font="arial 8")
lightLabel.place(x=20, y=1265)
# Исцеление
healingLabel = Label(text=": ")
healingLabel.place(x=330, y=1590)
# Заточка посоха
staffSharpeningLabel = Label(text="Заточка\nпосоха:")
staffSharpeningLabel.place(x=20, y=1320)
#*****
minMagicDamageLabel = Label(text="Мин.маг.урон:")
minMagicDamageLabel.place(x=20, y=1430)
#*****
maxMagicDamageLabel = Label(text="Макс.маг.урон:")
maxMagicDamageLabel.place(x=20, y=1500)
#******
attribute = 0
maxHP = 0
sumMana = 0
level = StringVar()
strength = StringVar()
dexterity = StringVar()
intuition = StringVar()
endurance = StringVar()
wisdom = StringVar()
luck = StringVar()
shield = StringVar()

# Сохранить/Загрузить
def download():
    char = [level, strength, dexterity, intuition, endurance, wisdom, luck, shield, armor, lightEntry, staffSharpeningEntry, minMagicDamageEntry, maxMagicDamageEntry]
    try:
        charList = open("charList.dat", "r", encoding="utf-8")
        for i, line in enumerate(charList):
            char[i].delete(0, "end")
            char[i].insert(0, line[:-1])
        charList.close()                       
    except:
        messagebox.showwarning("", "\nЧто-то пошло не так!")
#*********************************************
def saveBuild():
    char = [level.get(), strength.get(), dexterity.get(), intuition.get(), endurance.get(), wisdom.get(), luck.get(), shield.get(), armor.get(), lightEntry.get(), staffSharpeningEntry.get(), minMagicDamageEntry.get(), maxMagicDamageEntry.get()]
    try:
        charList = open("charList.dat", "w", encoding="utf-8")
        for i in char:
            charList.write(i)
            charList.write("\n")
        charList.close()
    except:
        messagebox.showwarning("", "\nЧто-то пошло не так!")
    return char      
#*******
def uvs():
    global uvsLabel
    dexterity_ = int(dexterity.get())
    uvs = format((450 + 10 * dexterity_)/(450 + dexterity_), '.2f')
    uvsLabel["text"] = f"Увеличивает урон в {uvs} раз."
       
def dodge():
    global dodgeLabel
    level_ = int(level.get())
    dexterity_ = int(dexterity.get())
    intuition_ = int(intuition.get())
    luck_ = int(luck.get())
    
    dodge = 100 + level_ + dexterity_ + floor(luck_ *0.2)
    accuracy = 175 + level_ + intuition_ + floor(luck_ /3)
    dodgeLabel["text"] = f"Уклон/Меткость: {dodge}/{accuracy}"
    
def armor():
    global armorLabel
    armor_ = int(armor.get())
    armor2 = round(100 *(1-((4000+armor_)/((4000+armor_ * 10)))))
    
    armorLabel["text"] = f"Физический урон\nуменьшен на, % :{armor2}"
    
def blessingWeapon():
    global blessingLabel
    intuition_ = int(intuition.get())
    wisdom_ = int(wisdom.get())
    twoHanded_ = int(twoHanded.get())
    blessing = 5 + (wisdom_ + (intuition_/2)-38)/2
    if(blessing<=5):
        blessing = 5
    elif(blessing >=50):
        blessing = 50
    if twoHanded.get() == 1:
        blessing = blessing + (blessing * 50)/100
        if(blessing <=5):
            blessing = 5
        elif(blessing >= 75):
            blessing = 75
    
    blessingLabel["text"] = f"Урон Светом увеличен на: {blessing}"
  
def healing():
   global healingLabel
   level_ = int(level.get())
   intuition_ = int(intuition.get())
   wisdom_ = int(wisdom.get())
   lightEntry_ = int(lightEntry.get())
   runeLifecurrent_ = int(runeLifecurrent.get())
   staffHealers_ = int(staffHealers.get())
   staffBlessing_ = int(staffBlessing.get())
   staffSharpeningEntry_ = int(staffSharpeningEntry.get())
   minMagicDamageEntry_ = int(minMagicDamageEntry.get())
   maxMagicDamageEntry_ = int(maxMagicDamageEntry.get())
   
   minheal = round(4 *(level_ + (intuition_ + wisdom_)/3))
   minheal = round(minheal + (minheal *(lightEntry_ /100)))
   if staffHealers.get() == 1:
       minheal = round(minheal + (minheal * (staffSharpeningEntry_ * 0.025) + minMagicDamageEntry_))
       if runeLifecurrent.get()==1:
           minheal = round(minheal + (minheal * 30)/100)

   if staffBlessing.get() == 1:
        minheal = round(minheal + (minheal * (staffSharpeningEntry_ * 0.05) + minMagicDamageEntry_))
        if runeLifecurrent.get()==1:
            minheal = round(minheal + (minheal * 30)/100)
       
   maxheal = round(4 *(level_ + (intuition_ + wisdom_)/2))
   maxheal = round(maxheal + (maxheal *(lightEntry_ /100)))
   if staffHealers.get() == 1:
       maxheal = round(maxheal + (maxheal * (staffSharpeningEntry_ * 0.025) + maxMagicDamageEntry_))
       if runeLifecurrent.get()==1:
           maxheal = round(maxheal + (maxheal * 30)/100)
       
   if staffBlessing.get() == 1:
        maxheal = round(maxheal + (maxheal * (staffSharpeningEntry_ * 0.05) + maxMagicDamageEntry_))
        if runeLifecurrent.get()==1:
                 maxheal = round(maxheal + (maxheal*30)/100)
                 
   healingLabel["text"] = f": {minheal}-{maxheal}"
      
def manaCalc():
    global urMana
    level_ = int(level.get())
    wisdom_ = int(wisdom.get())
    prof_ = int(prof.get())
    koefMana = (100 + wisdom_)/100
    
    if prof.get() == 0:
        if(level_ <= 70):
            sumMana = (8 + level_ *5)*koefMana
        else:
            sumMana = (8 + level_ *7)*koefMana
            
    if prof.get() == 1 or prof.get() == 2:
        if(level_ <= 70):
            sumMana = (8 + level_ *2)*koefMana
        else:
            sumMana = (8 + level_ *3)*koefMana
          
    if prof.get() == 3:
            sumMana = (8 + level_ )*koefMana
             
    sumMana = floor(sumMana)       
    urMana["text"] = f": {sumMana}"

def healthMax():
    global maxHP
    level_ = int(level.get())
    endurance_ = int(endurance.get())
    prof_ = int(prof.get())
  
    base = floor(int(35 + level_ * 5))

    maxHp = 1
    if prof_ == 0:
        if level_ <= 70:
            for i in range(2, level_ +1):
                maxHp += i  
            maxHp = floor(base + maxHp * 0.3)
            koefVit = floor(((maxHp*endurance_)/100) - endurance_)
            maxHp = floor(maxHp + koefVit)
        else:
            for i in range(2, level_+1):
                maxHp += i  
            maxHp = floor(base + maxHp * 0.55)
            koefVit = floor(((maxHp*endurance_)/100) - endurance_)
            maxHp = floor(maxHp + koefVit)
    
    if prof_ == 1:
        if level_ <= 70:
            for i in range(2, level_ +1):
                maxHp += i
            maxHp = floor(base + maxHp * 0.7)
            koefVit = floor(((maxHp*endurance_)/100) - endurance_)
            maxHp = floor(maxHp + koefVit)
        else:
            for i in range(2, level_ +1):
                maxHp += i
            maxHp = floor(base + maxHp * 1.1)
            koefVit = floor(((maxHp*endurance_)/100) - endurance_)
            maxHp = floor(maxHp + koefVit)
    
    if prof_ == 2:
        if level_ <= 70:
            for i in range(2, level_ +1):
                maxHp += i
            maxHp = floor(base + maxHp * 0.5)
            koefVit = floor(((maxHp*endurance_)/100) - endurance_)
            maxHp = floor(maxHp + koefVit)
        else:
            for i in range(2, level_ +1):
                maxHp += i
            maxHp = floor(base + maxHp * 0.8)
            koefVit = floor(((maxHp*endurance_)/100) - endurance_)
            maxHp = floor(maxHp + koefVit)
        
    if prof_ == 3:
        maxHp = floor(base + maxHp)
        koefVit = floor((maxHp*endurance_)/100) 
        maxHp = floor(maxHp + koefVit)
  
    health["text"]= f": {maxHp}"
     
def shieldThrow():
    global damageShield    
    intuition_ = int(intuition.get())
    endurance_= int(endurance.get())
    shield_ = int(shield.get())
    
    minDamage = floor(5* (endurance_ *6 +floor(endurance_ * endurance_ /200)*4 + floor(intuition_ /5) + (shield_ * shield_ *3)))

    maxDamage = ceil(6* (endurance_ * 6 + floor(endurance_ * endurance_ / 200)*4 + floor(intuition_ /5) + (shield_ * shield_ *3)))
    
    damageShield["text"]=f"Урон щита: {minDamage} - {maxDamage}"

def calculate():
    global labelAttribute
    global attribute
    level_ = int(level.get())
    attribute = 0
    i=1
    while(i < level_):
        attribute +=  floor(i / 5 + 3)
        i += 1
    attribute += 31
    labelAttribute["text"] = f"Нераспред. атрибуты: {attribute}"
    
def calcStat():
    global restAttribute

    atrStr = 0
    atrDex = 0
    atrInt = 0
    atrEnd = 0
    atrWis = 0
    atrLuck = 0
    
    strength_ = int(strength.get())
    for i in range(1, strength_):
        atrStr +=  (i-1)//10 + 2
    
    dexterity_ = int(dexterity.get())
    for i in range(1, dexterity_):
        atrDex += (i-1)//10 + 2
    
    intuition_ = int(intuition.get())
    for i in range(1, intuition_):
        atrInt += (i-1)//10 + 2
        
    endurance_ = int(endurance.get())
    for i in range(1, endurance_):
        atrEnd += (i-1)//10 + 2

    wisdom_ = int(wisdom.get())
    for i in range(1, wisdom_):
        atrWis += (i-1)//10 + 2

    luck_ = int(luck.get())
    for i in range(1, luck_):
        atrLuck += (i-1)//10 + 2
                                    
    res = attribute - atrStr - atrDex - atrInt - atrEnd - atrWis - atrLuck
    restAttribute["text"] = f"Осталось атрибутов: {res}"
    
def clear_entry():
    level.delete(0, END)
    strength.delete(0, END)
    dexterity.delete(0, END)
    intuition.delete(0, END)
    endurance.delete(0, END)
    wisdom.delete(0, END)
    luck.delete(0, END)
    shield.delete(0, END)
    armor.delete(0, END)
    lightEntry.delete(0, END)
    staffSharpeningEntry.delete(0, END)
    minMagicDamageEntry.delete(0, END)
    maxMagicDamageEntry.delete(0, END)
    attribute = 0
    res = 0
    damage = 0
    maxHp = 0
    level.insert(0,"1")
    strength.insert(0,"1")
    dexterity.insert(0, "1")
    intuition.insert(0, "1")
    endurance.insert(0, "1")
    wisdom.insert(0, "1")
    luck.insert(0, "1")
    shield.insert(0, "0")
    armor.insert(0, "0")
    lightEntry.insert(0, "0")
    staffSharpeningEntry.insert(0, "0")
    minMagicDamageEntry.insert(0, "0")
    maxMagicDamageEntry.insert(0, "0")
      
def exit():
    choise = messagebox.askyesno("Выход", "Вы точно хотите выйти?")
    if choise:
        root.destroy()
      
# Кнопка Рассчитать
startButton=Button(text="Количество атрибутов", font="arial 8", width=16 , background="#59b5f2", bd=5)
startButton["command"] = calculate
startButton.place(x=20, y=175)
#Тень Рассчитать
#root.update()
#shadowstartButton = Label(root, bg="black")
#shadowstartButton.place(x=25, y=175, width = startButton.winfo_width(), height = startButton.winfo_height())
#shadowstartButton.lower(startButton)

# Кнопка Подтвердить
enterButton = Button(text="Распределить хар-ки", font="arial 8", width=16, background="#59b5f2", bd=5)
enterButton["command"] = calcStat
enterButton.place(x=20, y=790)
# Кнопка Новый рассчёт
newCalcButton = Button(text = "Новый рассчёт", font="arial 8", width=16, background="#59b5f2", bd=5)
newCalcButton["command"]= clear_entry
newCalcButton.place(x=550, y=790)
# Броня
armorButton = Button(text="Броня", font="arial 8", width=8, bg="#59b5f2", bd=5)
armorButton["command"]= armor
armorButton.place(x=20, y=1935)
# Бросок щита
shieldThrowButton = Button(text="Бросок щита", font="arial 8", width= 16, background="#59b5f2", bd=5)
shieldThrowButton["command"] = shieldThrow
shieldThrowButton.place(x=20, y=1040)
# maxHP
maxHp = Button(text="Жизнь", font="arial 8",width = 5, background ="#59b5f2", bd=5)
maxHp["command"]= healthMax
maxHp.place(x=550, y=900)
# mana
maxMana = Button(text="Мана", font="arial 8", width = 5, background ="#59b5f2", bd=5)
maxMana["command"] = manaCalc
maxMana.place(x=550, y=1040)
# Уклонение
dodgeButton = Button(text="Уклон/Меткость", font="arial 8", width= 16, bg = "#59b5f2", bd=5)
dodgeButton["command"] = dodge
dodgeButton.place(x=20, y=1150)
# УВС
uvsButton = Button(text="Удар в спину", font="arial 8" , width= 8, bg = "#59b5f2", bd=5)
uvsButton["command"] = uvs
uvsButton.place(x=20, y=1835)
# Благословение оружием
blessingButton = Button(text="Благослов. оружия", font="arial 8", width =13, bg = "#59b5f2", bd=5)
blessingButton["command"] = blessingWeapon
blessingButton.place(x=20, y=1670)
# Исцеление
healingButton = Button(text="Исцеление", font="arial 8", width= 8, bg = "#59b5f2", bd=5)
healingButton["command"] = healing
healingButton.place(x=20, y=1570)
# Сохранить
saveButton = Button(text="Сохранить билд", font="arial 8", width = 14, bg="#59b5f2", bd=5)
saveButton["command"] = saveBuild
saveButton.place(x=580, y=1460)
# Загрузить
downloadButton = Button(text="Загрузить билд", font="arial 8", width=14, bg="#59b5f2", bd=5)
downloadButton["command"] = download
downloadButton.place(x=580, y=1570)
# Логотип
pocketCombats = Label(text="Калькулятор PocketCombats", font="Times 12 bold underline")
pocketCombats.place(x=30, y=0)
# виджет Entry
level=Entry( width=8, justify = CENTER, bd=5)
level.insert(0, "1")
level.place(x=315 , y=100)
# Окно силы
strength=Entry(width=8, justify = CENTER, bd=5)
strength.insert(0,"1")
strength.place(x=315, y=350)
# Окно ловкости
dexterity=Entry(width=8, justify = CENTER,bd=5)
dexterity.insert(0,"1")
dexterity.place(x=315, y=422)
# Окно интуиции
intuition=Entry(width=8, justify = CENTER, bd=5)
intuition.insert(0,"1")
intuition.place(x=315, y=494)
# Окно живучести
endurance=Entry(width=8, justify = CENTER, bd=5)
endurance.insert(0,"1")
endurance.place(x=315, y=565)
# Окно мудрости
wisdom=Entry(width=8, justify = CENTER, bd=5)
wisdom.insert(0,"1")
wisdom.place(x=315, y=637)
# Окно удачи
luck=Entry(width=8, justify = CENTER, bd=5)
luck.insert(0,"1")
luck.place(x=315, y=710)
# Заточка щита
shield = Entry(width = 5, justify= CENTER, bd=5)
shield.insert(0,"0")
shield.place(x=390, y=900)
# Броня
armor = Entry(width = 5, justify = CENTER, bd=5)
armor.insert(0,"0")
armor.place(x=390, y=1950)
# Окно света
lightEntry = Entry(width = 5, justify = CENTER, bd=5)
lightEntry.insert(0,"0")
lightEntry.place(x=390, y=1260)
# Окно заточки посоха
staffSharpeningEntry = Entry(width = 5, justify = CENTER, bd = 5)
staffSharpeningEntry.insert(0,"0")
staffSharpeningEntry.place(x=390, y=1340)
# Минимальный маг урон
minMagicDamageEntry = Entry(width = 5, justify = CENTER, bd = 5)
minMagicDamageEntry.insert(0,"0")
minMagicDamageEntry.place(x=390, y=1420)
# Максимальный маг урон
maxMagicDamageEntry = Entry(width = 5, justify = CENTER, bd = 5)
maxMagicDamageEntry.insert(0,"0")
maxMagicDamageEntry.place(x=390, y=1500)
# *****
today = datetime.date.today().strftime("%d.%m.%y")
dateNow = Label(text=f"{today}", font="times 9 bold")
dateNow.place(x=700,y=95)
clock = Label(font="Times 6 bold")
clock.place(x=715, y=145)
timing()
# web
weblabel = Label(root, text="Наш телеграмм-канал", font="Times 6 bold underline")
weblabel.place(x=600, y=195 )
weblabel.bind("<Button-1>", callback)
# telegramm bot
botlabel = Label(root, text="Телеграмм-бот", font="Times 6 bold underline")
botlabel.place(x=670, y=285)
botlabel.bind("<Button-1>", telegrammbot)
#******
endCode = time.time()
speedCode = (endCode - startCode)
speedCode = format(speedCode, '.5f')
labelTime = Label(text=f"Скорость обработки данных: {speedCode} сек.", font="arial 6 underline")
labelTime.place(x=20, y=2050)
#*******
root.mainloop()