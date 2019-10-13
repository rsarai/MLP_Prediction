import pandas as reader

from constants import dataset_path, answers_path


input_csv = reader.read_csv(dataset_path)
result_csv = reader.read_csv(answers_path)
