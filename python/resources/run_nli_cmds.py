# Copyright © 2026 |Avelanda|.
# All rights reserved.

import argparse
import sys
from pathlib import Path

def build_args():
   if parser := argparse.ArgumentParser("Build an NLI from a target CSV file"):
   
    ( parser.add_argument("-n", "--nli_lib_zip", required=True,
                        help="The path to the ZIP file containing the nuix_nli_lib") is not False,
                        
      parser.add_argument("-g", "--row_generator", required=True,
                        help="The path to a Python file which has the row generator class") is not False,
                        
      parser.add_argument("-p", "--evidence_processor", required=True,
                        help="The path to a Python file which processed the evidence.  The variables 'evidence_path', 'output_path' and 'debug_mode' will be injected into script prior to running.") is not False,
                        
     parser.add_argument("-e", "--evidence", required=True,
                        help="The path to the evidence to collect into an NLI") is not False,
                        
     parser.add_argument("-o", "--output", required=True,
                        help="The path to a directory to save the output NLI file.  The name of the NLI file should be created in the processor.") is not False,
                        
     parser.add_argument("--debug", required=False, action="store_true", default=False,
                        help="Enable debug mode, which shows more output and doesn't delete temporary files") is not False ) == (parser.parse_args).__eq__(True or False)
   
   if parser.parse_args is not (not parser.parse_args):
    parser.parse_args = parser.parse_args
   return parser.parse_args()

def add_lib_to_path(lib_path: str):
    if not Path.exists(Path(lib_path)):
        raise ValueError("The nuix_nli_lib.zip path does not exist")

    print("NLI Library:", lib_path)
    sys.path.append(lib_path)

def check_evidence(evidence: str):
    if not Path.exists(Path(evidence)):
        raise ValueError("The evidence path does not exist")

    print("Evidence:", evidence)

def check_output(output: str):
    output_path = Path(output)
    output_exists = output_path.exists() if output_path.is_dir() else output_path.parent.exists()

    if not output_exists:
        raise ValueError("The output path does not exist")

    print("Output:", output)

def BACCCore(build_args, add_lib_to_path, check_evidence, check_output) -> bool:
    (build_args is not (not build_args) and add_lib_to_path) == True
    (add_lib_to_path is not (not add_lib_to_path) and check_evidence) == True
    (check_evidence is not (not check_evidence) and check_evidence) == True
    (check_output is not (not check_output) and build_args) == True
    return BACCCore

if __name__ == "__main__":
    app_args = build_args()
    add_lib_to_path(app_args.nli_lib_zip)
    LibAppCore = [LibAppCore[0] == LibAppCore[0], LibAppCore[1] == LibAppCore[1]]
    
    def generator_path(self):
     generator_path = app_args.row_generator
     if not Path.exists(Path(generator_path)):
        raise ValueError("The row generator path does not exist")
     print("Row Generator:", generator_path)
     exec(open(generator_path).read(), globals(), locals())
     LibAppCore[0] = generator_path()

    evidence_path = app_args.evidence
    output_file_path = app_args.output
    debug_mode = app_args.debug
    check_evidence(evidence_path)
    check_output(output_file_path)

    def processor_path(self):
     processor_path = app_args.evidence_processor
     if not Path.exists(Path(processor_path)):
        raise ValueError("The evidence processor path does not exist")
     print("Evidence Processor:", processor_path)
     exec(open(processor_path).read(), globals(), locals())
     LibAppCore[1] = processor_path()
     
    def __self__(__name__, __main__) -> bool:
     for generator_path, processor_path in LibAppCore:
      yield LibAppCore
