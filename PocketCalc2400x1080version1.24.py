from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox
from math import*
import datetime
import calendar
import time
import webbrowser
import random
# ****************************************
startCode = time.time()
# ******
def exit2():
    choise = messagebox.askyesno("", "Вы точно хотите выйти?")
    if choise:
        root.destroy()

def tenba():
    messagebox.showinfo("", "\nОтдельные слова благодарности\nхотел бы выразить игрокам:\n@Smertnay_Tenb и @Астма,\nза предоставленные формулы\nпо игре.")
         
def bot():
    messagebox.showinfo("", "\nПо вопросам телеграмм-бота\nписать @PocketYa")
        
def firmado():
    messagebox.showinfo("", "\nВы можете найти\nменя в телеграмме\n@Firmado")

def version():
    messagebox.showinfo("", "\nВерсия 1.24\nот 04.12.2022")

def nuance():
    messagebox.showinfo("", """Нюансы работы калькулятора:\n◦Если вы свернули калькуля-\nтор, а потом возобновили работу,\nто для активации клавиатуры\nнеобходимо один раз нажать на\nкнопку ◀ на клавиатуре\nтелефона.\n◦Погрешность при вычислении\n Исцеления.\n◦Погрешность при вычислении\nмагического урона.""")
        
def instruction():
    messagebox.showinfo("", """‌◦Внимание!!! Для рассчёта \nатрибутов все поля характерис-\nтик должны быть заполнены.\nЕсли нет необходимости рассчи-\nтывать характеристику, ставим\nпросто единицу.\n◦Для "Броска щитом"\nзаполняем интуицию, живучесть\nи уровень заточки щита, если \nщит без заточки, ставим ноль.\n◦Для "Исцеления" заполняем\nуровень, интуицию, мудрость,\nурон от Света, заточку посоха,\nмин. и макс. магический урон,\nи выбираем необходимый нам\nпосох.\n◦Для рассчёта жизни и маны\nзаполняем уровень, живучесть и \nмудрость.\n◦Для рассчёта уворота и мет-\nкости заполняем уровень,\nловкость,интуицию и удачу.""")
# ****************************************
root=Tk()
back = "#59b5f2" # <--- Цвет кнопок
#********
mainmenu = Menu(root, font="Times 8 bold", activebackground= back)
root.config(menu = mainmenu)
#*****
instructionmenu = Menu(mainmenu, activebackground= back)
instructionmenu.add_separator()
instructionmenu.add_command(label="Как заполнять поля?",font="Times 8 bold", command = instruction)
instructionmenu.add_separator()
instructionmenu.add_command(label="Нюанс работы калькулятора", font="Times 8 bold", command = nuance)
#*****
infomenu = Menu(mainmenu, activebackground= back)
infomenu.add_separator()
infomenu.add_command(label="Версия программы", font="Times 8 bold", command = version)
infomenu.add_separator()
infomenu.add_command(label="Об авторе", font="Times 8 bold", command = firmado)
infomenu.add_separator()
infomenu.add_command(label="Телеграмм-бот", font="Times 8 bold", command = bot)
infomenu.add_separator()
infomenu.add_command(label="Благодарность", font="Times 8 bold", command = tenba)
#*****
exitmenu = Menu(mainmenu, activebackground= back)
exitmenu.add_separator()
exitmenu.add_command(label="Выход", font="Times 8 bold", command = exit2)
#*****
mainmenu.add_cascade(label="   Инструкция", menu = instructionmenu)
mainmenu.add_cascade(label="     О программе", menu = infomenu)
mainmenu.add_cascade(label="        Выход", menu = exitmenu)
#*****************************************
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
mage.place(x=600, y=430)

warrior = Radiobutton(text="Воин", variable = prof, value = 1)
warrior.place(x=600, y=500)

hunter = Radiobutton(text="Охотник", variable = prof, value = 2)
hunter.place(x=600, y=570)

newbie = Radiobutton(text="Новичок", variable = prof, value = 3)
newbie.place(x=600, y=640)

stakanov = Radiobutton(text="Стаканов", variable = prof, value = 4, command = exit)
stakanov.place(x=600, y=710)
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
# Жуткий посох
staffCreepy = IntVar()
staffCreepy.set(0)

staffCreepy_checkbutton = Checkbutton(text="Жуткий посох", font="arial 8", variable = staffCreepy, bd = 5)
staffCreepy_checkbutton.place(x=550, y=1450)
# Скорость ветра
windSpeed = IntVar()
windSpeed.set(0)

windSpeed_checkbutton = Checkbutton(text="Скорость ветра", font="arial 8", variable = windSpeed, bd = 5)
windSpeed_checkbutton.place(x=530, y=1140)
# Капюшон злых намерений
evilHood = IntVar()
evilHood.set(0)

evilHood_checkbutton = Checkbutton(text="Капюшон злых нам.", font="arial 8", variable = evilHood, bd=5)
evilHood_checkbutton.place(x=550, y=1515)
# Бросок щита
shieldSharp = Label (text="Заточка щита:")
shieldSharp.place(x=20, y=900)
# Урон броска щита
damageShield = Label (text="Урон щита: ", font="arial 7")
damageShield.place(x=20, y=970)
# maxHP
health = Label (text=": ")
health.place(x=785, y=915)
# maxMana
urMana = Label(text=": ")
urMana.place(x=785, y=1055)
# Уклонение
dodgeLabel = Label(text="Уклон/Меткость:", font = "arial 7" )
dodgeLabel.place(x=550, y=1200)
# Броня
armorLabel = Label(text="Физический урон\nуменьшен на, % :__", font="arial 7")
armorLabel.place(x=550, y=1935)
# Магический урон вещей
equipmentMagicDamage = Label(text="Маг.урон с предметов экипировки: ", font="arial 8")
equipmentMagicDamage.place(x=20, y=1590)
# Усиление магии от рун и вещей
amplifyMagic = Label(text="Усиление магии от рун и вещей: ", font="arial 8")
amplifyMagic.place(x=20, y=1665)
# Урон от света
lightLabel = Label(text="Урон от Света: ", font="arial 8")
lightLabel.place(x=20, y=1265)
# Исцеление
healingLabel = Label(text=": ")
healingLabel.place(x=330, y=1855)
# Маг урон
magicDamageLabel= Label(text=": ")
magicDamageLabel.place(x=330, y=1760)
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
    char = [level, strength, dexterity, intuition, endurance, wisdom, luck, shield, armor, lightEntry, staffSharpeningEntry, minMagicDamageEntry, maxMagicDamageEntry, equipmentMagicDamageEntry, amplifyMagicEntry]
    try:
        charList = open("charList.dat", "r", encoding="utf-8")
        for i, line in enumerate(charList):
            char[i].delete(0, "end")
            char[i].insert(0, line[:-1])
        charList.close()                       
    except:
        messagebox.showwarning("", "\nЧто-то пошло не так!")
#*****************************************
def saveBuild():
    char = [level.get(), strength.get(), dexterity.get(), intuition.get(), endurance.get(), wisdom.get(), luck.get(), shield.get(), armor.get(), lightEntry.get(), staffSharpeningEntry.get(), minMagicDamageEntry.get(), maxMagicDamageEntry.get(), equipmentMagicDamageEntry.get(), amplifyMagicEntry.get()]
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
def dodge():
    global dodgeLabel
    level_ = int(level.get())
    dexterity_ = int(dexterity.get())
    intuition_ = int(intuition.get())
    luck_ = int(luck.get())
    windSpeed_ = int(windSpeed.get())
    
    dodge = 100 + level_ + dexterity_ + floor(luck_ *0.2)
    if ( windSpeed.get() == 1):
        dodge = (100 + level_ + dexterity_ + floor(luck_ * 0.2)) +30
    accuracy = 175 + level_ + intuition_ + floor(luck_ /3)
    dodgeLabel["text"] = f"Уклон/Меткость: {dodge}/{accuracy}"
    
def armor():
    global armorLabel
    armor_ = int(armor.get())
    armor2 = round(100 *(1-((4000+armor_)/((4000+armor_ * 10)))))
    
    armorLabel["text"] = f"Физический урон\nуменьшен на, % :{armor2}"
    
def wizardDamage():
    global magicDamageLabel
    level_ = int(level.get())
    wisdom_ = int(wisdom.get())
    intuition_ = int(intuition.get())
    luck_ = int(luck.get())
    equipmentMagicDamageEntry_ = int(equipmentMagicDamageEntry.get())
    amplifyMagicEntry_ = int(amplifyMagicEntry.get())
    staffSharpeningEntry_ = int(staffSharpeningEntry.get())
    evilHood_ = int(evilHood.get())
    staffCreepy_ = int(staffCreepy.get())
    
    koefWizardDamage = round((600+ intuition_ * 10)/(600 + intuition_), 1)
    
    minBWD = ceil(level_ /6 + wisdom_ *1.2 + intuition_ /5 + luck_ /3)
    minEquipment = ceil(equipmentMagicDamageEntry_ * 0.9)
    amplify = amplifyMagicEntry_ /100 +1
    
    minWizardDamage = trunc(((minBWD + minEquipment) * amplify) * koefWizardDamage)
    if(evilHood.get() ==1 and staffCreepy.get()==1):
        minWizardDamage = trunc(((minBWD +(staffSharpeningEntry_ *10) + minEquipment) * amplify) * koefWizardDamage)
    if(evilHood.get() == 1 and staffCreepy.get() == 1 and staffSharpeningEntry.get() =="10"):
        minWizardDamage = trunc(((minBWD + (staffSharpeningEntry_ *10 +50) + minEquipment) * amplify) * koefWizardDamage)
    minMagicDamageEntry.delete(0, END)
    minMagicDamageEntry.insert(0,  minWizardDamage)
    
    maxBWD = ceil((level_ / 4 + wisdom_ *4/3 + intuition_ /5 + luck_ *2/3 ))
    maxEquipment = equipmentMagicDamageEntry_
    
    maxWizardDamage = trunc(((maxBWD + maxEquipment) * amplify) * koefWizardDamage)
    if(evilHood.get()==1 and staffCreepy.get()==1):
        maxWizardDamage = trunc(((maxBWD + (staffSharpeningEntry_ * 10) + maxEquipment) * amplify) * koefWizardDamage)
    if(evilHood.get() == 1 and staffCreepy.get() == 1 and staffSharpeningEntry.get() =="10"):
        maxWizardDamage = trunc(((maxBWD + (staffSharpeningEntry_ *10 +50) + maxEquipment) * amplify) * koefWizardDamage)
    maxMagicDamageEntry.delete(0, END)
    maxMagicDamageEntry.insert(0, maxWizardDamage)
              
    magicDamageLabel["text"] = f":{minWizardDamage}-{maxWizardDamage}"
       
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
   elif(staffHealers.get() != 1 and staffBlessing.get() != 1 and runeLifecurrent.get()==1):
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
   elif(staffHealers.get() != 1 and staffBlessing.get() != 1 and runeLifecurrent.get()==1):
       maxheal = round(maxheal + (maxheal * 30)/100)
       
   if staffBlessing.get() == 1:
        maxheal = round(maxheal + (maxheal * (staffSharpeningEntry_ * 0.05) + maxMagicDamageEntry_))
        if runeLifecurrent.get()==1:
                 maxheal = round(maxheal + (maxheal*30)/100)
                 
   healingLabel["text"] = f":{minheal}-{maxheal}"
      
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

    maxHp = 0
    if prof_ == 0:
        if level_ <= 70:
            for i in range(2, level_ +1):
                maxHp += floor(i * 0.3)   
            maxHp = floor(base + maxHp)
            koefVit = floor((maxHp*endurance_)/100)
            maxHp = floor(maxHp + koefVit)
        else:
            for i in range(2, level_+1):
                maxHp += floor(i * 0.55)  
            maxHp = floor(base + maxHp)
            koefVit = floor((maxHp*endurance_)/100)
            maxHp = floor(maxHp + koefVit)
    
    if prof_ == 1:
        if level_ <= 70:
            for i in range(2, level_ +1):
                maxHp += floor(i * 0.7)
            maxHp = floor(base + maxHp)
            koefVit = floor((maxHp*endurance_)/100)
            maxHp = floor(maxHp + koefVit)
        else:
            for i in range(2, level_ +1):
                maxHp += floor(i * 1.1)
            maxHp = floor(base + maxHp)
            koefVit = floor((maxHp*endurance_)/100)
            maxHp = floor(maxHp + koefVit)
    
    if prof_ == 2:
        if level_ <= 70:
            for i in range(2, level_ +1):
                maxHp += floor(i * 0.5)
            maxHp = floor(base + maxHp)
            koefVit = floor((maxHp*endurance_)/100)
            maxHp = floor(maxHp + koefVit)
        else:
            for i in range(2, level_ +1):
                maxHp += floor(i * 0.8)
            maxHp = floor(base + maxHp)
            koefVit = floor((maxHp*endurance_)/100)
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
    
    minDamage = floor(5* (endurance_ *6 +floor(endurance_ * endurance_ /200)*4 + floor(intuition_ /5) + (pow(shield_, 2)*3)))

    maxDamage = ceil(6* (endurance_ * 6 + floor(endurance_ * endurance_ / 200)*4 + floor(intuition_ /5) + (pow(shield_, 2)*3)))
    
    damageShield["text"]=f"Урон щита: {minDamage} - {maxDamage}"

def protection():
    global stunLabel
    global blindnessLabel
    global poisoningLabel
    global glaciationLabel
    global petrificationLabel
    global burnLabel
    global bleedingLabel
    global dumbnessLabel
    global curseLabel
    endurance_ = int(endurance.get())
    wisdom_ = int(wisdom.get())
    luck_ = int(luck.get())
        
    stun = endurance_
    if(stun >= 75):
        stun = 75
    stun2 = ceil(luck_ * 0.4)
    
    blindness = int((wisdom_ + endurance_ )/2)
    if(blindness >= 75):
        blindness = 75
    blindness2 = ceil(luck_ * 0.4)
    
    poisoning = endurance_
    if(poisoning >= 75):
        poisoning = 75  
    poisoning2 = ceil(luck_ * 0.4)
    
    glaciation = int(wisdom_ /2)
    if(glaciation >= 75):
        glaciation = 75
    glaciation2 = ceil(luck_ * 0.4)
    
    petrification = int(wisdom_ /2)
    if(petrification >= 75):
        petrification = 75
        
    burn = round(wisdom_ /3)
    if(burn >= 70):
        burn = 70
        
    bleeding = endurance_
    if(bleeding >= 75):
        bleeding = 75
        
    dumbness = floor(floor(wisdom_ /2) + floor(endurance_ /4) + floor(luck_ /8))
    if(dumbness >= 75):
        dumbness = 75
        
    curse = luck_
    
    stunLabel["text"] = f"Защита от оглушения:       {stun}%+{stun2}"
    blindnessLabel["text"] = f"Защита от ослепления:      {blindness}%+{blindness2}"
    poisoningLabel["text"] = f"Защита от отравления:      {poisoning}%+{poisoning2}"
    glaciationLabel["text"] = f"Защита от оледенения:      {glaciation}%+{glaciation2}"
    petrificationLabel["text"] = f"Защита от окаменения:     {petrification}%"
    burnLabel["text"] = f"Защита от ожога:                  {burn}%"
    bleedingLabel["text"] = f"Защита от кровотечения: {bleeding}%"
    dumbnessLabel["text"] = f"Защита от немоты:              {dumbness}%"
    curseLabel["text"] = f"Защита от проклятия:        {curse}%"
    
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
    equipmentMagicDamageEntry.delete(0, END)
    amplifyMagicEntry.delete(0, END)
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
    equipmentMagicDamageEntry.insert(0, "0")
    amplifyMagicEntry.insert(0, "0")
      
def exit():
    choise = messagebox.askyesno("Выход", "Вы точно хотите выйти?")
    if choise:
        root.destroy()
      
# Кнопка Рассчитать
startButton=Button(text="Количество атрибутов", font="arial 8", width=16 , background= back, bd=5)
startButton["command"] = calculate
startButton.place(x=20, y=175)
# Кнопка Подтвердить
enterButton = Button(text="Распределить хар-ки", font="arial 8", width=16, background= back, bd=5)
enterButton["command"] = lambda: (calcStat(), protection())
enterButton.place(x=20, y=790)
# Кнопка Новый рассчёт
newCalcButton = Button(text = "Новый рассчёт", font="arial 8", width=16, background= back, bd=5)
newCalcButton["command"]= clear_entry
newCalcButton.place(x=550, y=790)
# Броня
armorButton = Button(text="Броня", font="arial 8", width=8, bg= back, bd=5)
armorButton["command"]= armor
armorButton.place(x=20, y=1935)
# Бросок щита
shieldThrowButton = Button(text="Бросок щита", font="arial 8", width= 16, background= back, bd=5)
shieldThrowButton["command"] = shieldThrow
shieldThrowButton.place(x=20, y=1040)
# maxHP
maxHp = Button(text="Жизнь", font="arial 8",width = 5, background = back, bd=5)
maxHp["command"]= healthMax
maxHp.place(x=550, y=900)
# mana
maxMana = Button(text="Мана", font="arial 8", width = 5, background = back, bd=5)
maxMana["command"] = manaCalc
maxMana.place(x=550, y=1040)
# Уклонение
dodgeButton = Button(text="Уклон/Меткость", font="arial 8", width= 16, bg = back, bd=5)
dodgeButton["command"] = dodge
dodgeButton.place(x=20, y=1150)
# Исцеление
healingButton = Button(text="Исцеление", font="arial 8", width= 8, bg = back, bd=5)
healingButton["command"] = healing
healingButton.place(x=20, y=1835)
# Маг урон
magicDamageButton = Button(text="Маг.урон", font="arial 8", width=8, bg= back, bd=5)
magicDamageButton["command"] = wizardDamage
magicDamageButton.place(x=20, y=1735 )
# Сохранить
saveButton = Button(text="Сохранить билд", font="arial 8", width = 14, bg= back, bd=5)
saveButton["command"] = saveBuild
saveButton.place(x=580, y=1735)
# Загрузить
downloadButton = Button(text="Загрузить билд", font="arial 8", width=14, bg= back, bd=5)
downloadButton["command"] = download
downloadButton.place(x=580, y=1835)
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
# Маг урон от вещей
equipmentMagicDamageEntry = Entry(width = 5, justify = CENTER, bd =5)
equipmentMagicDamageEntry.insert(0, "0")
equipmentMagicDamageEntry.place(x=800, y=1585)
# Усиление магии от рун и вещей
amplifyMagicEntry= Entry(width=5, justify = CENTER, bd = 5)
amplifyMagicEntry.insert(0,"0")
amplifyMagicEntry.place(x=800, y=1660)
# Кнопки Защиты
saveFont = "Times 5"
# Защита от оглушения
stunLabel = Label(text="Защита от оглушения:", font= saveFont)
stunLabel.place(x=550, y=100)
# Защита от ослепления
blindnessLabel = Label(text="Защита от ослепления:", font= saveFont)
blindnessLabel.place(x=550, y=135)
# Защита от отравления
poisoningLabel = Label(text="Защита от отравления:", font= saveFont)
poisoningLabel.place(x=550, y= 170)
# Защита от оледенения
glaciationLabel = Label(text="Защита от оледенения:", font= saveFont)
glaciationLabel.place(x=550, y=205)
# Защита от окаменения
petrificationLabel = Label(text="Защита от окаменения:", font= saveFont)
petrificationLabel.place(x=550, y=240)
# Защита от ожога
burnLabel = Label(text="Защита от ожога:", font = saveFont)
burnLabel.place(x=550, y=275)
# Защита от кровотечения
bleedingLabel = Label(text="Защита от кровотечения:", font= saveFont)
bleedingLabel.place(x=550, y= 310)
# Защита от немоты
dumbnessLabel = Label(text="Защита от немоты:", font= saveFont)
dumbnessLabel.place(x=550, y=345)
# Защита от проклятия
curseLabel = Label(text="Защита от проклятия:", font= saveFont)
curseLabel.place(x=550, y=380)
#******
endCode = time.time()
speedCode = (endCode - startCode)
speedCode = format(speedCode, '.5f')
labelTime = Label(text=f"Скорость обработки данных: {speedCode} сек.", font="arial 6 underline")
labelTime.place(x=20, y=2050)
#*******
root.mainloop()
