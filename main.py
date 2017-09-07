#!/usr/bin/python

from network.server import Server, ServerCfg


_th = Server(ServerCfg)
_th.start()

_t = raw_input('Anykey to stop')

s = ServerCfg.sockobj
s.shutdown(0)

ServerCfg.run_ind = False

