
xplor.requireVersion("2.26")

#inputStructuresGlob="precalc/refine_1.sa"
inputStructuresGlob="proteins/protein_EM_your_pdbfile"
import glob
import sys

inputStructures=glob.glob(inputStructuresGlob)
#this could also be a list of filenames
#inputStructuresGlob=sys.argv[1]

simWorld.setRandomSeed( 785 )


import protocol

backbone="name C or name CA or name N or name O or name HN"

#Nilges topology/parameters
xplor.command('evaluate ($par_nonbonded = "OPLSX")')
protocol.parameters['protein']="waterRef/parallhdg5.3.pro.new"
protocol.parameters['water']  ="waterRef/parallhdg5.3.sol"
protocol.topology['protein']  ="waterRef/topallhdg5.3.pro.new"
protocol.topology['water']    ="waterRef/topallhdg5.3.sol"
waterResname="TIP3"
protocol.initParams(("protein","ion.par"))

#protocol.initStruct("zc2h2_waterref.psf")
protocol.loadPDB(inputStructures[0],deleteUnknownAtoms=True)

from potList import PotList
from simulationTools import MultRamp, StaticRamp, FinalParams
potList = PotList()
rampedParams=[]


# set up NOE potential
noe=PotList('noe')
potList.append(noe)
from noePotTools import create_NOEPot
for (name,scale,file) in [('all',1,"constraints/yourfolder/yourfoldernoe.tbl"),
                          #add entries for additional tables
                          ]:
    pot = create_NOEPot(name,file)
    # pot.setPotType("soft") - if you think there may be bad NOEs
    pot.setScale(scale)
    noe.append(pot)
rampedParams.append( MultRamp(2,30, "noe.setScale( VALUE )") )

# Set up dihedral angles
from xplorPot import XplorPot
protocol.initDihedrals("constraints/yourfolder/yourfolder_dihed_g_all.tbl",
                       useDefaults=False)
potList.append( XplorPot('CDIH') )
rampedParams.append( StaticRamp("potList['CDIH'].setScale(200)") )

from simulationTools import StructureLoop


def calcOneStructure( structData ):
    from waterRefineTools import refine
    refine(outFilename=structData.filename(),
           potList=potList,
           coolingParams=rampedParams,
#           keepWaters=True,
           waterResname=waterResname)
    pass


StructureLoop(pdbFilesIn=inputStructures,
              pdbTemplate="WRresult_your_pdbfile",
              structLoopAction=calcOneStructure,
              genViolationStats=True,
              averagePotList=potList,
              averageContext=FinalParams(rampedParams),
              ).run()
