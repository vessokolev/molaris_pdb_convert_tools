## MOLARIS PDB convert tools

### Tools for checking and converting PDB files created by old versions of MOLARIS.

#### Author: Veselin Kolev <vesso.kolev@gmail.com>
#### Released under GPLv2 licence.
#### Version: 2018041400

#### Content:

#### 1. Introduction.
#### 2. How to download the source code of the project.
#### 3. Identifying if the PDB matches the old format.
#### 4. Converting the PDB into the standard PDB format.


_1. Introduction_

When writing the content of PDB files, the old versions of MOLARIS simulation package do shift with one position left the atom name records. That is not a major error, but sometimes it might cause problems, especially when reading the PDB for sake of analysis by using tools like VMD and USCF Chimera.

The Python 3 scripts provided here help to identify and convert those PDB files.

_2. How to download the source code of the project._

The preferable method for obtaining the code is to use the tool ``git`` and clone the source tree locally to your file system:

```
git clone https://github.com/vessokolev/molaris_pdb_convert_tools.git
```

You may download the source as a ZIP-archive by pressing the button "Clone or download" in the web-interface on GitHub, or by using wget:

```
wget https://github.com/vessokolev/molaris_pdb_convert_tools/archive/master.zip
```

_3. Identifying if the PDB matches the old format._

To check if a PDB file is created by an old MOLARIS version, invoke the script ``check_if_pdb_is_in_old_molaris_format.py``:

```
check_if_pdb_is_in_old_molaris_format.py input.pdb
```

If ``input.pdb`` matches the old format, the following message will appear on the screen:

```
The supplied PDB file matches the old MOLARIS format! Do convert it!
```

When finishing, the script returns a value to the invoking shell. If the return value is 0, then the PDB file should not be converted. If the value is 2, a conversion need to be performed. Using the code can help organizing batch script for checking and (eventually) converting large number of PDB files.

_4. Converting the PDB into the standard PDB format._

To convert a PDB file from the old to the standard format of ATOM and HETATM records, invoke the script ``convert_molaris_old_pdb_to_new_pdb.py`` by giving as parameters the name of the PDB file that needs to be converted and the output PDB file name. For example:

```
convert_molaris_old_pdb_to_new_pdb.py input.pdb output.pdb
```

