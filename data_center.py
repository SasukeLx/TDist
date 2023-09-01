import json
import os
from dataclasses import dataclass
from typing import Mapping

@dataclass
class ExecResult:
    stdout: str
    stderr: str
    returncode: int
    time: float

class DataCenter:
    """
    DataCenter class.
    """

    exec_result: Mapping[str, ExecResult] = {}
    simulator: str
    timeout: int
    workspace: str
    logpath: str

    def __init__(self, config_file: str) -> None:
        self.config_file = config_file
        self.parse_config_file()

        
    def parse_config_file(self) -> None:
        """
        Parse the config file.
        """
        with open(self.config_file, "r") as f:
            self.exec_result = json.load(f)

        self.simulator = self.exec_result["simulator"]
        self.timeout = self.exec_result["timeout"] * 60  # second
        self.workspace = self.exec_result["workspace"]
        self.logpath = self.exec_result["logpath"]
        
    def get_exec_result(self, tc_idx: str or int) -> str:
        """
        Get the exec result by tc index.
        """
        return self.exec_result[tc_idx]
    
    def set_exec_result(self, tc_idx: str or int, exec_result: ExecResult) -> None:
        """
        Set the exec results by tc index and exec_result.
        """
        self.exec_result[tc_idx] = exec_result

    @staticmethod
    def get_exec_log(tc_idx: str or int) -> str:
        """
        Get the path to the data file.
        """
        return os.path.join(DataCenter.get_data_path(), tc_idx)


data_center = DataCenter('./config.json')
