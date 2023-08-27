from typing import Sequence
from dataclasses import dataclass
from enum import Enum


class WorkStatus(Enum):
	IDLE = 0
	SUSPENDED = 1
	RUNNING = 2
	FINISHED = 3
	

class WorkResult(Enum):
	OK = 0
	ERROR = 1

@dataclass
class WorkLoad:
	id: int
	exec_file: str
	cycles: int
	config: str
	description: str

	status: WorkStatus = WorkStatus.IDLE
	result: WorkResult = WorkResult.OK

	def get_status(self) -> WorkStatus:
		return self.status

	def set_status(self, status: WorkStatus):
		self.status = status

	def get_result(self) -> WorkResult:
		return self.result

	def set_result(self, result: WorkResult):
		self.result = result

# Example usage:
work_load = WorkLoad(1, "example.out", 50, "config.json", "This is a test demo")
print(work_load)