import sys,os
from datetime import datetime
import curses

"""
총 타자수
타자 속도(분)

화면은 내용을 넣고
refresh()해야 한다.
다음 키보드 입력을 기다린다.
한글 입력이 되는가?
"""

def iamtyping(stdscr): # wrapper를 쓰면 stdscr = curses.initscr로 안 해도 되는 것 같다.
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(1) # hide cursor

    total_keystrokes = 0
    total_time = 0
    average_speed = 0
    start = datetime.now()
    cursor_x = 0
    cursor_y = 0
    inputstr = ""
    index = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        information = f"타자수: {total_keystrokes} | 총시간: {total_time}초 | 타자속도: {average_speed}/분"
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, information)
        # TODO: 한글과 같이 멀티 바이트 문자는 그 만큼의 갯수를 더해 줘야 한다. 이걸 대신할 함수를 만들자.
        information_len = len(information) + 12
        stdscr.addstr(height-1, information_len, " " * (width - 1 - information_len))
        stdscr.attroff(curses.color_pair(3))

        # test statement
        # TODO: 임의의 문장 입력하기
        teststr = "This is testing."

        # TODO: 변수이름을 바꾼다.
        cursor_y = int(height / 2)
        cursor_x = int((width - len(teststr)) / 2)
        stdscr.attron(curses.color_pair(2))
        stdscr.addstr(cursor_y - 2, cursor_x, teststr)
        stdscr.attroff(curses.color_pair(2))

        stdscr.attron(curses.color_pair(1))
        seperator = "------"
        stdscr.addstr(cursor_y, int((width - len(seperator)) / 2), seperator)
        stdscr.addstr(cursor_y + 2, cursor_x, inputstr)
        stdscr.attroff(curses.color_pair(1))

        stdscr.refresh()

        keystroke = stdscr.getch()
        index += 1

        # TODO: IndexError - 엔터와 같이 처리하기
        # TODO: 아래 순환문 정리하기
        if keystroke == curses.KEY_BACKSPACE and total_keystrokes != 0:
            total_keystrokes -= 1
        elif keystroke != ord(teststr[index - 1]):
            pass
        else:
            total_keystrokes += 1

        if keystroke == ord("\n"):
            inputstr = ""
            index = 0
            stdscr.move(cursor_y, cursor_x)
            # TODO: instant speed를 따로 출력하자.
        elif keystroke == curses.KEY_BACKSPACE and inputstr != "":
            inputstr = inputstr[:-1]
            index -= 1
        else:
            inputstr += chr(keystroke)

        total_time = int((datetime.now() - start).total_seconds())
        if total_time == 0:
            average_speed = 0
        else:
            average_speed = int((total_keystrokes / total_time) * 60)


def main():
    curses.wrapper(iamtyping)

if __name__ == "__main__":
    main()
