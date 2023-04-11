import os
Import("env")

filename = ""
version = os.environ.get('LUX_VERSION')
build = os.environ.get('LUX_BUILD')
config = os.environ.get('LUX_CONFIG_NAME')
release = os.environ.get('LUX_RELEASE')

filename = version
if release != "1":
    filename += "." + build
filename += " " + config

env.Replace(PROGNAME="Luxuri %s" % filename)
