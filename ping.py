#!/usr/bin/env python3

import datetime
import time

import lib.ping as ping

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

def okstring(s):
  return f"{bcolors.OKCYAN}" + s + f"{bcolors.ENDC}"

def ngstring(s):
  return f"{bcolors.FAIL}{bcolors.UNDERLINE}" + s + f"{bcolors.ENDC}"

def tryping(instance, url):
  ret = instance.ping(url)
  return [ret.is_reached(), ret.messages]

p = ping.Ping(keep=True)
interval = 3
logname = datetime.datetime.now().strftime("%Y-%m-%d.log")
log = open(logname, 'a')
while True:
  [succeeded, msg] = tryping(p, 'google.com')
  if succeeded:
    log.write(f"OK: {datetime.datetime.now()}\n")
    print(f"{okstring('OK')}: {datetime.datetime.now()}")
  else:
    log.write(f"NG: {datetime.datetime.now()} [{msg}]\n")
    print(f"{ngstring('NG')}: {datetime.datetime.now()} [{msg}]")
  log.flush()
  time.sleep(interval)
