# 🎮 Sudoku Game Solver

## Showcase
<img src="https://user-images.githubusercontent.com/25794814/202914214-292a9b2a-6e12-4588-a423-075c7b09f50e.gif" alt="drawing" width="250"/>

## Description
* 2022년 국민대 이민석 교수님 사제동행세미나 강좌 개발 문화 체험용 토이 프로젝트
* 스도쿠 문제를 풀어 주는 백-트랙킹 알고리즘
* PyQT6 프레임워크를 활용한 GUI

## Dev Environment
* IDE : Pycharm 2022.2.4 (Professional Edition)
* Language : Python 3.9
* Package Manager : pip
* style : PEP8
* OS : macOS Ventura 13.0.1
* Machine : MacBook Pro 14-inch, 2021
* Chip : Apple M1 Pro

## Install
1. 파이썬 3.9 기반의 가상 환경을 구성 **(권장)**
    ```Shell
    python3 -m venv 가상환경이름
    source .가상환경이름/bin/activate
    ```
2. 파이썬 가상 환경 에서 pip 를 통해 의존성 설치
    ```Shell
    pip install -r requirements.txt
    ```

3. 프로그램 실행
    ```Shell
    python3 main.py
    ```
   
## How To Use
1. 프로그램을 실행
2. 게임 판에 풀고 싶은 수도쿠 문제 숫자를 입력
3. Solve 버튼을 클릭 하여 문제를 해결
4. Reset 버튼을 클릭 하여 새로운 문제를 입력

## Unit Test
* 프로그램의 유지 보수가 필요한 경우 단위 테스트 활용
   ```Shell
  python3 -m unittest UnitTest/SudokuGameUnitTest.py
   ```

## Copyright
* Copyright (C) 2022 JeongTaek Han All Right Reserved