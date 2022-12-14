# ๐ฎ Sudoku Game Solver

## Showcase
<img src="https://user-images.githubusercontent.com/25794814/202914214-292a9b2a-6e12-4588-a423-075c7b09f50e.gif" alt="drawing" width="250"/>

## Description
* 2022๋ ๊ตญ๋ฏผ๋ ์ด๋ฏผ์ ๊ต์๋ ์ฌ์ ๋ํ์ธ๋ฏธ๋ ๊ฐ์ข ๊ฐ๋ฐ ๋ฌธํ ์ฒดํ์ฉ ํ ์ด ํ๋ก์ ํธ
* ์ค๋์ฟ  ๋ฌธ์ ๋ฅผ ํ์ด ์ฃผ๋ ๋ฐฑ-ํธ๋ํน ์๊ณ ๋ฆฌ์ฆ
* PyQT6 ํ๋ ์์ํฌ๋ฅผ ํ์ฉํ GUI

## Dev Environment
* IDE : Pycharm 2022.2.4 (Professional Edition)
* Language : Python 3.9
* Package Manager : pip
* style : PEP8
* OS : macOS Ventura 13.0.1
* Machine : MacBook Pro 14-inch, 2021
* Chip : Apple M1 Pro

## Install
1. ํ์ด์ฌ 3.9 ๊ธฐ๋ฐ์ ๊ฐ์ ํ๊ฒฝ์ ๊ตฌ์ฑ **(๊ถ์ฅ)**
    ```Shell
    python3 -m venv ๊ฐ์ํ๊ฒฝ์ด๋ฆ
    source .๊ฐ์ํ๊ฒฝ์ด๋ฆ/bin/activate
    ```
2. ํ์ด์ฌ ๊ฐ์ ํ๊ฒฝ ์์ pip ๋ฅผ ํตํด ์์กด์ฑ ์ค์น
    ```Shell
    pip install -r requirements.txt
    ```

3. ํ๋ก๊ทธ๋จ ์คํ
    ```Shell
    python3 main.py
    ```
   
## How To Use
1. ํ๋ก๊ทธ๋จ์ ์คํ
2. ๊ฒ์ ํ์ ํ๊ณ  ์ถ์ ์๋์ฟ  ๋ฌธ์  ์ซ์๋ฅผ ์๋ ฅ
3. Solve ๋ฒํผ์ ํด๋ฆญ ํ์ฌ ๋ฌธ์ ๋ฅผ ํด๊ฒฐ
4. Reset ๋ฒํผ์ ํด๋ฆญ ํ์ฌ ์๋ก์ด ๋ฌธ์ ๋ฅผ ์๋ ฅ

## Unit Test
* ํ๋ก๊ทธ๋จ์ ์ ์ง ๋ณด์๊ฐ ํ์ํ ๊ฒฝ์ฐ ๋จ์ ํ์คํธ ํ์ฉ
   ```Shell
  python3 -m unittest UnitTest/SudokuGameUnitTest.py
   ```

## Copyright
* Copyright (C) 2022 JeongTaek Han All Right Reserved