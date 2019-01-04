from d7a.system_files.access_profile import AccessProfileFile
from d7a.system_files.dll_config import DllConfigFile
from d7a.system_files.firmware_version import FirmwareVersionFile
from d7a.system_files.not_implemented import NotImplementedFile
from d7a.system_files.security_key import SecurityKeyFile
from d7a.system_files.system_file_ids import SystemFileIds
from d7a.system_files.uid import UidFile


class SystemFiles:
  files = {
    SystemFileIds.UID: UidFile(),
    SystemFileIds.FACTORY_SETTINGS: NotImplementedFile(SystemFileIds.FACTORY_SETTINGS.value, 0),
    SystemFileIds.FIRMWARE_VERSION: FirmwareVersionFile(),
    SystemFileIds.DEVICE_CAPACITY: NotImplementedFile(SystemFileIds.DEVICE_CAPACITY.value, 19),
    SystemFileIds.DEVICE_STATUS: NotImplementedFile(SystemFileIds.DEVICE_STATUS, 9),
    SystemFileIds.ENGINEERING_MODE: NotImplementedFile(SystemFileIds.ENGINEERING_MODE, 0),
    SystemFileIds.VID: NotImplementedFile(SystemFileIds.VID, 3),
    SystemFileIds.RFU_07: NotImplementedFile(SystemFileIds.RFU_07, 0),
    SystemFileIds.PHY_CONFIG: NotImplementedFile(SystemFileIds.PHY_CONFIG, 9),
    SystemFileIds.PHY_STATUS: NotImplementedFile(SystemFileIds.PHY_STATUS, 24),  # TODO assuming 3 channels for now
    SystemFileIds.DLL_CONFIG: DllConfigFile(),
    SystemFileIds.DLL_STATUS: NotImplementedFile(SystemFileIds.DLL_STATUS, 12),
    SystemFileIds.NWL_ROUTING: NotImplementedFile(SystemFileIds.NWL_ROUTING, 1),  # TODO variable routing table
    SystemFileIds.NWL_SECURITY: NotImplementedFile(SystemFileIds.NWL_SECURITY, 5),
    SystemFileIds.NWL_SECURITY_KEY: SecurityKeyFile(),
    SystemFileIds.NWL_SSR: NotImplementedFile(SystemFileIds.NWL_SSR, 4),  # TODO 0 recorded devices
    SystemFileIds.NWL_STATUS: NotImplementedFile(SystemFileIds.NWL_STATUS, 20),
    SystemFileIds.TRL_STATUS: NotImplementedFile(SystemFileIds.TRL_STATUS, 1),  # TODO 0 TRL records
    SystemFileIds.SEL_CONFIG: NotImplementedFile(SystemFileIds.SEL_CONFIG, 6),
    SystemFileIds.FOF_STATUS: NotImplementedFile(SystemFileIds.FOF_STATUS, 10),
    SystemFileIds.RFU_07: NotImplementedFile(SystemFileIds.RFU_14, 0),
    SystemFileIds.RFU_07: NotImplementedFile(SystemFileIds.RFU_15, 0),
    SystemFileIds.RFU_07: NotImplementedFile(SystemFileIds.RFU_16, 0),
    SystemFileIds.LOCATION_DATA: NotImplementedFile(SystemFileIds.LOCATION_DATA, 1),  # TODO 0 recorded locations
    SystemFileIds.ACCESS_PROFILE_0: AccessProfileFile(access_specifier=0),
    SystemFileIds.ACCESS_PROFILE_1: AccessProfileFile(access_specifier=1),
    SystemFileIds.ACCESS_PROFILE_2: AccessProfileFile(access_specifier=2),
    SystemFileIds.ACCESS_PROFILE_3: AccessProfileFile(access_specifier=3),
    SystemFileIds.ACCESS_PROFILE_4: AccessProfileFile(access_specifier=4),
    SystemFileIds.ACCESS_PROFILE_5: AccessProfileFile(access_specifier=5),
    SystemFileIds.ACCESS_PROFILE_6: AccessProfileFile(access_specifier=6),
    SystemFileIds.ACCESS_PROFILE_7: AccessProfileFile(access_specifier=7),
    SystemFileIds.ACCESS_PROFILE_8: AccessProfileFile(access_specifier=8),
    SystemFileIds.ACCESS_PROFILE_9: AccessProfileFile(access_specifier=9),
    SystemFileIds.ACCESS_PROFILE_10: AccessProfileFile(access_specifier=10),
    SystemFileIds.ACCESS_PROFILE_11: AccessProfileFile(access_specifier=11),
    SystemFileIds.ACCESS_PROFILE_12: AccessProfileFile(access_specifier=12),
    SystemFileIds.ACCESS_PROFILE_13: AccessProfileFile(access_specifier=13),
    SystemFileIds.ACCESS_PROFILE_14: AccessProfileFile(access_specifier=14)
  }

  def get_all_system_files(self):
    return sorted(self.files, key=lambda t: t.value)

