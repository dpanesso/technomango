# -*- coding: utf-8 -*-
#
# TP-Link Wi-Fi Smart Plug Protocol Client
# For use with TP-Link HS-100 or HS-110
#
# by David Panesso
#
# Credits to Lubomir Stroetmann
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#

import socket

# Set target IP and port
ip = '192.168.1.10'
port = 9999

# Predefined Smart Plug Commands
# For a full list of commands, consult tplink_commands.txt
commands = {
    'info': '{"emeter":{"get_realtime":{}},"schedule":{"get_next_action":{}},"system":{"get_sysinfo":{}},"cnCloud":{"get_info":{}}}',
    'on': '{"system":{"set_relay_state":{"state":1}}}',
    'off': '{"system":{"set_relay_state":{"state":0}}}',
    'cloudinfo': '{"cnCloud":{"get_info":{}}}',
    'wlanscan': '{"netif":{"get_scaninfo":{"refresh":0}}}',
    'time': '{"time":{"get_time":{}}}',
    'schedule': '{"schedule":{"get_rules":{}}}',
    'countdown': '{"count_down":{"get_rules":{}}}',
    'antitheft': '{"anti_theft":{"get_rules":{}}}',
    'reboot': '{"system":{"reboot":{"delay":1}}}',
    'reset': '{"system":{"reset":{"delay":1}}}',
    'emeter': '{"emeter":{"get_realtime":{}}}'
}


# Encryption and Decryption of TP-Link Smart Home Protocol
# XOR Autokey Cipher with starting key = 171
def encrypt(string):
    key = 171
    result = "\0\0\0\0"
    for i in string:
        a = key ^ ord(i)
        key = a
        result += chr(a)
    return result


def decrypt(string):
    key = 171
    result = ""
    for i in string:
        a = key ^ ord(i)
        key = ord(i)
        result += chr(a)
    return result


def send_cmd(cmd):
    try:
        sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_tcp.connect((ip, port))
        sock_tcp.send(encrypt(commands[cmd]))
        data = decrypt(sock_tcp.recv(2048)[4:])
        sock_tcp.close()
        return data
    except socket.error:
        quit("Cound not connect to host " + ip + ":" + str(port))
