'''
Rutranslit.
Copyright (C) 2021 Fedor Egorov <fedoregorov1@yandex.ru>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
from colorama import Fore, Style, init;
from datetime import datetime;
from os import system;
from re import split;
from pyperclip import copy;
import ctypes;

init();
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
    t1 = input();
    t1 = split(r'( .)',t1);


    for i in t1:
        i2 = i;
        check = i.upper();
        if i == check:
            for i1 in range(len(check_1)):
                i2 = i2.replace(check_1[i1],check_2[i1]);

        for i1 in range(len(ru)):
            i2 = i2.replace(ru[i1],lat[i1]);
        t1[t1.index(i)] = i2;

    t = '';
    for i in t1:
        t += i;

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
    copy(t);
    print(Fore.YELLOW + '\nВерсия на латинице:\n' + Style.RESET_ALL + t);
    print(Fore.YELLOW)
    print('\nТекст скопирован. Нажмите Enter, чтобы продолжить.');
    print(Style.RESET_ALL);

def ot2():
    global t;
    copy(t);
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
    system('cls');

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
        system('cls');
        print(Fore.YELLOW + 'Выход...' + Style.RESET_ALL);
        f = open('rutranslit_history.txt', 'a+');
        f.write(history);
        f.close();
        break;

    input();
    system('cls');