#!/usr/bin/python
#TODO Export Configs in extra File
from network.server import Server, ServerCfg, shut_down

_th = Server(ServerCfg)
_th.start()

_t = raw_input('Anykey to stop')

shut_down(ServerCfg)

