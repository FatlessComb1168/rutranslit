import colorama;
from colorama import Fore, Style;
import datetime;
from datetime import datetime;
import os;
import sys;
import pyperclip;
import ctypes;
colorama.init();
ctypes.windll.kernel32.SetConsoleTitleW('Rutranslit');

check_1 = ['Э', 'Ж', 'Ё', 'ТСЯ', 'Щ', 'Ч', 'Ш', 'Ю', 'Я', 'Ц', 'Ь', 'Ъ'];
check_2 = ['EH', 'ZH', 'YO', 'TSYA', 'SHCH', 'CH', 'SH', 'YU', 'YA', 'TS', "'", '"'];

ru = ['Ё', 'Ж', 'Щ', 'Ч', 'Ш', 'Ю', 'Я', 'Ц', 'Э', 'э', 'тся', 'я', 'ый', 'щ', 'ч', 'ц', 'ш', 'ю', 'ё', 'ж', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н','О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ы', 'а', 'б', 'в', 'г', 'д', 'е', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ъ', 'ы', 'ь']
lat = ['Yo', 'Zh', 'Shch', 'Ch', 'Sh', 'Yu', 'Ya', 'Ts', 'Eh', 'eh', 'tsya', 'ya', 'yj', 'shch', 'ch', 'ts', 'sh', 'yu', 'yo', 'zh', 'A', 'B', 'V', 'G', 'D', 'E', 'Z', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'F', 'H', 'Y','a', 'b', 'v', 'g', 'd', 'e', 'z', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'h', '"', 'y', "'"];

history = '';

def dt():
    global td, d, m, y, h, mi, s, date;
    td = datetime.today();

    d = td.day;
    if d < 10: d = '0' + str(d);
    d = str(d);

    m = td.month;
    if m < 10: m = '0' + str(m);
    m = str(m);

    y = str(td.year);

    h = td.hour;
    if h < 10: h = '0' + str(h);
    h = str(h);

    mi = td.minute;
    if mi < 10: mi = '0' + str(mi);
    mi = str(mi);

    s = td.second;
    if s < 10: s = '0' + str(s);
    s = str(s);

    date = d + '.' + m + '.' + y + ', ' + h + ':' + mi + ':' + s + ":\n";

def tol():
    global t;
    print(Fore.YELLOW + 'Введите текст на русском:' + Style.RESET_ALL);
    t = input();
    
    check = t.upper();
    if t == check:
        for i in range(len(check_1)):
            if check_1[i] in t:
                t = t.replace(check_1[i],check_2[i]);

    for i in range(len(ru)):
        if ru[i] in t:
            t = t.replace(ru[i],lat[i]);

def frl():
    global t;
    print(Fore.YELLOW + 'Введите переведённый текст:' + Style.RESET_ALL);
    t = input();

    check = t.upper();
    if t == check:
        for i in range(len(check_1)):
            if check_2[i] in t:
                t = t.replace(check_2[i],check_1[i]);

    for i in range(len(ru)):
        if lat[i] in t:
            t = t.replace(lat[i],ru[i]);

def ot1():
    global t;
    pyperclip.copy(t);
    print(Fore.YELLOW + '\nВерсия на латинице:\n' + Style.RESET_ALL + t);
    print(Fore.YELLOW)
    print('\nТекст скопирован. Нажмите Enter, чтобы продолжить.');
    print(Style.RESET_ALL);

def ot2():
    global t;
    pyperclip.copy(t);
    print(Fore.YELLOW + '\nОригинал:\n' + Style.RESET_ALL + t);
    print(Fore.YELLOW)
    print('\nТекст скопирован. Нажмите Enter, чтобы продолжить.');
    print(Style.RESET_ALL);

def launch():
    print(Fore.YELLOW + 'Добро пожаловать в Rutranslit!');
    print('Напишите любой текст на русском языке');
    print('и получите его версию на латинском алфавите.\n');
    print('0 - Перевод на латиницу\n1 - Перевод на русский алфавит');
    print('2 - История выводов\n3 - Выход с сохранением истории выводов.')
    print(Style.RESET_ALL);

while True:
    launch();
    a = input();
    os.system('cls');
    if a == '0':
        tol();
        dt();
        history = history + date + t + '\n\n';
        ot1();
    if a == '1':
        frl();
        dt();
        history = history + date + t + '\n\n';
        ot2();
    if a == '2':
        print(history);
        print(Fore.YELLOW + 'Нажмите Enter, чтобы продолжить.');
    if a == '3':
        os.system('cls');
        print(Fore.YELLOW + 'Выход...' + Style.RESET_ALL);
        f = open('rutranslit_history.txt', 'a+');
        f.write(history);
        f.close();
        sys.close();
    input();
    os.system('cls');