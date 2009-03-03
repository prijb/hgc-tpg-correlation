import FWCore.ParameterSet.Config as cms

hltHITdqm = cms.EDAnalyzer('DQMHcalIsoTrackHLT',
folderName=cms.string("HLT/AlCa_IsoTrack"),
outputRootFileName=cms.string("hltHITdqm.root"),

hltRAWTriggerEventLabel=cms.string("hltTriggerSummaryRAW"),
hltAODTriggerEventLabel=cms.string("hltTriggerSummaryAOD"),

useHLTDebug=cms.bool(False),
l2collectionLabel=cms.string("hltIsolPixelTrackProd"),
l3collectionLabel=cms.string("hltHITIPTCorrector"),
                             
hltL3filterLabel=cms.string("hltIsolPixelTracksFilter"),
hltL2filterLabel=cms.string("hltIsolPixelTrackFilterL2"),
hltL1filterLabel=cms.string("hltL1sHLTIsoTrack"),
                             
hltProcessName=cms.string("HLT")
)
