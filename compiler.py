import os
import subprocess
from xml.etree.ElementTree import Element, SubElement, tostring

def create_test_suite_element(tests):
  suite_element = Element("test_suite")
  for test_case in tests:
      suite_element.append(create_test_case_element(test_case))
  return suite_element

def create_test_case_element(test_case):
  case_element = Element("test_case")
  exec_file_element = SubElement(case_element, "exec_file")
  exec_file_element.text = test_case.exec_file
  cycles_element = SubElement(case_element, "cycles")
  cycles_element.text = str(test_case.cycles)
  description_element = SubElement(case_element, "description")
  description_element.text = test_case.description
  expected_result_element = SubElement(case_element, "expected_result")
  expected_result_element.text = test_case.expected_result
  return case_element

def compile_cpp_files(src_dir, build_dir, xml_file):
  cpp_files = [f for f in os.listdir(src_dir) if f.endswith(".cpp")]
  for cpp_file in cpp_files:
      exec_file = cpp_file.replace(".cpp", "")
      cmd = f"g++ -o {build_dir}/{exec_file} {src_dir}/{cpp_file}"
      subprocess.run(cmd, shell=True, check=True)
    #   test_case = TestTask(exec_file, 10, f"Compile {cpp_file}", "Success")
    #   tests.append(test_case)
  suite_element = create_test_suite_element(tests)
  # tree = ElementTree.ElementTree(suite_element)
  # tree.write(xml_file, encoding="unicode")

if __name__ == "__main__":
  src_dir = "./src"
  build_dir = "./build"
  xml_file = "compile_test_case_config.xml"
  tests = []
  compile_cpp_files(src_dir, build_dir, xml_file)
  print(f"Compiled {len(tests)} cpp files and created {xml_file}")