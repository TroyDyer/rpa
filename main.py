import pywinmacro as pw
import time
import sys


# 크롬 시크릿창으로 실행
def chromeopen():
    pw.key_on("window")
    pw.key_on("r")
    pw.key_off("window")
    pw.key_off("r")
    time.sleep(0.5)
    pw.type_in('"chrome" -incognito')
    time.sleep(2)
    pw.key_press_once("enter")


# 다수의 로그인정보 처리 로직 만들다가 중단
# def checkaccount():


# 해외 영업지원 이메일 자동 로그인 후 받은편지함 이동
def emailautologin():

    # 크롬 시크릿창으로 실행
    chromeopen()
    time.sleep(2)

    # 웹메일 사이트 접속
    pw.type_in("webmail.koscom.co.kr")
    time.sleep(0.5)
    pw.key_press_once("enter")
    time.sleep(1)

    # 로그인 정보 입력 및 로그인
    # 기본 커서가 ID 입력창이므로 마우스 포지션 처리 작업 없음
    pw.type_in("")  # 이메일 정보는 개인 정보라 git에 올리는 파일에서는 제거. 추후 별도 txt 파일 분리로 개선 예정
    time.sleep(0.5)
    pw.key_press_once("tab")
    time.sleep(0.5)
    pw.type_in("")  # 이메일 정보는 개인 정보라 git에 올리는 파일에서는 제거. 추후 별도 txt 파일 분리로 개선 예정
    time.sleep(0.5)
    pw.key_press_once("enter")
    time.sleep(2)

    # '편지함'으로 커서 이동
    for i in range(7):
        pw.key_press_once("tab")
        time.sleep(0.1)

    # '편지함' 입장
    pw.key_press_once("enter")


emailautologin()
