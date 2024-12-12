![logonew](https://github.com/Dharyaj11/Ethify/assets/119648064/e5ed3776-a2ef-4c05-beea-bca22971feb1)

# Ethify
“Revolutionizing E-Commerce transparency through the use of Advanced ML-powered 
Dark patterns detecting models” 
# Deployed Link 
https://dharyaj11.github.io/ethify_landing_page/

This is our project for the 2024 DPBH Hackathon 

Team Name "DESI BOYS"
- Aaditya Sharma
- Dharya Jasuja
- Dheerain Thakur
- Darren Chahal


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


  - When a user clicks the "ANALYZE SITE" button in the popup, the popup.js script sends a message to the scrape.js to initiate the analysis.
  - The content script then scrapes the DOM elements on the current web page, filters and sends relevant text data to the Flask API endpoint (api/app.py) using a POST request.
  - The Flask API processes the input using machine learning models and returns the classification results.
  - The content script receives the results, highlights elements with dark patterns, and updates the dark pattern count.
  - The updated count is then sent back to the popup script, which updates the displayed count in the extension popup.


### Project file structure
  ![project_structure_updated](https://github.com/Dharyaj11/Ethify/assets/119648064/646cfb67-34ec-4782-b701-5c83a10f6a56)
  

## working

<img width="957" alt="Screenshot 2024-12-12 191508" src="https://github.com/user-attachments/assets/ea6d89d4-d716-464b-a0c0-2ef0f16e861d" />


### Training and Classification
Various ML models were tested, and Bernoulli Naive Bayes was chosen for its simplicity and high accuracy (96.86%). Comparison with deep learning models was conducted, opting for simplicity due to comparable accuracy.

### Dataset and Resources
Merged data from two primary sources: a research paper [Dark Patterns at Scale](https://arxiv.org/pdf/1907.07032.pdf) and a GitHub dataset [ec-darkpattern](https://github.com/yamanalab/ec-darkpattern/blob/master/dataset/dataset.tsv).



### Cookies Model
- GitHub repo- https://github.com/Dharyaj11/Ethify_cookie_feature

A web scraper fetches text data of cookies using BeautifulSoup(). NLP is applied to classify cookie popups as dark patterns. Decision Tree or Random Forest is used based on accuracy. The algorithm uses columns 5, 11, and 14, giving more weight to 5 and 11.

## Results

- Accuracy: Bernoulli Naive Bayes model achieved the highest accuracy of 96.86% among tested models.
- Browser Compatibility: Compatible with leading browsers: Mozilla Firefox, Chrome, Brave, Microsoft Edge. Integration with Safari is part of future development.
- Data Privacy: Ethify prioritizes client security, scraping HTML code without collecting or storing user data. It uses ML models to detect and highlight dark patterns without accessing or retaining user information.
- Scalability: The ML model performed well on a dataset of 2000 rows. Parallel execution on the backend ensures efficiency and speed. Future optimization strategies aim to enhance scalability.
