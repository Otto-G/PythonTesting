# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

#added_files = [(r'C:\Users\z28bl\PycharmProjects\PythonTesting\venv2\Lib\site-packages\PyQt5\Qt\bin\Qt5Core.dll'),
#               (r'C:\Users\z28bl\PycharmProjects\PythonTesting\venv2\Lib\site-packages\PyQt5\Qt\bin\Qt5Gui.dll'),
#               (r'C:\Users\z28bl\PycharmProjects\PythonTesting\venv2\Lib\site-packages\PyQt5\Qt\bin\Qt5Widgets.dll)]


a = Analysis(['BasicGui.py'],
             pathex=[r'C:\\Users\\z28bl\\PycharmProjects\\PythonTesting\\PyInstaller with Qt5',
                     r'venv2\Lib\site-packages\PyQt5\Qt\bin'],
             binaries=[],
             # datas=added_files,
             datas=[(HOMEPATH + '\\PyQt5\\Qt\\bin\*', 'PyQt5\\Qt\\bin')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='BasicGui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
