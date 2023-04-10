import os
Import("env")
env.Replace(PROGNAME="Luxuri_%s" % os.environ['LUXURI_FIRMWARE_NAME'])