from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import sys
config = config()

submitVersion = "JamboreeAug19"

doEleTree = 'doEleID=True'
doPhoTree = 'doPhoID=False'
doHLTTree = 'doTrigger=False'
doRECO    = 'doRECO=True'

mainOutputDir = '/store/group/phys_egamma/swmukher/Run3_DYtoEE/%s' % submitVersion

config.General.transferLogs = False

config.JobType.pluginName  = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName  = '/afs/cern.ch/user/s/swmukher/work/egammaNtuple/try/CMSSW_10_6_1_patch1/src/EgammaAnalysis/TnPTreeProducer/python/TnPTreeProducer_cfg.py'
config.Data.allowNonValidInputDataset = False

config.Data.inputDBS = 'global'
config.Data.publication = False

#config.Data.publishDataName = 
config.Site.storageSite = 'T2_CH_CERN'


if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea = 'crab_%s' % submitVersion

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)


    ##### submit MC
    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.Data.splitting     = 'FileBased'
    config.Data.unitsPerJob   = 20
    config.JobType.pyCfgParams  = ['isMC=True','isAOD=True',doEleTree,doPhoTree,doHLTTree,doRECO]
    config.Data.allowNonValidInputDataset = True

    config.General.requestName  = 'ttbar_semilep_2023'
#    config.Data.inputDataset    = '/TTToSemiLeptonic_TuneCP5_14TeV-powheg-pythia8/Run3Summer19DRPremix-2021Scenario_106X_mcRun3_2021_realistic_v3-v2/AODSIM'
#    config.Data.inputDataset    = '/TTToSemiLeptonic_TuneCP5_14TeV-powheg-pythia8/Run3Summer19DRPremix-2024Scenario_106X_mcRun3_2024_realistic_v4-v2/AODSIM'
    config.Data.inputDataset    = '/TTToSemiLeptonic_TuneCP5_14TeV-powheg-pythia8/Run3Summer19DRPremix-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/AODSIM'
#    config.Data.inputDataset    = '/TTbar_14TeV_TuneCP5_Pythia8/Run3Summer19DR-106X_mcRun3_2023_realistic_v3-v2/AODSIM'
    submit(config) 

#    config.General.requestName  = 'dyjets_NonValidInputDataset'
#    config.Data.inputDataset    = '/DYJets_incl_MLL-50_TuneCP5_14TeV-madgraphMLM-pythia8/Run3Summer19DRPremix-2023Scenario_106X_mcRun3_2023_realistic_v3-v1/AODSIM'
#    submit(config) 

#    config.General.requestName  = 'DYtoEE_2021_powheg'
#    config.Data.inputDataset    = '/DYToEE_M-50_NNPDF31_TuneCP5_14TeV-powheg-pythia8/Run3Summer19DRPremix-2021Scenario_106X_mcRun3_2021_realistic_v3-v2/AODSIM'
#    submit(config) 

#    config.General.requestName  = 'DYtoEE_2023_powheg'
#    config.Data.inputDataset    = '/DYToEE_M-50_NNPDF31_TuneCP5_14TeV-powheg-pythia8/Run3Summer19DRPremix-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/AODSIM'
#    submit(config) 

#    config.General.requestName  = 'DYtoEE_2024_powheg'
#    config.Data.inputDataset    = '/DYToEE_M-50_NNPDF31_TuneCP5_14TeV-powheg-pythia8/Run3Summer19DRPremix-2024Scenario_106X_mcRun3_2024_realistic_v4-v2/AODSIM'
#    submit(config) 


#    config.General.requestName  = 'DYJetsToLL_M50_amcatnloFXFX'
#    config.Data.inputDataset    = '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/AODSIM'
#    submit(config) 



    
