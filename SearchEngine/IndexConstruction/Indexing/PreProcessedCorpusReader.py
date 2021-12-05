import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
print(sys.path)
import Classes.Path as Path
import re


class PreprocessedCorpusReader:

    corpus = 0

    def __init__(self):
        self.search_compiler = {"nct_id": re.compile(r"<nct_id>.+</nct_id>"),
                                "official_title": re.compile(r"<official_title>.+</official_title>", re.DOTALL),
                                "breif_summary": re.compile(r"<brief_summary>.+</brief_summary>", re.DOTALL),
                                "criteia": re.compile(r"<criteria>.+</criteria>", re.DOTALL),
                                "detailed_description": re.compile(r"<detailed_description>.+</detailed_description>",
                                                                   re.DOTALL)}
        self.corpus = open(Path.XMLPath, "r")

    def nextDocument(self):

        file_line = self.corpus.readline().strip("\n")
        if file_line is not None and len(file_line) != 0:
            record = self.get_xml_element_re(str(file_line), self.search_compiler)
            if record is not None and len(record) != 0:
                return record
        return None

    def get_xml_element_re(self, file, search_compiler):
        content = ""
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                content += line
        nct_id = re.findall(search_compiler["nct_id"], content)
        official_title = re.findall(search_compiler["official_title"], content)
        breif_summary = re.findall(search_compiler["breif_summary"], content)  # 要提取text
        criteia = re.findall(search_compiler["criteia"], content)
        detailed_description = re.findall(search_compiler["detailed_description"], content)
        result = {}
        if nct_id is not None and nct_id != []:
            result["nct_id"] = nct_id[0]
        if official_title is not None and official_title != []:
            result["official_title"] = official_title[0]
        if breif_summary is not None and breif_summary != []:
            result["breif_summary"] = breif_summary[0].replace("<textblock>\n", "").replace("</textblock>\n", "")
        if criteia is not None and criteia != []:
            result["criteia"] = criteia[0].replace("<textblock>\n", "").replace("</textblock>\n", "")
        if detailed_description is not None and detailed_description != []:
            result["detailed_description"] = detailed_description[0].replace("<textblock>\n", "").replace(
                "</textblock>\n", "")
        return result

    def get_all_files_from_part(self, part_path):
        text_list = []
        for file in os.listdir(part_path):
            # pass hidden files
            if file[0] == ".": 
                continue
            xml_list = os.listdir(os.path.join(part_path, file))
            for xml_file in xml_list:
                text_list.append(os.path.join(part_path, file, xml_file))
        return text_list

    def create_path_file(self, write_filename):  # need to write in the filepath of raw material manually
        part_path1 = r"C:\Users\trees\Downloads\ClinicalTrials.2021-04-27.part1"
        part_path2 = r"C:\Users\trees\Downloads\ClinicalTrials.2021-04-27.part2"
        part_path3 = r"C:\Users\trees\Downloads\ClinicalTrials.2021-04-27.part3"
        part_path4 = r"C:\Users\trees\Downloads\ClinicalTrials.2021-04-27.part4"
        part_path5 = r"C:\Users\trees\Downloads\ClinicalTrials.2021-04-27.part5"
        all_xml_files = self.get_all_files_from_part(part_path1) + self.get_all_files_from_part(part_path2) \
            + self.get_all_files_from_part(part_path3) + self.get_all_files_from_part(part_path4) \
            + self.get_all_files_from_part(part_path5)
        with open(write_filename, "w") as fp:
            for i in all_xml_files:
                fp.write(i + "\n")

if __name__ == "__main__":
    preprocessor = PreprocessedCorpusReader()
    preprocessor.create_path_file(Path.XMLPath)
