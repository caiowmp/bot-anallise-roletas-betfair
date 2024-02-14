@echo off
pip install pyinstaller
pip install webdriver_manager
pip install selenium
pip install time
pip install apscheduler
pyinstaller --onefile -w main.py