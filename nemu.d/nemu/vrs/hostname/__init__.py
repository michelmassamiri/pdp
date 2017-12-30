# ------------------------------------------------------
# -- NEmu : The Network Emulator for Mobile Universes --
# ------------------------------------------------------

# Copyright (C) 2011-2016  Vincent Autefage

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.

#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

# http://nemu.valab.net

from nemu.vrc import VRc

def init(vrouter, *largs, **kargs):
    fd = VRc(name='hostname', id='00', vrouter=vrouter)
    fd.write('hostname ' + str(vrouter.name) + ';')
    fd.write('echo ' + str(vrouter.name) + ' > /etc/hostname;')
    fd.close()

def help():
    ret = dict()
    ret['syn'] = 'Service("hostname")'
    ret['desc'] = 'Sets the hostname of the VRouter'
    ret['args'] = list()
    return ret
