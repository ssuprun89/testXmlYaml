import argparse
import datetime
import json
import os

from parser import ParserXML, ParserYAML

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Please provide an input files")
    parser.add_argument(
        "--xmls", type=str, help="Input paths of xml example: xml1.xml,xml2.xml"
    )
    parser.add_argument(
        "--yamls", type=str, help="Input paths of yaml example: yaml1.yaml,yaml2.yaml"
    )
    parser.add_argument("--output", help="Write output to console", action="store_true")
    args = parser.parse_args()
    print(f"You provide next xml files: {args.xmls}")
    print(f"You provide next yaml files: {args.yamls}")
    response = []
    if args.xmls:
        for file_path in args.xmls.split(","):
            file_path = f"/data/{file_path}"
            response.append(ParserXML(file_path).parse_file())
    if args.yamls:
        for file_path in args.yamls.split(","):
            file_path = f"/data/{file_path}"
            response.append(ParserYAML(file_path).parse_file())

    name_of_file = f"{int(datetime.datetime.utcnow().timestamp())}.json"
    with open(f"/data/{name_of_file}", "w") as f:
        f.write(json.dumps(response))

    print(f"Saved file: {name_of_file}")

    if args.output:
        print("Result:")
        print(json.dumps(response))
