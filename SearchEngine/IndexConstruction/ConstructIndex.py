from Indexing.PreProcessedCorpusReader import PreprocessedCorpusReader
from Indexing.StopWordRemover import StopWordRemover
from Indexing.WordTokenizer import WordTokenizer
from Indexing.WordNormalizer import WordNormalizer
from Indexing.MyIndexWriter import MyIndexWriter


preprocessor = PreprocessedCorpusReader()
document = preprocessor.nextDocument()
stop_word_remover = StopWordRemover()
word_normalizer = WordNormalizer()
index_writer = MyIndexWriter()
cnt = 0

while document is not None:
    fields_list = ["official_title", "breif_summary", "criteia", "detailed_description"]
    result = {"nct_id": document["nct_id"][8:-9]}
    for field in fields_list:
        if document.get(field):
            word_tokenizer = WordTokenizer(document[field])
            tokenized_word = word_tokenizer.nextWord()
            words_list = []
            while tokenized_word is not None and len(tokenized_word) != 0:
                x = stop_word_remover.isStopword(tokenized_word)
                if not stop_word_remover.isStopword(tokenized_word):
                    normalized_word_lowercase = word_normalizer.lowercase(tokenized_word)
                    normalized_word_lowercase_stem = word_normalizer.stem(normalized_word_lowercase)
                    words_list.append(normalized_word_lowercase_stem)
                tokenized_word = word_tokenizer.nextWord()
            result[field] = " ".join(words_list)
        else:
            result[field] = ""
    index_writer.index(result)
    if cnt % 10000 == 0:
        print(cnt)
    cnt += 1
    document = preprocessor.nextDocument()
print(cnt)
index_writer.close()