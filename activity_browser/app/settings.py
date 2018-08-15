# -*- coding: utf-8 -*-
import os
import json
import shutil

import appdirs

from .. import PACKAGE_DIRECTORY


class ABSettings():
    """
    Interface to the json settings file. Will create a userdata directory via appdirs if not
    already present.
    """
    def __init__(self):
        ab_dir = appdirs.AppDirs('ActivityBrowser', 'ActivityBrowser')
        self.data_dir = ab_dir.user_data_dir
        if not os.path.isdir(self.data_dir):
            os.makedirs(self.data_dir, exist_ok=True)
        self.settings_file = os.path.join(self.data_dir, 'ABsettings.json')
        self.move_old_settings()
        if os.path.isfile(self.settings_file):
            self.load_settings()
        else:
            self.settings = {}

    def move_old_settings(self):
        """
        legacy code: This function is only required for compatibility with the old settings file and
        can be removed in a future release
        """
        if not os.path.exists(self.settings_file):
            old_settings = os.path.join(PACKAGE_DIRECTORY, 'ABsettings.json')
            if os.path.exists(old_settings):
                shutil.copyfile(old_settings, self.settings_file)

    def load_settings(self):
        with open(self.settings_file, 'r') as infile:
            self.settings = json.load(infile)

    def write_settings(self):
        with open(self.settings_file, 'w') as outfile:
            json.dump(self.settings, outfile, indent=4, sort_keys=True)


ab_settings = ABSettings()
