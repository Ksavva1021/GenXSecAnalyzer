# Instructions

 GenXSecAnalyzer can be used to compute the cross section correctly in the MC production or for the physics analysis (on an existing MC sample, in MINIAODSIM format file)

 # Step 1: Set up CMSSW version

The CMSSW release must not predate the release that was used in writing the input files. For the example input files here, CMSSW `13_0_13` was used.

```
cmsrel CMSSW_13_0_13
cd CMSSW_13_0_13/src
cmsenv
```

# Step 2: Clone the repository

```
git clone git@github.com:Ksavva1021/GenXSecAnalyzer.git
cd GenXSecAnalyzer
```

# Step 3: Produce the input `.txt` files

We utilise `dasgoclient` to get the list of files in the sample of interest.

```
dasgoclient -query="file dataset=/GluGluHJJto2TauUncorrelatedDecay_CP-mix_M-125_CP5_13p6TeV_powheg-minlo-pythia
8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM" &> GluGluHJJto2TauUncorrelatedDecay_CP-mix.txt
```

# Step 4: Run `ana.py` to compute cross-sections/filter-efficiencies

Note: You can set the maxEvents to your preference: -1 $\rightarrow$ whole file

```
cmsRun ana_new.py inputFileList=GluGluHJJto2TauUncorrelatedDecay_CP-odd.txt maxEvents=-1
```
