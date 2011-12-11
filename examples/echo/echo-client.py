#! /usr/bin/env python

import MateCORBA
import CORBA
import sys

if len(sys.argv) != 2:
    print "usage: %s <message>" % sys.argv[0]
    sys.exit(1)

## this should no longer be needed, but is here as workaround to
## http://bugzilla.mate.org/show_bug.cgi?id=323201
## you also need to use this if the server is not MateCORBA2 based
MateCORBA.load_file("./echo.idl")
#import Test  # use this if the server is not MateCORBA2 based

orb = CORBA.ORB_init(sys.argv)

ior = file('iorfile').read()
echo = orb.string_to_object(ior)#._narrow(Test.Echo) # _narrow not needed with MateCORBA2 servers
print repr(echo)

if sys.argv[1] == 'quit':
    echo.quit()
else:
    print echo.echo(sys.argv[1])

