### Sarcasm Detection
* Sarcasm Detection is an important part of sentimental analysis as it changes the whole meaning of the sentence.
* This project works only on sentences which are sarcastic by theselves and require no prior context.
* Dataset used was taken from https://www.kaggle.com/rmisra/news-headlines-dataset-for-sarcasm-detection


### Contents of the Repository
* The json file contains the dataset used.
* _model1_85%.h5_ is a pretrained model with 85 percent accuracy.

* _sarcasm_dense.py_ file contains python code for simple dense network that classifies if the text is sarcastic or not. The data was converted into vectors using tf-idf vectorizer.

* _sarcasm_detection.ipynb_ file contains an ipython notebook in which multiple networks were trained using lstms.

* _sarcasm_predictor.py_ file contains code to use the trained model to make predictions.

Citation:
@dataset{dataset,
  author = {Misra, Rishabh},
  year = {2018},
  month = {06},
  pages = {},
  title = {News Category Dataset},
  doi = {10.13140/RG.2.2.20331.18729}
}

@book{book,
  author = {Misra, Rishabh and Grover, Jigyasa},
  year = {2021},
  month = {01},
  pages = {},
  title = {Sculpting Data for ML: The first act of Machine Learning},
  isbn = {978-0-578-83125-1}
}
