![logo](https://github.com/Dharyaj11/Ethify/assets/119648064/f3f132a8-a116-4eee-8895-4699a6135847)

# Ethify
“Revolutionizing E-Commerce transparency through the use of Advanced ML-powered 
Dark patterns detecting models”


# Ethify Browser Extension
- The solution created is in the form of a browser extension(ethify) with a simple, user friendly and interactive interface 
- Following functionalities are targeted through our extension-
  + Analyzing UI deception: Analyzes all the ui used as a dark patterns on a website
  + Fake urgency and scarcity: Identifies instances when e-commerce sites use fake timers or stock level to create false sense of scarcity 
  + Classification: Is able to identify and categorize the dark patterns into a number of categories and a user is able to use filter for different types of dark patterns
  + Provides total count of identified dark patterns as well as category wise. 
  + User reviews: Is able to scrutinize user reviews for signs of fake content and manipulation
  + Cookie classifier- Classifies cookies as dark patterns and informs the user about them

* Introduction

Dark patterns, manipulative UI designs on websites, exploit human psychology for platform benefit. Ethify is a browser extension addressing this issue. It identifies and classifies dark patterns on e-commerce websites, utilizing machine learning models, with Bernoulli Naive Bayes proving most effective (96.86% accuracy).

## Methodology


  ![Untitled-2024-01-25-2001-font](https://github.com/Dharyaj11/Ethify/assets/119648064/7c81390c-35bd-4ef5-bda2-84881faf3848)


### Project file structure
  ![project_structure_updated](https://github.com/Dharyaj11/Ethify/assets/119648064/646cfb67-34ec-4782-b701-5c83a10f6a56)
  

## working
<img width="900" alt="image_2024-01-30_13-18-26" src="https://github.com/Dharyaj11/Ethify/assets/119648064/ba4bc3d8-1bde-4df4-979d-52552269ee28">

[https://github.com/Dharyaj11/Ethify/assets/119648064/dc04a943-4661-45a4-a17a-8e4469ae8451](https://github.com/Dharyaj11/Ethify/assets/119648064/77c5a127-d201-492b-a5cc-f09cc1a0f7ed)


### Training and Classification
Various ML models were tested, and Bernoulli Naive Bayes was chosen for its simplicity and high accuracy (96.86%). Comparison with deep learning models was conducted, opting for simplicity due to comparable accuracy.

### Dataset and Resources
Merged data from two primary sources: a research paper [Dark Patterns at Scale](https://arxiv.org/pdf/1907.07032.pdf) and a GitHub dataset [ec-darkpattern](https://github.com/yamanalab/ec-darkpattern/blob/master/dataset/dataset.tsv).



### Cookies Model
A web scraper fetches text data of cookies using BeautifulSoup(). NLP is applied to classify cookie popups as dark patterns. Decision Tree or Random Forest is used based on accuracy. The algorithm uses columns 5, 11, and 14, giving more weight to 5 and 11.

## Results

- Accuracy: Bernoulli Naive Bayes model achieved the highest accuracy of 96.86% among tested models.
- Browser Compatibility: Compatible with leading browsers: Mozilla Firefox, Chrome, Brave, Microsoft Edge. Integration with Safari is part of future development.
- Data Privacy: Ethify prioritizes client security, scraping HTML code without collecting or storing user data. It uses ML models to detect and highlight dark patterns without accessing or retaining user information.
- Scalability: The ML model performed well on a dataset of 2000 rows. Parallel execution on the backend ensures efficiency and speed. Future optimization strategies aim to enhance scalability.
