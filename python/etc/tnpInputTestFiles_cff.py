import FWCore.ParameterSet.Config as cms


filesMiniAOD_Preliminary2018 = {
    'mc' :  cms.untracked.vstring(
        '/store/relval/CMSSW_10_6_4_patch1/RelValZEE_13/MINIAODSIM/PU25ns_106X_upgrade2018_realistic_v9_HS_resub-v1/10000/F5108D18-CE6C-2543-8F6F-D9173ED9C94C.root'
        ),

    'data' : cms.untracked.vstring(
        '/store/data/Run2018C/EGamma/MINIAOD/ForValUL2018-v2/230000/ECF32957-E451-E148-9DFA-A81011B4F118.root'
        )
}

filesAOD_Preliminary2018 = {
    'mc' :  cms.untracked.vstring(
#        '/store/mc/RunIISpring18DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/100X_upgrade2018_realistic_v10-v2/90001/FE8F7D45-133E-E811-891E-FA163EA4957D.root',
        ),
    'data' :  cms.untracked.vstring(
        '/store/data/Run2018B/EGamma/AOD/PromptReco-v1/000/317/864/00000/C269C719-EC71-E811-9C7E-FA163EF55202.root',
        )
}

filesAOD_Preliminary2017 = {
    'mc' :  cms.untracked.vstring(
        '/store/mc/RunIISummer19UL17RECO/DYJetsToEE_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/106X_mc2017_realistic_v6-v2/30000/FFCA4B4F-6AFD-D644-8CA6-C9264C6C0C68.root' ## UL17
#        '/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/AODSIM/PU2017RECOPF_94X_mc2017_realistic_v11-v1/50000/D42B8057-9F67-E811-9656-549F3525C4EC.root'
        ),
    'data' :  cms.untracked.vstring(
        '/store/data/Run2018B/ParkingBPH1/MINIAOD/05May2019-v2/230000/00775987-81BC-A246-91CB-6056E660D7AD.root',
#        '/store/data/Run2017B/DoubleEG/AOD/09Aug2019_UL2017-v1/260001/FA19C3F9-711B-1D4C-AF1C-CD772242B55B.root', ## UL17
        )
}

 
filesMiniAOD_Preliminary2017 = {
    'mc' :  cms.untracked.vstring(
#        '/store/mc/RunIISummer17MiniAOD/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10_ext1-v1/110000/02CF84A2-6086-E711-A3A1-0CC47A7C3458.root',#92X
        '/store/mc/RunIIFall17MiniAOD/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/94X_mc2017_realistic_v10-v1/20000/001C74A0-B4D6-E711-BD4B-FA163EB4F61D.root',#94X
        ),
    
    'data' : cms.untracked.vstring( 
        '/store/data/Run2017B/DoubleEG/MINIAOD/09Aug2019_UL2017-v1/50000/FC5478A2-1ADF-754E-B34B-3AA5A7119429.root',
        )
}

#OLD 2016 SAMPLES
filesMiniAOD_23Sep2016 = {
    'mc' :  cms.untracked.vstring(
        '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/120000/101D622A-85C4-E611-A7C2-C4346BC80410.root',
        ),
    
    'data' : cms.untracked.vstring( 
        '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/14415255-6B8C-E611-87D3-002590E3A212.root',
        )
}

filesAOD_23Sep2016 = {
    'mc' : cms.untracked.vstring(
        '/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/110000/00389155-1FB1-E611-A88A-001E674FB207.root',
        ),
    'data' : cms.untracked.vstring(
        '/store/data/Run2016B/SingleElectron/AOD/23Sep2016-v2/80000/0220DA0C-648C-E611-A9AA-0CC47A78A2F6.root',
        )
}
