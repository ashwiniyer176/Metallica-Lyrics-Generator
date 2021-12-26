# Template Repository for Machine Learning Projects 

 This is the template repository for all Machine Learning based Projects as mentioned by **Abhishek Thakur**, in his book **Appraoching (Almost) Any Machine Learning Problem**. The folder structure is as follows:
<br>

## Structure:

1. data : This folder consists of all the input files and data for your machine learning project. If you are working on NLP projects, you can keep your embeddings here. If you are working on image projects, all images go to a subfolder inside this folder. 


2.  src: We will keep all the python scripts associated with the project here. If I talk about a python script, i.e. any *.py file, it is stored in the src folder. 


3.  models: This folder keeps all the trained models.   


4.  notebooks: All jupyter notebooks (i.e. any *.ipynb file) are stored in the notebooks folder. 


5.  README.md: This is a markdown file where you can describe your project and write instructions on how to train the model or to serve this in a production environment. 


6.  LICENSE: This is a simple text file that consists of a license for the project, such as MIT, Apache, etc. Going into details of the licenses is beyond the scope of this book.
<br>

## Usage:
1. Use the notebook `notebooks/Preprocessing.ipynb` to begin preprocessing
2. Save the dataset after preprocessing as `final_train.csv`
3. Use the notebook `notebooks/EDA.ipynb` for Exploratory Data Analysis and shortlisting models
4. Open `src/config.py`
5. Select a model (sklearn model instance) and a metric (sklearn metric)
6. Configure number of folds required
7. Open Command Prompt and run the `createFoldsAndRun.bat`


Note: The objective for doing this is to build a framework which ensures that running most models becomes simple plug and play, enabling a much faster pace of development and experimentation.

<br>

For the purposes of this repository, I am using [Heart Failure Prediction Dataset](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data), whereas the author uses MNIST in CSV format.