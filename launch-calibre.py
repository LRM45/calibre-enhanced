#!/usr/bin/env python3
"""Calibre launcher with all patches applied"""
import sys
import os

BASE = '/home/marco/calibre-dev'

sys.frozen = False
sys.calibre_dev = True
sys.extensions_location = BASE + '/src/calibre/plugins/'
sys.resources_location = BASE + '/resources/'
sys.appdata = os.path.expanduser('~/.local/share/calibre')
sys.confdir = os.path.expanduser('~/.config/calibre')
sys.executables_location = BASE + '/src/calibre/executables/'
sys.argv0 = BASE
sys.executable = sys.executable
sys._prog_name = 'calibre'
sys.is_frozen = False

if BASE + '/src' not in sys.path:
    sys.path.insert(0, BASE + '/src')

os.environ['CALIBRE_ESPEAK_DATA_DIR'] = '/opt/piper-tts/espeak-ng-data/'
os.environ['CALIBRE_PIPER_VOICES_DIR'] = '/usr/share/piper-voices'
# NOTE: Removed CALIBRE_TEMP_DIR - ptempfile.py handles this internally

from calibre.gui2.main import main
sys.exit(main())
