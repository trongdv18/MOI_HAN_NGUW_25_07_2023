# import the necessary packages
import os

# BASE_PATH chưa các folder train , test, val, trong mỗi folder đó lại có các folder tên class
BASE_PATH = "dataset"
# define the names of the training, testing, and validation
# directories
TRAIN = "train"
TEST = "val"
VAL = "test"
# initialize the list of class label names
CLASSES = ["good", "ng"]
# set the batch size
BATCH_SIZE = 32
BASE_CSV_PATH = "output"
if not os.path.exists(BASE_CSV_PATH):
    os.mkdir(BASE_CSV_PATH)
# initialize the label encoder file path and the output directory to
# where the extracted features (in CSV file format) will be stored
LE_PATH = os.path.join(BASE_CSV_PATH, "le.cpickle")

# set the path to the serialized model after training
MODEL_PATH = os.path.join(BASE_CSV_PATH, "model.cpickle")