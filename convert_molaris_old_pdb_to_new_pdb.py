#!/usr/bin/env python3
#
# This script converts the PDB files created by the old
# versions of MOLARIS to the standard format of ATOM and
# HEATM records.
#
# Author : Veselin Kolev <vesso.kolev@gmail.com>
# Version: 2018041400
# License: GPLv2
#
import sys
#
if len(sys.argv)!=3:
   #
   print('\nWrong number of input parameters!\n')
   #
   print('HINT: When invoking the program supply the input and '+\
         'output PDB file names as input parameters, for instance:\n')
   #
   print(sys.argv[0]+' input.pdb output.pdb\n')
   #
else:
   #
   inp_pdb=sys.argv[1]
   #
   out_pdb=sys.argv[2]
   #
   inp_file_obj=open(inp_pdb,'r')
   #
   out_file_obj=open(out_pdb,'w')
   #
   for i in inp_file_obj:
      #
      ident=i[0:6]
      #
      if ident=='ATOM  ' or ident=='HETATM':
         #
         serial=i[6:11]
         #
         aname=i[12:17]
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
         aname="%-4s" % ''.join(''.join(aname).split())
         #
         out_file_obj.write(ident+serial+' '+aname+alt+resname+\
                            chainID+resnum+achar+'   '+x+y+z+'\n')
         #
      else:
         #
         out_file_obj.write(i)
         #
   inp_file_obj.close()
   #
   out_file_obj.close()
   #
   print('\nSuccessfully done!\n')
   #
   sys.exit(1)

