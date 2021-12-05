import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from final_project.settings import BASE_DIR

# address of generated Text index file.
IndexTextDir = os.path.join(BASE_DIR, "SearchEngine", "IndexConstruction", "data", "index")

# address of stopwords
StopwordDir = os.path.join(BASE_DIR, "SearchEngine", "IndexConstruction", "data", "stopword.txt")

XMLPath = os.path.join(BASE_DIR, "SearchEngine", "IndexConstruction", "data", "xml_path.txt")

print(IndexTextDir)
print(StopwordDir)
print(XMLPath)