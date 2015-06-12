
"""A simple python script.

"""

import os
import sys
import argparse
from classes.myclass import MyClass

def main(arguments):

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-n', '--name', help="Your name", default="Default", required=True)

    args = parser.parse_args(arguments)

    mc = MyClass(args.name)
    mc.sayName()
    print("Finished")

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
