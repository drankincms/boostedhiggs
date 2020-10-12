import json

xs = {
    "WW_TuneCP5_13TeV-pythia8": 75.82,
    "WZ_TuneCP5_13TeV-pythia8": 27.6,
    "ZZ_TuneCP5_13TeV-pythia8": 12.14,
    "QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 248600000.,
    "QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 27990000.,
    "QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 9999999.,#FIXME
    "QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 322600.,
    "QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 29980.,
    "QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 6334.,
    "QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 1088.,
    "QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 99.11,
    "QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 20.23,
    "DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8": 6225.42,
    "DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8": 161.1,
    "DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8": 48.58,
    "DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8": 5.678,
    "DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8": 1.738,
    "DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8": 0.8077,
    "DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8": 0.1514,
    "DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8": 0.003435,
    "WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8": 52940.,
    "WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8": 999999.,#FIXME
    "WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8": 1395.,
    "WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8": 407.9,
    "WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8": 57.48,
    "WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8": 12.87,
    "WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8": 5.366,
    "WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8": 1.074,
    "WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8": 0.008001,
    "WJetsToQQ_HT400to600_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8": 315.6,
    "WJetsToQQ_HT600to800_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8": 68.57,
    "WJetsToQQ_HT-800toInf_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8": 34.9,
    "ZJetsToQQ_HT400to600_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8": 145.4,
    "ZJetsToQQ_HT600to800_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8": 34.0,
    "ZJetsToQQ_HT-800toInf_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8": 18.67,
    "ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8": 11.24,
    "ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8": 3.74,
    "ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8": 67.91,
    "ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8": 113.3,
    "ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8": 34.97,
    "ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8": 34.91,
    "TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8": 88.29,
    "TTToHadronic_TuneCP5_13TeV-powheg-pythia8": 377.96,
    "TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8": 365.34,
    "GluGluHToTauTau": 0.0398
}

with open('xsec.json', 'w') as outfile:
    json.dump(xs, outfile, indent=4)
