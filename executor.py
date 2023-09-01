from workmode import WorkMode
from typing import Dict, Callable
from workload import WorkLoad
from enum import Enum
from data_center import ExecResult, data_center
import subprocess
import time


class ExecStatus(Enum):
    """
    执行状态
    """
    WAITTING = 0
    EXECUTING = 1
    COMPLETED = 2
    EROOR = 3
    CANCELED = 4

class Executor(object):
    """
    执行器
    """

    def local_process(self, work_load: WorkLoad):
        cmd = f'{data_center.workspace}/{data_center.simulator} ' \
              f'--exec_file={work_load.exec_file} --sim_tick={work_load.cycles} ' \
              f'--output_path={data_center.logpath}/{work_load.exec_file}_log/'
        
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        start_time = time.time()
        while True:
            result = process.poll()
            if result is not None:
                self.exec_status = ExecStatus.COMPLETED
                end_time = time.time()
                break
            time.sleep(0.1)

        cost_time = end_time - start_time
        exec_result = ExecResult(process.stdout.read(),
                                 process.stderr.read(),
                                 process.communicate()[0],
                                 cost_time)
        data_center.set_exec_result(work_load.exec_file, exec_result)
        print(exec_result)

        

    def remote_process(self, work_load: WorkLoad):
        pass

    exec_func: Dict[WorkMode, Callable] = {
        WorkMode.LOCAL: lambda self: self.local_process,
        WorkMode.REMOTE: lambda self: self.remote_process
    }
    work_mode: WorkMode
    exec_status: ExecStatus = ExecStatus.WAITTING
    exec_result: ExecResult = None

    def __init__(self, work_mode: WorkMode):
        self.work_mode = work_mode

    def execute(self, work_load: WorkLoad):
        """
        执行
        :param mode:
        :return:
        """
        if not isinstance(work_load, WorkLoad):
            raise TypeError("work_load must be WorkLoad")
        self.exec_func[self.work_mode](work_load)
        self.exec_status = ExecStatus.EXECUTING

