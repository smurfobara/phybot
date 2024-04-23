power = "Сила — это физическая величина, характеризующая действие одного тела на другое. \n Сила - F \n сила\n"
powerUpr = "Силу, возникающую в теле в результате его упругой деформации и стремящуюся вернуть тело в исходное состояние, называют силой упругости. \n Сила упругости - F упр=kx \n k=жёсткость тела \n x=измерение длины \n k можно найти с помощью: k=F упр/x \n сила упругости \n \n"
powerEarth = "Силу, с которой Земля притягивает к себе тело, называют силой тяжести. Притяжение всех тел Вселенной друг к другу называют всемирным тяготением. \n Сила тяжести - F=mg \n m=масса тела \n g=ускорение свободного падения (10 м\с²) \n сила тяжести \n \n"
powerVes = "Вес тела — это сила, с которой тело действует на подвес или опору вследствие притяжения Земле. \n вес тела \n \n"
powerTr = "Сила трения — это сила, возникающая при соприкосновении двух тел и препятствующая их относительному движению. \n сила трения \n \n"
powerRavno = "Силу, которая производит на тело такое же действие, как несколько одновременно действующих на это сил, называют равнодействующей этих сил. \n Равнодействущая сил - R=F₁+F₂ или если \n силы направлены в противоположные сторону R=F₂-F₁ \n равнодействущая сил \n \n"
powerArh = "Выталкивающая сила, действующая на тело, погруженное в жидкость (газ) и равная весу вытесненной телом жидкости (газа) - архимедова сила \n \n FАрх = ρ жидкости * g * Vпогр., где ρ жидкости — плотность жидкости [кг/м3], Vпогр. — объем погруженной части тела [м3], g — ускорение свободного падения [м/с2]"

listPowers = [power, powerUpr, powerEarth, powerVes, powerTr, powerRavno, powerArh]


molekyla = "Мельчайшая частица данного вещества - молекула"
diffuz = "Взаимное проникновение одного вещества между молекулами другого - диффузия"
mehdvizh =  "Изменение положения тела в пространстве относительно других тел с течением времени - механическое движение"
traektory = "Линия, по которой движется тело - траектория"
put = "Длина траектории, по которой движется тело в течении некоторого промежутка времени - путь"
speed = "Величина, равная отношению пути ко времени, за которое этот путь пройден - скорость"
plotnost = "Физическая величина, равная отношению массы тела к его объёму - плотность"
sila = "Мера механического воздействия на тело со стороны других тел - сила"
deformaciya = "Любое изменение формы и размеров тела - деформация"
davleniye = "Физическая величина, равная отношению силы, действующей перпендикулярно некоторой поверхности, к площади этой поверхности - давление"
atmosdavleniye = "Давление атмосферы, действующее на все находящиеся в ней предметы и на земную поверхность, равное модулю силы, действующей в атмосфере, на единицу площади поверхности по нормали к ней - атмосферное давление"
osadka = "Глубина, на которую судно погружается в воду - осадка"
waterline = "Наибольшая допустимая осадка, отмеченная на корпусе судна красной линией"
moshnost = "Физическая величина, численно равная работе, совершенной за единицу времени - мощность \n \n N = A / t, где A — работа, t — время ее совершения"
listOprs = [molekyla, diffuz, mehdvizh, traektory, put, speed, plotnost, sila, deformaciya, davleniye, atmosdavleniye, osadka, waterline, moshnost]
text = "осадка"
listAll = [listPowers, listOprs]

for line in listOprs:
    if "осадка" in line:
        print(line)