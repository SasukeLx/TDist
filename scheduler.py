from dataclasses import dataclass
import concurrent.futures
import time
from workload import WorkLoad


@dataclass
class Resource:
	cpu: int
	memory: int

@dataclass
class TaskScheduler:
	tasks: list
	resources: Resource
	max_parallelism: int

	def distribute_tasks(self):
		with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_parallelism) as executor:
			futures = []
			for task in self.tasks:
				future = executor.submit(self.execute_task, task)
				futures.append(future)
			concurrent.futures.wait(futures)

	def execute_task(self, task):
		print(f"Executing task{task.id} {task.exec_file} for {task.cycles} cycles.\n")
		time.sleep(task.cycles)
		print(f"Task{task.id} completed.\n")

