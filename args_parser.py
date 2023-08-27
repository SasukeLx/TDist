import argparse
import os

def get_case_files(case_dir):
    return [f for f in os.listdir(case_dir) if os.path.isfile(os.path.join(case_dir, f))]

def parse_args():
    parser = argparse.ArgumentParser(description="Test Task Scheduler")
    parser.add_argument("-t", "--tasks", type=int, default=1, help="Number of tasks to execute in parallel")
    parser.add_argument("-l", "--log-path", type=str, default="./logs", help="Path to store log files")
    parser.add_argument("-c", "--case-dir", type=str, default="./", help="Directory containing test cases")
    parser.add_argument("-x", "--case-xml", type=str, default="testcase.xml", help="Xml file describe test cases")
    parser.add_argument("-p", "--cpu", type=int, default=1, help="Number of CPU cores available")
    parser.add_argument("-m", "--mem", type=int, default=1024, help="Memory size available")

    return parser.parse_args()

if __name__ == "__main__":
    parse_args()
