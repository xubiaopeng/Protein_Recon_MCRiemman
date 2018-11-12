Energy minimization using Gromacs:

1) Install Gromacs-5.0
2) running following command step by step:


###   $1 is the pdb file before EM (input) $2 is output file name; 
   
   echo 6 | gmx pdb2gmx -f $1 -o $2_processed.gro -water tip3p -ignh -missing   
   ### (# 6: AMBER99SB-ILDN; 9: CHARMM36; 16: OPLSAA)
  
   gmx editconf -f $2_processed.gro -o $2_newbox.gro -c -d 1.0 -bt cubic

   gmx solvate -cp $2_newbox.gro -cs spc216.gro -o $2_solv.gro -p topol.top

   gmx grompp -f ions.mdp -c $2_solv.gro -p topol.top -o ions.tpr

   echo 13 | gmx genion -s ions.tpr -o $2_solv_ions.gro -p topol.top -pname NA -nname CL -neutral -conc 0.1

   gmx grompp -f minim.mdp -c $2_solv_ions.gro -p topol.top -o em.tpr 

   gmx mdrun -deffnm em

   echo 1 | gmx trjconv -f em.gro -s em.tpr -pbc mol -ur compact -o protein_$2.gro

3) protein_$2.gro is the final result, and change it to .pdb format using vmd.
