Water refinement: Software XPLOR is used here.

The procedure for water refinement using XPLOR:

1) Install XPLOR 2.26 (If you are using later version, please change the corresponding information in wrefine.py)
2) Put the input pdb file into the folder "proteins";

   Put the input restraints files into the folder "constraints" (See examples "1b4r" in folder "constraints"): There are two restraints files needed: *_dihed_g_all.tbl, *noe.tbl (* denotes the pdb name, "*_dihed_g_all.tbl" means the Ramachandran angle restraints, "*noe.tbl" means the NOE distance restraints). These .tbl files can be obtained from the webpage "http://restraintsgrid.bmrb.wisc.edu/NRG/MRGridServlet". However, sometimes some necessary changes on the *noe.tbl file are needed for example:  1. the string "segid “A” and" in the .tbl file should be deleted 2.The distance restaints related to NH atom in the first resiude should be removed.    3. Any distance restraints related to the HD1 atom on HIS residue need to be removed (see the examples "1b4rnoe.tbl" in folder "constraints/1b4r/")

3) In current directory, run the command:
   ./run_wrefine.sh proteins
   The final results will be generated under the current directory.
