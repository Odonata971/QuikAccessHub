# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['ui_home.py','component.py','kernel.py','template_service.py',
    'ui_config_page.py','ui_config_template.py','ui_help.py','globals.py'],
    pathex=[],
    binaries=[],
    datas=[('../json/templates.json', 'json'), ('../icons/QuikAccessHub_logo.ico', 'icons')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ui_home',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
