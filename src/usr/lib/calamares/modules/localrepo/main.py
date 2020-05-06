#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# === This file is part of Calamares - <https://github.com/calamares> ===
#
#   Copyright 2016, Artoo <artoo@manjaro.org>
#   Copyright 2017, Alf Gaida <agaida@siduction.org>
#   Copyright 2018, Gabriel Craciunescu <crazy@frugalware.org>
#   Copyright 2019, Adriaan de Groot <groot@kde.org>
#
#   Calamares is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Calamares is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Calamares. If not, see <http://www.gnu.org/licenses/>.

import libcalamares

from libcalamares.utils import debug, target_env_call

import gettext
_ = gettext.translation("calamares-python",
                        localedir=libcalamares.utils.gettext_path(),
                        languages=libcalamares.utils.gettext_languages(),
                        fallback=True).gettext


def pretty_name():
    return _("Start local repo")


class LocalRepo:

    def __init__(self):
        self.__root = libcalamares.globalstorage.value('rootMountPoint')

    @property
    def root(self):
        return self.__root

    '''def setTheme(self):
        plymouth_theme = libcalamares.job.configuration["plymouth_theme"]
        target_env_call(["sed", "-e", 's|^.*Theme=.*|Theme=' +
                         plymouth_theme + '|', "-i",
                         "/etc/plymouth/plymouthd.conf"])

    def detect(self):
        isPlymouth = target_env_call(["sh", "-c", "which plymouth"])
        debug("which plymouth exit code: {!s}".format(isPlymouth))

        return isPlymouth'''

    def run(self):
        target_env_call(["mv","/etc/pacman.conf","/etc/pacman.conf.bak"])
        target_env_call(["mv","/etc/pacman.d/installpkgs","/etc/pacman.conf"])
        target_env_call(["pacman","-Sy"])
        return None


def run():
    lr = LocalRepo()
    return lr.run()
