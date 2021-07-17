#!/usr/bin/env python3
'''OMSimulator command line client'''

import OMSimulator

def _main():
  oms = OMSimulator.OMSimulator()
  print(oms.getVersion())

if __name__ == '__main__':
  _main()
