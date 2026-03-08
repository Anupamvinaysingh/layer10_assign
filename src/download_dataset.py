# import os
# import urllib.request
# import tarfile


# DATA_URL = "https://www.cs.cmu.edu/~enron/enron_mail_20150507.tar.gz"
# DATA_DIR = "data"


# def download_dataset():

#     os.makedirs(DATA_DIR, exist_ok=True)

#     file_path = os.path.join(DATA_DIR, "enron.tar.gz")

#     if not os.path.exists(file_path):
#         print("Downloading Enron dataset...")
#         urllib.request.urlretrieve(DATA_URL, file_path)
#         print("Download complete")

#     else:
#         print("Dataset already downloaded")

#     print("Extracting dataset...")

#     with tarfile.open(file_path, "r:gz") as tar:
#         tar.extractall(DATA_DIR)

#     print("Extraction finished")


# if __name__ == "__main__":
#     download_dataset()

import os
import tarfile

DATA_DIR = "data"
TAR_FILE = os.path.join(DATA_DIR, "enron.tar.gz")
EXTRACT_DIR = os.path.join(DATA_DIR, "enron_sample")

MAX_FILES = 500


def download_dataset():

    if not os.path.exists(TAR_FILE):
        print("ERROR: enron.tar.gz not found in data folder")
        return

    os.makedirs(EXTRACT_DIR, exist_ok=True)

    print("Extracting small sample from archive...")

    count = 0

    with tarfile.open(TAR_FILE, "r:gz") as tar:

        for member in tar.getmembers():

            if member.isfile():

                tar.extract(member, EXTRACT_DIR)

                count += 1

                if count >= MAX_FILES:
                    break

    print(f"Extracted {count} email files to {EXTRACT_DIR}")


if __name__ == "__main__":
    download_dataset()