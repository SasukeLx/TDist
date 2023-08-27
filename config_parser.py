import xml.etree.ElementTree as ET
import os
from workload import WorkLoad

def parse_config(config_file):
	tests = []
	tree = ET.parse(config_file)
	root = tree.getroot()
	for test_case_element in root.findall("testcase"):
		name = test_case_element.find("name").text # type: ignore
		id = int(test_case_element.find("id").text) # type: ignore
		cycles = int(test_case_element.find("cycles").text) # type: ignore
		desc = test_case_element.find("desc").text # type: ignore
		config = test_case_element.find("config").text # type: ignore
		expect = test_case_element.find('expect').text # type: ignore
		test = WorkLoad(id, name, cycles, desc, config, expect) # type: ignore
		tests.append(test)
	return tests

def main():
	config_file = "./testcase/testcase.xml"
	tests = parse_config(config_file)

if __name__ == "__main__":
	main()