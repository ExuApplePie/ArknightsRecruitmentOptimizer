MUST INSTALL [https://github.com/UB-Mannheim/tesseract/releases](https://github.com/UB-Mannheim/tesseract/wiki) and add to PATH

Set constants in const.py. Then run create_executable.bat and find the executable in /dist/. Only supports English, and Windows only.
The emulator must also be on the primary monitor.
The constants you should set are:
- `EMULATOR_NAME`: The name of the emulator window. You can find this by hovering over the emulator window in the taskbar. Case-sensitive
- `EMULATOR_SIZE`: The size of the emulator window. As long as your monitor is larger than this it should be fine.
- `IS_BLUESTACKS`: If it is bluestacks (or equivalently there is a thing on top of your emulator)
- `ENABLE_STARTER_TAG`: If you want to enable the starter tag
- `KEYS`: self-explanatory
- `SAVE_TO_MEMORY`: If you want to save to memory instead of a file
