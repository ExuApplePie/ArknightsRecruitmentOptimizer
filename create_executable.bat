rem This script will create a venv and install the required packages and then create the executable
rem This script will only work on Windows
python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
pip install pyinstaller
pyinstaller --clean -F -n OptimalRecruitmentChecker main.py
exit
```