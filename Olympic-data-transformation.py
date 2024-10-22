from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType, DoubleType, BooleanType, DateType

# Azure Storage Account Configurations
configs = {
    "fs.azure.account.auth.type": "OAuth",
    "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
    "fs.azure.account.oauth2.client.id": "f1e9884d-8e97-4940-90e3-2554ee64404d",
    "fs.azure.account.oauth2.client.secret": 'RgI8Q~2fcOZ7CDvpssWXNEeVz46Mjp1jWMlfVaSM',
    "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/tanent_id/oauth2/token"
}

# Mount the Azure Data Lake Storage
dbutils.fs.mount(
    source="abfss://tokyo-olympic-data@tokyoolympicdata.dfs.core.windows.net",  # Container and storage account
    mount_point="/mnt/tokyoolympic",
    extra_configs=configs
)

# Load datasets from the mounted storage
athletes = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/mnt/tokyoolympic/raw-data/athletes.csv")
coaches = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/mnt/tokyoolympic/raw-data/coaches.csv")
entriesgender = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/mnt/tokyoolympic/raw-data/entriesgender.csv")
medals = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/mnt/tokyoolympic/raw-data/medals.csv")
teams = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/mnt/tokyoolympic/raw-data/teams.csv")

# Data Transformation Operations
# 1. Find the top countries with the highest number of gold medals
top_gold_medal_countries = medals.orderBy("Gold", ascending=False).select("Team_Country", "Gold")
top_gold_medal_countries.show()

# 2. Calculate the average number of entries by gender for each discipline
average_entries_by_gender = entriesgender.withColumn(
    'Avg_Female', entriesgender['Female'] / entriesgender['Total']
).withColumn(
    'Avg_Male', entriesgender['Male'] / entriesgender['Total']
)
average_entries_by_gender.show()

# Save the transformed datasets to Azure Data Lake Storage
athletes.repartition(1).write.mode("overwrite").option("header", 'true').csv("/mnt/tokyoolympic/transformed-data/athletes")
coaches.repartition(1).write.mode("overwrite").option("header", "true").csv("/mnt/tokyoolympic/transformed-data/coaches")
entriesgender.repartition(1).write.mode("overwrite").option("header", "true").csv("/mnt/tokyoolympic/transformed-data/entriesgender")
medals.repartition(1).write.mode("overwrite").option("header", "true").csv("/mnt/tokyoolympic/transformed-data/medals")
teams.repartition(1).write.mode("overwrite").option("header", "true").csv("/mnt/tokyoolympic/transformed-data/teams")
