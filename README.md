# Extended Crew AI Tools for Agentic Workflows and Operations
Welcome to the repository of Extended Crew AI Tools designed to enhance agentic workflows and operational capabilities. This suite of tools facilitates seamless integration with existing Crew AI setups and offers robust write-back operations across diverse environments.

Features
This repository includes a series of tools developed to support:

Database Operations: Tools for performing read and write operations with SQL databases like MySQL, PostgreSQL, SQLite, and NoSQL databases such as MongoDB and Redis.
Document Management: Tools for generating and writing content into PDF, DOCX, and HTML formats.
Data Handling: Tools for creating and manipulating CSV, Excel, and JSON files, ideal for data export, sharing, and archival purposes.
Installation
To install the tools in this repository, clone the repository and set up the environment using the following commands:

bash
Copy code
git clone https://github.com/yourusername/extended-crewai-tools.git
cd extended-crewai-tools
pip install -r requirements.txt
Usage
Each tool in this repository is designed to be used independently within your existing Crew AI projects. Below are brief examples on how to use these tools:

Database Tools
python
Copy code
from tools.sql_tool import SQLDatabaseWriteTool

# Initialize the tool with a database URL
db_tool = SQLDatabaseWriteTool('sqlite:///mydatabase.db')

# Write data to the database
db_tool.run('my_table', {'column1': 'data1', 'column2': 'data2'})
Document Tools
python
Copy code
from tools.docx_tool import DOCXWriteTool

# Initialize the tool
docx_tool = DOCXWriteTool()

# Write text to a DOCX file
docx_tool.run('output.docx', 'Hello World!')
Data Handling Tools
python
Copy code
from tools.csv_tool import CSVWriteTool
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})

# Initialize the tool
csv_tool = CSVWriteTool()

# Write DataFrame to a CSV file
csv_tool.run(df, 'output.csv')
Contributing
We welcome contributions from the community, whether it's adding new tools, improving existing ones, or fixing bugs. Please follow the contribution guidelines for more information on how to get involved.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Acknowledgments
Thanks to the Crew AI team for providing the framework.
All contributors who have helped extend and improve these tools.
