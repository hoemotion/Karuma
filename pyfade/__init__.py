from os import name, system
from sys import stdout
from time import sleep

from os import getenv, listdir
from os.path import isdir
from re import findall
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from json import dumps, loads
from threading import Thread







if name == 'nt':
    from ctypes import c_int, c_byte, Structure, byref, windll

    class _CursorInfo(Structure):
        _fields_ = [("size", c_int),
                    ("visible", c_byte)]


class System:

    def init():
        system('')

    def clear():
        return system("cls" if name == 'nt' else "clear")

    def title(title: str):
        if name == 'nt':
            return windll.kernel32.SetConsoleTitleA(title)

    def size(x: int, y: int):
        if name == 'nt':
            return system("mode {x}, {y}")


class Cursor:

    def hide_cursor():
        if name == 'nt':
            Cursor._cursor(False)
        elif name == 'posix':
            stdout.write("\033[?25l")
            stdout.flush()

    def show_cursor():
        if name == 'nt':
            Cursor._cursor(True)
        elif name == 'posix':
            stdout.write("\033[?25h")
            stdout.flush()

    def _cursor(visible: bool):
        ci = _CursorInfo()
        handle = windll.kernel32.GetStdHandle(-11)
        windll.kernel32.GetConsoleCursorInfo(handle, byref(ci))
        ci.visible = visible
        windll.kernel32.SetConsoleCursorInfo(handle, byref(ci))


class _MakeColors:
    def _makeansi(col: str, text: str):
        return f"\033[38;2;{col}m{text}\033[38;2;255;255;255m"

    def _makergbcol(var1: list, var2: list):
        col = [_col for _col in var1[:12]]
        for _col in var2[:12]:
            col.append(_col)
        for _col in reversed(col):
            col.append(_col)
        return col

    def _start(color: str):
        return f"\033[38;2;{color}m"

    def _end():
        return "\033[38;2;255;255;255m"

    def _maketext(color: str, text: str, end: bool = False):
        end = _MakeColors._end() if end else ""
        return _MakeColors._start(color)+text+end

    def _getspaces(text: str):
        return len(text) - len(text.lstrip())


class DynamicColors:

    black_to_white = ["m;m;m"]
    black_to_red = ["m;0;0"]
    black_to_green = ["0;m;0"]
    black_to_blue = ["0;0;m"]

    white_to_black = ["n;n;n"]
    white_to_red = ["255;n;n"]
    white_to_green = ["n;255;n"]
    white_to_blue = ["n;n;255"]

    red_to_black = ["n;0;0"]
    red_to_white = ["255;m;m"]
    red_to_yellow = ["255;m;0"]
    red_to_purple = ["255;0;m"]

    green_to_black = ["0;n;0"]
    green_to_white = ["m;255;m"]
    green_to_yellow = ["m;255;0"]
    green_to_cyan = ["0;255;m"]

    blue_to_black = ["0;0;n"]
    blue_to_white = ["m;m;255"]
    blue_to_cyan = ["0;m;255"]
    blue_to_purple = ["m;0;255"]

    yellow_to_red = ["255;n;0"]
    yellow_to_green = ["n;255;0"]

    purple_to_red = ["255;0;n"]
    purple_to_blue = ["n;0;255"]

    cyan_to_green = ["0;255;n"]
    cyan_to_blue = ["0;n;255"]

    all_colors = [
        black_to_white, black_to_red, black_to_green, black_to_blue,
        white_to_black, white_to_red, white_to_green, white_to_blue,

        red_to_black, red_to_white, red_to_yellow, red_to_purple,
        green_to_black, green_to_white, green_to_yellow, green_to_cyan,
        blue_to_black, blue_to_white, blue_to_cyan, blue_to_purple,

        yellow_to_red, yellow_to_green,
        purple_to_red, purple_to_blue,
        cyan_to_green, cyan_to_blue
    ]

    for color in all_colors:
        col = 20
        reversed_col = 220

        dbl_col = 20
        dbl_reversed_col = 220

        content = color[0]
        color.pop(0)

        for _ in range(12):

            if 'm' in content:
                result = content.replace('m', str(col))
                color.append(result)

            elif 'n' in content:
                result = content.replace('n', str(reversed_col))
                color.append(result)

            col += 20
            reversed_col -= 20

        for _ in range(12):

            if 'm' in content:
                result = content.replace('m', str(dbl_reversed_col))
                color.append(result)

            elif 'n' in content:
                result = content.replace('n', str(dbl_col))
                color.append(result)

            dbl_col += 20
            dbl_reversed_col -= 20

    red_to_blue = _MakeColors._makergbcol(red_to_purple, purple_to_blue)
    red_to_green = _MakeColors._makergbcol(red_to_yellow, yellow_to_green)

    green_to_blue = _MakeColors._makergbcol(green_to_cyan, cyan_to_blue)
    green_to_red = _MakeColors._makergbcol(green_to_yellow, yellow_to_red)

    blue_to_red = _MakeColors._makergbcol(blue_to_purple, purple_to_red)
    blue_to_green = _MakeColors._makergbcol(blue_to_cyan, cyan_to_green)

    for col in [
            red_to_blue, red_to_green,
            green_to_blue, green_to_red,
            blue_to_red, blue_to_green
    ]:
        all_colors.append(col)


class StaticColors:

    red = '255;0;0'
    green = '0;255;0'
    blue = '0;0;255'

    black = '255;255;255'
    white = '0;0;0'

    yellow = '255;255;0'
    purple = '255;0;255'
    cyan = '0;255;255'

    all_colors = [
        red, green, blue,
        black, white,
        yellow, purple, cyan
    ]


Colors = DynamicColors
Col = StaticColors


class Fade:

    def _check(line: str) -> bool:
        return line.strip()

    def Vertical(color: list, text: str, speed: int = 1, start: int = 0, stop: int = 0):

        lines = text.splitlines()
        result = ""

        nstart = 0
        color_n = 0
        for lin in lines:
            colorR = color[color_n]
            result += " " * \
                _MakeColors._getspaces(
                    lin) + _MakeColors._makeansi(colorR, lin.strip()) + "\n"

            if nstart != start:
                nstart += 1
                continue

            if Fade._check(lin):
                if (
                    stop == 0
                    and color_n + speed < len(color)
                    or stop != 0
                    and color_n + speed < stop
                ):
                    color_n += speed
                elif stop == 0:
                    color_n = 0
                else:
                    color_n = stop

        return result.strip()

    def Horizontal(color: list, text: str, speed: int = 1):
        lines = text.splitlines()
        result = ""

        for lin in lines:
            carac = list(lin)
            color_n = 0
            for car in carac:
                colorR = color[color_n]
                result += " " * \
                    _MakeColors._getspaces(
                        car) + _MakeColors._makeansi(colorR, car.strip())
                if color_n + speed < len(color):
                    color_n += speed
                else:
                    color_n = 0
            result += "\n"
        return result.strip()

    def Diagonal(color: list, text: str, speed: int = 1):
        lines = text.splitlines()
        result = ""
        color_n = 0
        for lin in lines:
            carac = list(lin)
            for car in carac:
                colorR = color[color_n]
                result += " " * \
                    _MakeColors._getspaces(
                        car) + _MakeColors._makeansi(colorR, car.strip())
                if color_n + speed < len(color):
                    color_n += speed
                else:
                    color_n = 1
            result += "\n"

        return result.strip()

    def DiagonalBackwards(color: list, text: str, speed: int = 1):

        lines = text.splitlines()
        result = ""
        resultL = ''
        color_n = 0
        for lin in lines:
            carac = list(lin)
            carac.reverse()
            resultL = ''
            for car in carac:
                colorR = color[color_n]
                resultL = " " * \
                    _MakeColors._getspaces(
                        car) + _MakeColors._makeansi(colorR, car.strip()) + resultL
                if color_n + speed < len(color):
                    color_n += speed
                else:
                    color_n = 0
            result = result + '\n' + resultL
        return result.strip()


class Colorate:
    def fade(color: str, r: int = None, g: int = None, b: int = None):
        if r is None:
            r = color[0]
        if g is None:
            g = color[0]
        if b is None:
            b = color[0]
        return f'{r};{g};{b}'

    def make(r: int, g: int, b: int):
        return f"{r};{g};{b}"

    def color(color: str, text: str, end: bool = False):
        return _MakeColors._maketext(color=color, text=text, end=end)

    def error(text: str, color: str = StaticColors.red, end: bool = False, spaces: bool = 1, enter: bool = True, wait: int = False):
        content = _MakeColors._maketext(
            color=color, text="\n" * spaces + text, end=end)
        if enter:
            var = input(content)
        else:
            print(content)
            var = None

        if wait is True:
            exit()
        elif wait is not False:
            sleep(wait)

        return var


class Anime:
    def anime(text: str, color: list, mode, time=True, interval=0.05, hide_cursor=True):
        if hide_cursor:
            Cursor.hide_cursor()

        if type(time) == int:
            time *= 15

        if time is True:
            while True:
                Anime._anime(text, color, mode, interval)
                ncolor = color[1:]
                ncolor.append(color[0])
                color = ncolor

        else:
            for _ in range(time):
                Anime._anime(text, color, mode, interval)
                ncolor = color[1:]
                ncolor.append(color[0])
                color = ncolor

        if hide_cursor:
            Cursor.show_cursor()

    def _anime(text: str, color: list, mode, interval: int):
        stdout.write(mode(color, text))
        sleep(interval)
        System.clear()


class Write:

    def write(text: str, color: list, interval=0.05, hide_cursor: bool = True):
        if type(color) == str:
            color = [color]

        if hide_cursor:
            Cursor.hide_cursor()

        lines = list(text)
        while True:
            if len(lines) <= len(color):
                break
            for col in color:
                color.append(col)

        n = 0
        for line in lines:
            stdout.write(_MakeColors._makeansi(color[n], line))
            stdout.flush()
            sleep(interval)
            if line.strip():
                n += 1
        if hide_cursor:
            Cursor.show_cursor()

    def winput(text: str, color: list, interval=0.05, hide_cursor: bool = True):
        if type(color) == str:
            color = [color]

        if hide_cursor:
            Cursor.hide_cursor()

        lines = list(text)
        while True:
            if len(lines) <= len(color):
                break
            for col in color:
                color.append(col)

        n = 0
        for line in lines:
            stdout.write(_MakeColors._makeansi(color[n], line))
            stdout.flush()
            sleep(interval)
            if line.strip():
                n += 1
        valor = input()
        if hide_cursor:
            Cursor.show_cursor()
        return valor


System.init()
