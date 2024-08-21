import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
import os

# Create an options object
options = VarParsing('analysis')

# Add a new option for the text file containing input file paths
options.register('inputFileList',
                 '',
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.string,
                 "Path to the text file containing input file paths")

# Parse the arguments
options.parseArguments()

# Create a cms.Process
process = cms.Process('XSec')

# Set the max events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

# Load the MessageLogger
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100000

# Read input files from the text file if provided
input_files = []
if options.inputFileList:
    if os.path.exists(options.inputFileList):
        with open(options.inputFileList, 'r') as f:
            input_files = [line.strip() for line in f if line.strip()]

# Set up the source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(input_files if input_files else options.inputFiles),
    secondaryFileNames = cms.untracked.vstring()
)

# Set up the analyzer
process.xsec = cms.EDAnalyzer("GenXSecAnalyzer")

# Define the path and schedule
process.ana = cms.Path(process.xsec)
process.schedule = cms.Schedule(process.ana)
