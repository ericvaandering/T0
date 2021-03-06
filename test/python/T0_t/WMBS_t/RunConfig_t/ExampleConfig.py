"""
_ExampleConfig_

Example configuration for RunConfig unittest

"""
from T0.RunConfig.Tier0Config import addDataset
from T0.RunConfig.Tier0Config import createTier0Config
from T0.RunConfig.Tier0Config import setAcquisitionEra
from T0.RunConfig.Tier0Config import setScramArch
from T0.RunConfig.Tier0Config import setDefaultScramArch
from T0.RunConfig.Tier0Config import setBackfill
from T0.RunConfig.Tier0Config import setBulkDataType
from T0.RunConfig.Tier0Config import setBulkDataLocation
from T0.RunConfig.Tier0Config import setDQMUploadUrl
from T0.RunConfig.Tier0Config import setPromptCalibrationConfig
from T0.RunConfig.Tier0Config import setConfigVersion
from T0.RunConfig.Tier0Config import ignoreStream
from T0.RunConfig.Tier0Config import addRepackConfig
from T0.RunConfig.Tier0Config import addExpressConfig
from T0.RunConfig.Tier0Config import addRegistrationConfig
from T0.RunConfig.Tier0Config import addConversionConfig

# Create the Tier0 configuration object
tier0Config = createTier0Config()

# set the config version (not really used at the moment)
setConfigVersion(tier0Config, "replace with real version")

# Set global parameters:
#  acquisition era
#  backfill mode
#  data type
setAcquisitionEra(tier0Config, "ExampleConfig_UnitTest")
setBackfill(tier0Config, None)
setBulkDataType(tier0Config, "data")
setBulkDataLocation(tier0Config, "T2_CH_CERN")
setDQMUploadUrl(tier0Config, "https://cmsweb.cern.ch/dqm/dev")
setPromptCalibrationConfig(tier0Config,
                           alcaHarvestTimeout = 12*3600,
                           alcaHarvestDir = "/some/afs/dir",
                           conditionUploadTimeout = 18*3600,
                           dropboxHost = "webcondvm.cern.ch",
                           validationMode = True)

# configure ScramArch
setDefaultScramArch(tier0Config, "slc5_amd64_gcc462")
setScramArch(tier0Config, "CMSSW_6_2_4", "slc5_amd64_gcc472")

# setup repack and express version mappings
repackVersionOverride = {
    }
expressVersionOverride = {
    "CMSSW_5_2_7" : "CMSSW_5_3_14",
    }
hltmonVersionOverride = {
    "CMSSW_5_2_7" : "CMSSW_5_3_8",
    }

addRepackConfig(tier0Config, "Default",
                proc_ver = 1,
                maxSizeSingleLumi = 1234,
                maxSizeMultiLumi = 1122,
                minInputSize = 210,
                maxInputSize = 400,
                maxEdmSize = 1233,
                maxOverSize = 1133,
                maxInputEvents = 500,
                maxInputFiles = 1111,
                versionOverride = repackVersionOverride)

addExpressConfig(tier0Config, "Express",
                 scenario = "pp",
                 multicore = 4,
                 data_tiers = [ "FEVT" ],
                 write_dqm = True,
                 maxInputRate = 1234,
                 maxInputEvents = 123,
                 maxInputSize = 123456789,
                 maxInputFiles = 1234,
                 maxLatency = 12 * 23,
                 alca_producers = [ "SiStripCalZeroBias", "PromptCalibProd" ],
                 dqm_sequences = [ "@common" ],
                 global_tag = "GlobalTag1",
                 reco_version = "CMSSW_6_2_4",
                 proc_ver = 2,
                 periodicHarvestInterval = 20 * 60,
                 blockCloseDelay = 3600,
                 versionOverride = expressVersionOverride)

addExpressConfig(tier0Config, "HLTMON",
                 scenario = "cosmics",
                 data_tiers = [ "FEVTHLTALL" ],
                 write_dqm = False,
                 global_tag = "GlobalTag2",
                 proc_ver = 3,
                 blockCloseDelay = 7200,
                 versionOverride = hltmonVersionOverride)

addDataset(tier0Config, "Default",
           do_reco = False,
           write_reco = False, write_aod = True, write_dqm = True,
           reco_delay = 60,
           reco_delay_offset = 30,
           reco_split = 2000,
           proc_version = 4,
           cmssw_version = "CMSSW_5_3_8",
           multicore = 8,
           global_tag = "GlobalTag3",
           archival_node = "Node1",
           blockCloseDelay = 24 * 3600,
           scenario = "pp")

addDataset(tier0Config, "Cosmics",
           do_reco = True,
           write_reco = True, write_aod = True, write_dqm = True,
           reco_split = 100,
           proc_version = 5,
           cmssw_version = "CMSSW_5_3_14",
           multicore = 4,
           global_tag = "GlobalTag4",
           alca_producers = [ "Skim1", "Skim2", "Skim3" ],
           archival_node = "Node2",
           tape_node = "Node3",
           disk_node = "Node4",
           scenario = "cosmics")

addDataset(tier0Config, "MinimumBias",
           write_reco = False, write_aod = False, write_dqm = False,
           reco_split = 200,
           proc_version = 6,
           cmssw_version = "CMSSW_6_2_4",
           global_tag = "GlobalTag5",
           alca_producers = [],
           archival_node = "Node5",
           scenario = "pp")

if __name__ == '__main__':
    print tier0Config
