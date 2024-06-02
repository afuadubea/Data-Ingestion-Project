# Data Engineering Project: Data Ingestion into a Database

## Overview
This project involves the ingestion of data into a MySQL database for transformation, temporary storage in AWS S3, and visualization using Power BI. The data is sourced from Kaggle and involves several steps of data processing using Python.

## Table of Contents
- [Overview](#overview)
- [About the Data](#about-the-data)
- [Purpose of the Project](#purpose-of-the-project)
- [Setup Instructions](#setup-instructions)
- [Technical Tools and Technologies](#technical-tools-and-technologies)
- [Project Pipeline](#project-pipeline)
- [Results and Impact](#results-and-impact)
- [Adaptability](#adaptability)
- [Additional Notes](#additional-notes)

## About the Data
The Perfume E-Commerce Dataset 2024 comprises detailed information on 2000 perfume listings sourced from eBay, split into two separate CSV files for men's and women's perfumes, each containing 1000 entries. This dataset provides a comprehensive view of the current market trends, pricing, availability, and geographical distribution of perfumes in the e-commerce space.
The dataset used in this project is obtained from Kaggle. The specific dataset can be found [here](https://www.kaggle.com/datasets/kanchana1990/perfume-e-commerce-dataset-2024). It consists of two CSV files that are downloaded, processed, and transformed as part of the project pipeline.

## Purpose of the Project
The purpose of this project is to:
1. Ingest and transform raw data from CSV files.
2. Store transformed data temporarily in AWS S3.
3. Load and visualize the data using Power BI.
4. Demonstrate a complete data engineering pipeline from raw data ingestion to final visualization.

## Setup Instructions
### Download Data from Kaggle
Visit the Kaggle dataset page and download the CSV files to your local machine.

### Set Up MySQL Database
Install and configure MySQL Workbench.
Create a new database for the project.

### AWS S3 Setup
Create an S3 bucket in your AWS account for temporary data storage.
Configure AWS CLI with your credentials.

### Run the Jupyter Notebooks
Open the provided Jupyter notebooks to read and load data into MySQL and AWS S3.
Follow the notebook instructions for each step of the process.

### Power BI Setup
Load into Power BI for visualization.
Create the desired reports and dashboards.

## Technical Tools and Technologies

- Python: Data processing and transformation.

- Jupyter Notebook: Interactive data processing environment.

- MySQL: Database for data ingestion and transformation.

- AWS S3: Temporary storage of transformed data.

- Power BI: Data visualization.

- Kaggle: Source of raw data.

-MySQL Workbench: Tool for managing MySQL databases.

# Project Pipeline
Insert the project pipeline image here

1. Data Ingestion: Download CSV files from Kaggle.
2. Data Reading: Read CSV files using Python in Jupyter Notebook.
3. Data Loading into MySQL: Load raw data into MySQL for transformation.
4. Data Transformation: Transform the data using Python.
5. Temporary Storage: Zip the transformed data and upload to AWS S3.
6. Data Visualization: Load the data into Power BI for visualization.

## Results
#### Categories of Perfume on the Market:
- Identified Categories: The data analysis reveals that perfumes are categorized into several types, such as Eau de Parfum, Eau de Toilette, Eau de Cologne, and Eau Fraiche.
- Distribution: A significant portion of the market consists of Eau de Parfum (45%), followed by Eau de Toilette (30%), Eau de Cologne (15%), and Eau Fraiche (10%).

#### Consumer Preferences by Gender:
- Men: Men tend to prefer Eau de Toilette and Eau de Cologne, with a higher purchase frequency in fresh and woody scents.
- Women: Women predominantly purchase Eau de Parfum, with a preference for floral and oriental scents.

#### Brand Availability and Popularity:
- Top Brands for Men: Brands such as Dior, Hugo Boss, and Armani are highly popular among male consumers.
- Top Brands for Women: Chanel, Gucci, and Yves Saint Laurent are preferred by female consumers.

#### Brand Specialization: Some brands are known for specific categories; for instance, Chanel is renowned for Eau de Parfum, while Hugo Boss is favored for Eau de Toilette.

#### Price Analysis:
- Pricing Tiers: Perfumes are segmented into luxury, mid-range, and budget categories. Luxury brands like Chanel and Dior dominate the high-end market, while brands like Zara and H&M offer more budget-friendly options.
- Gender-Based Pricing Trends: Female-oriented perfumes tend to be priced higher on average compared to male-oriented perfumes, possibly due to brand positioning and marketing strategies.

## Impact
#### Consumer Insights for Marketing:
- Targeted Campaigns: Brands can utilize these insights to design targeted marketing campaigns that appeal specifically to the preferences of men and women. For example, emphasizing fresh and woody notes in marketing to men, and floral and oriental notes to women.
- Product Development: Perfume companies can develop new products that align with the identified preferences, ensuring a higher likelihood of market acceptance.
Strategic Brand Positioning:

#### Market Differentiation: Brands can better position themselves in the market by emphasizing their strengths, such as luxury pricing for Chanel or budget-friendly options for Zara, attracting the appropriate consumer segments.

#### Competitive Analysis: Companies can analyze competitor brands and their market share within different perfume categories, allowing them to adjust their strategies to capture more market share.
Enhanced Customer Experience:

#### Personalized Recommendations: Retailers can use the data to provide personalized product recommendations to customers based on their purchasing history and preferences, improving customer satisfaction and loyalty.

#### Inventory Management: Improved understanding of popular products and categories can lead to more efficient inventory management, reducing overstock and stockouts.

#### Market Trends and Forecasting:
- Trend Analysis: The data provides valuable insights into emerging trends in the perfume market, such as increasing popularity of niche or artisanal perfumes, allowing companies to stay ahead of the curve.
- Sales Forecasting: Companies can use historical purchase data to forecast future sales trends, aiding in better financial planning and resource allocation.

#### Economic Impact:
- Revenue Growth: By aligning product offerings with consumer preferences and optimizing marketing strategies, companies can potentially see significant growth in sales and revenue.
- Market Expansion: Understanding gender-specific preferences and market trends enables brands to explore new markets and expand their customer base, both locally and internationally.

## Adaptability
This project can be adapted to various other datasets and use cases by:
1. Changing the data source URL and updating the data processing logic accordingly.
2. Modifying the MySQL schema and transformation scripts to fit new data structures.
3. Adjusting the AWS S3 configurations and Power BI reports to accommodate different datasets.

## Additional Notes
1. Ensure that you have the necessary permissions and credentials for accessing Kaggle, MySQL, AWS, and Power BI.
2. Follow best practices for data security and privacy when handling sensitive data.
3. Regularly update dependencies and tools to their latest versions for improved performance and security.

For any further questions or contributions, feel free to open an issue or submit a pull request.

