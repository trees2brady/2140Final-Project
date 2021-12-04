from final_project.settings import BASE_DIR
import os

# address of generated Text index file.
IndexTextDir = os.path.join(BASE_DIR, "SearchEngine\\IndexConstruction\\data\\index\\")

# address of stopwords
StopwordDir = "data//stopword.txt"

XMLPath = "data//xml_path.txt"
print(IndexTextDir)