#!/usr/bin/env python3
#
# This script checks the input PDB file is created by
# the old versions of MOLARIS which does not conform the
# the standard positioning of ATOM and HEATM records.
#
# Author : Veselin Kolev <vesso.kolev@gmail.com>
# Version: 2018041400
# License: GPLv2
#
import sys
#
# Check the Python version.
#
version=sys.version_info
#
if version.major<3 or (version.major==3 and version.minor<4):
   #
   print('\nRunning this script requires Python 3.4 or higher.\n')
   #
   sys.exit(1)
   #
import os
#
if len(sys.argv)<2:
   #
   print('\nFATAL ERROR: Wrong number of parameters supplied!\n')
   #
   print('Invoke the program by supplying the PDB file as first '+\
          'and only argument. For example:\n')
   #
   print(sys.argv[0]+' file.pdb\n')
   #
   sys.exit(1)
   #
if not os.path.isfile(sys.argv[1]):
      #
      print('\nFATAL ERROR: The PDB file\n')
      #
      print(sys.argv[1]+'\n')
      #
      print('either does not exists or it is not accessible to '+\
            'the user invoking this program.\n')
      #
      sys.exit(1)
      #
if len(sys.argv)!=2:
   #
   print('\nWrong number of input parameters!\n')
   #
   print("HINT: When invoking the program supply the input and '+\
         'output PDB file names as input parameters, for instance:\n")
   #
   print(sys.argv[0]+" input.pdb output.pdb\n")
   #
else:
   #
   anames=[]
   #
   inp_pdb=sys.argv[1]
   #
   inp_file_obj=open(inp_pdb,'r')
   #
   for i in inp_file_obj:
      #
      ident=i[0:6]
      #
      if ident=='ATOM  ' or ident=='HETATM':
         #
         serial=i[6:11]
         #
         anames.append(i[12:17])
         #
         alt=' '
         #
         resname=i[17:20]
         #
         chainID=i[20]
         #
         resnum=i[21:26]
         #
         achar=i[26]
         #
         x=i[30:38]
         #
         y=i[38:46]
         #
         z=i[46:54]
         #
   inp_file_obj.close()
   #
   flag=False
   #
   for i in anames:
      #
      if i[0]==' ':
         #
         flag=True
         #
   if flag:
      #
      print('\nThe supplied PDB file matches the old MOLARIS format! Do convert it!\n')
      #
      sys.exit(2)
      #
   else:
      #
      print('\nThe supplied PDB file matches the new MOLARIS format! Do not convert it!\n')
      #
      sys.exit(0)
