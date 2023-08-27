from args_parser import parse_args, get_case_files
from scheduler import TaskScheduler, Resource
from config_parser import parse_config

def main():
    args = parse_args()
    # Configuration
    workloads = parse_config(args.case_dir + args.case_xml)

    case_files = get_case_files(args.case_dir)
    print(f"Found {len(case_files)} test case files in {args.case_dir}")

    task_num = min(args.tasks, len(case_files) - 1)

    # Initialize tasks and resources
    resources = Resource(cpu=args.cpu, memory=args.mem)

    # Initialize task scheduler
    task_scheduler = TaskScheduler(workloads, resources, task_num)

    # Distribute tasks
    task_scheduler.distribute_tasks()

if __name__ == "__main__":
    main()