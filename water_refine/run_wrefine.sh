for f in $1/*.pdb
do
    f2=${f#*/protein_EM_}
    echo $f2
#    name=${f2%[0-9].pdb}
    name=${f2:0:4}
    echo $name    
    pdbfile=${f2};
    noefile=${name}_noe.tbl;
    dihedralfile=${name}_dihedral.tbl;
    sed "s/your_pdbfile/$pdbfile/g" wrefine.py | sed  "s/yourfolder/$name/g"  > wrefine_test1.py
    #| sed "53s/dihed_g_all.tbl/$dihedralfile/" | sed "72s/result/${name}"  > wrefine_xubiao_test1.py
    xplor -py wrefine_test1.py
done
