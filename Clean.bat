@echo off
chcp 65001
echo 1-删除Merged内容	
echo 2-删除Output内容	
echo 3-删除Receipts内容 
echo 4-清空这三个文件夹	
echo.
set /p choice=请输入编号选择操作：


if "%choice%"=="1" (
    del /q "Merged\*"
    echo Merged内容已删除。
)

if "%choice%"=="2" (
    del /q "Output\*"
    echo Output内容已删除。
)

if "%choice%"=="3" (
    del /q "Receipts\*"
    echo Receipts内容已删除。
)

if "%choice%"=="4" (
    del /q "Merged\*"
    del /q "Output\*"
    del /q "Receipts\*"
    echo Merged、Output和Receipts的内容已清空。
)

pause
