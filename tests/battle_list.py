#!/usr/bin/python
# coding: utf-8
# Copyright (C) 2010 Lucas Alvares Gomes <lucasagomes@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

from tibiadevel.object.client import Client
from tibiadevel.object.battle_list import BattleList
from tibiadevel.dicts import skull

if __name__ == '__main__':
    a = Client()
    b = BattleList()

    INFOS = "Name: %s\nHP: %d%%\nSkull: %s\n"

    for i in b.get_entities():
        print INFOS % (i.name, i.hp_bar, skull[i.skull_icon])
