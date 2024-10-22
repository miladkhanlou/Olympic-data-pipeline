# Olympic Data Analysis & Transformation

This project is an end-to-end data engineering pipeline built using **Azure services** to process Olympic data. The pipeline extracts raw data from a source, transforms it using **Apache Spark** (via Azure Databricks), stores the data in **Azure Data Lake Storage**, and performs analytical queries using **Azure Synapse Analytics**. Finally, the processed data is visualized through a dashboard built in **Power BI**.

## Project Objectives:
1. Extract Olympic data from a source (Kaggle or public repository).
2. Perform data transformations using **Apache Spark** in **Azure Databricks**.
3. Store both raw and transformed data in **Azure Data Lake Storage**.
4. Analyze the data using **Azure Synapse Analytics** and create an interactive dashboard.

## Steps:

### 1. Data Extraction:
- Data is extracted from the source using **Azure Data Factory** and stored in **Azure Data Lake Storage**.

### 2. Data Transformation:
- Data is transformed using **Apache Spark** in **Azure Databricks**. The script handles tasks such as:
  - Identifying top countries with the highest number of gold medals.
  - Calculating gender-based statistics (entries by gender).
- The transformed data is saved back to **Azure Data Lake Storage**.

### 3. Data Analysis:
- Perform data analysis on the transformed data using **Azure Synapse Analytics**, where SQL queries can be run to explore the data.

### 4. Visualization:
- Use **Power BI** or **Tableau** to create interactive dashboards showcasing insights from the Olympic data (e.g., medal counts, gender-based statistics).

## Technologies Used:
- **Azure Data Factory**: For extracting data.
- **Azure Databricks**: For transforming data using Apache Spark.
- **Azure Data Lake Storage**: For storing raw and transformed data.
- **Azure Synapse Analytics**: For querying and analyzing data.
- **Power BI/Tableau**: For creating dashboards.

## How to Run:
1. Set up your **Azure** environment (Azure Data Factory, Databricks, Data Lake Storage).
2. Use the provided `Olympic-data-transformation.py` script in **Azure Databricks** to process the data.
3. Run the SQL scripts in **Azure Synapse Analytics** to perform analytical queries.
4. Create a Power BI dashboard using the transformed data for visualization.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
