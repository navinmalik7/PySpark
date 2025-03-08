# Database Configuration File (db_config.py)
from db_credentials import DATABASE_CREDENTIALS
DATABASE_CONFIG = {
    "url": "jdbc:sqlserver://localhost:1434;databaseName=SparkDatabase;trustServerCertificate=true",
    "user": DATABASE_CREDENTIALS["user"],
    "password": DATABASE_CREDENTIALS["password"],
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver",
    "jar_path": "C:/HADOOP_HOME/bin/jars/mssql-jdbc-12.8.1.jre11.jar"  # Update this path
}