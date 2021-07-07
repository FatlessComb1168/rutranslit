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

    check = t.lower();
    check = t.upper();
    if t == check:
        t = t.replace('Э', 'EH');
        t = t.replace('Ж', 'ZH');
        t = t.replace('Ё', 'YO');
        t = t.replace('Ш', 'SH');
        t = t.replace('Щ', 'SHCH');
        t = t.replace('Ю', 'YU');
        t = t.replace('Я', 'YA');
        t = t.replace('Ц', 'TS');
        t = t.replace('Ч', 'CH');
        t = t.replace('Ь', "'");
        t = t.replace('Ъ', '"');

    t = t.replace('А', 'A');
    t = t.replace('Б', 'B');
    t = t.replace('В', 'V');
    t = t.replace('Г', 'G');
    t = t.replace('Д', 'D');
    t = t.replace('Е', 'Е');
    t = t.replace('Ё', 'Yo');
    t = t.replace('Ж', 'Zh');
    t = t.replace('З', 'Z');
    t = t.replace('И', 'I');
    t = t.replace('Й', 'J');
    t = t.replace('К', 'K');
    t = t.replace('Л', 'L');
    t = t.replace('М', 'M');
    t = t.replace('Н', 'N');
    t = t.replace('О', 'O');
    t = t.replace('П', 'P');
    t = t.replace('Р', 'R');
    t = t.replace('С', 'S');
    t = t.replace('Т', 'T');
    t = t.replace('У', 'U');
    t = t.replace('Ф', 'F');
    t = t.replace('Х', 'H');
    t = t.replace('Ц', 'Ts');
    t = t.replace('Ч', 'Ch');
    t = t.replace('Ш', 'Sh');
    t = t.replace('Щ', 'Shch');
    t = t.replace('Ы', 'Y');
    t = t.replace('Э', 'Eh');
    t = t.replace('Ю', 'Yu');
    t = t.replace('Я', 'Ya');

    t = t.replace('а', 'a');
    t = t.replace('б', 'b');
    t = t.replace('в', 'v');
    t = t.replace('г', 'g');
    t = t.replace('д', 'd');
    t = t.replace('е', 'e');
    t = t.replace('ё', 'yo');
    t = t.replace('ж', 'zh');
    t = t.replace('з', 'z');
    t = t.replace('и', 'i');
    t = t.replace('й', 'j');
    t = t.replace('к', 'k');
    t = t.replace('л', 'l');
    t = t.replace('м', 'm');
    t = t.replace('н', 'n');
    t = t.replace('о', 'o');
    t = t.replace('п', 'p');
    t = t.replace('р', 'r');
    t = t.replace('с', 's');
    t = t.replace('т', 't');
    t = t.replace('у', 'u');
    t = t.replace('ф', 'f');
    t = t.replace('х', 'h');
    t = t.replace('ц', 'ts');
    t = t.replace('ч', 'ch');
    t = t.replace('ш', 'sh');
    t = t.replace('щ', 'shch');
    t = t.replace('ъ', '"');
    t = t.replace('ы', 'y');
    t = t.replace('ь', "'");
    t = t.replace('э', 'eh');
    t = t.replace('ю', 'yu');
    t = t.replace('я', 'ya');

def frl():
    global t;
    print(Fore.YELLOW + 'Введите переведённый текст:' + Style.RESET_ALL);
    t = input();

    check = t.lower();
    check = t.upper();
    if t == check:
        t = t.replace('EH', 'Э');
        t = t.replace('ZH', 'Ж');
        t = t.replace('YO', 'Ё');
        t = t.replace('TSYA', 'ТСЯ');
        t = t.replace('SHCH', 'Щ');
        t = t.replace('CH', 'Ч');
        t = t.replace('SH', 'Ш');
        t = t.replace('YU', 'Ю');
        t = t.replace('YA', 'Я');
        t = t.replace('TS', 'Ц');
        t = t.replace("'", "Ь");
        t = t.replace('"', 'Ъ');

    t = t.replace('Eh', 'Э');
    t = t.replace('A', 'А');
    t = t.replace('B', 'Б');
    t = t.replace('V', 'В');
    t = t.replace('G', 'Г');
    t = t.replace('D', 'Д');
    t = t.replace('E', 'Е');
    t = t.replace('Yo', 'Ё');
    t = t.replace('Zh', 'Ж');
    t = t.replace('Z', 'З');
    t = t.replace('I', 'И');
    t = t.replace('J', 'Й');
    t = t.replace('K', 'К');
    t = t.replace('L', 'Л');
    t = t.replace('M', 'М');
    t = t.replace('N', 'Н');
    t = t.replace('O', 'О');
    t = t.replace('P', 'П');
    t = t.replace('R', 'Р');
    t = t.replace('S', 'С');
    t = t.replace('T', 'Т');
    t = t.replace('U', 'У');
    t = t.replace('F', 'Ф');
    t = t.replace('H', 'Х');
    t = t.replace('Ts', 'Ц');
    t = t.replace('Ch', 'Ч');
    t = t.replace('Sh', 'Ш');
    t = t.replace('Shch', 'Щ');
    t = t.replace('Y', 'Ы');
    t = t.replace('Yu', 'Ю');
    t = t.replace('Ya', 'Я');

    t = t.replace('eh', 'э');
    t = t.replace('tsya', 'тся');
    t = t.replace('ya','я');
    t = t.replace('yj','ый');
    t = t.replace('shch', 'щ');
    t = t.replace('ch', 'ч');
    t = t.replace('ts', 'ц');
    t = t.replace('sh', 'ш');
    t = t.replace('yu', 'ю');

    t = t.replace('a', 'а');
    t = t.replace('b', 'б');
    t = t.replace('v', 'в');
    t = t.replace('g', 'г');
    t = t.replace('d', 'д');
    t = t.replace('e', 'е');
    t = t.replace('yo', 'ё');
    t = t.replace('zh', 'ж');
    t = t.replace('z', 'з');
    t = t.replace('i', 'и');
    t = t.replace('j', 'й');
    t = t.replace('k', 'к');
    t = t.replace('l', 'л');
    t = t.replace('m', 'м');
    t = t.replace('n', 'н');
    t = t.replace('o', 'о');
    t = t.replace('p', 'п');
    t = t.replace('r', 'р');
    t = t.replace('s', 'с');
    t = t.replace('t', 'т');
    t = t.replace('u', 'у');
    t = t.replace('f', 'ф');
    t = t.replace('h', 'х');
    t = t.replace('"', 'ъ');
    t = t.replace('y', 'ы');
    t = t.replace("'", "ь");

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
        print('Нажмите Enter, чтобы продолжить.');
    if a == '3':
        os.system('cls');
        print(Fore.YELLOW + 'Выход...' + Style.RESET_ALL);
        f = open('rutranslit_history.txt', 'a+');
        f.write(history);
        f.close();
        sys.close();
    input();
    os.system('cls');