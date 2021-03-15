
from cx_Freeze import setup, Executable

executables = [Executable('main.py',
                          targetName='main.exe',
                          base='Win32GUI',
                          icon='rocket.ico'
                          )]

# excludes = ['unittest', 'email', 'html', 'http', 'urllib',
#             'xml', 'bz2']
#
# options = {
#     'build_exe': {
#         'include_msvcr': True,
#         'excludes': excludes,
#     }
# }
setup(
    name = "AChS",
    version = "0.1",
    description = "AChS",
    executables = executables,
    # options=options
)

# pyuic5 GUI.ui -o GUI.py - конвертирование из .ui в .py
# python.exe setup.py build - компиляция в .exe