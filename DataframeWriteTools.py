from crewai_tools import BaseTool
import pandas as pd

# Tool for writing DataFrame to CSV file
class CSVWriteTool(BaseTool):
    name = "CSVWriteTool"
    description = "Writes pandas DataFrame to a CSV file."

    def _run(self, dataframe, file_path):
        dataframe.to_csv(file_path, index=False)
        return f"DataFrame written successfully to {file_path} as CSV."

# Tool for writing DataFrame to Excel file
class ExcelWriteTool(BaseTool):
    name = "ExcelWriteTool"
    description = "Writes pandas DataFrame to an Excel file."

    def _run(self, dataframe, file_path):
        dataframe.to_excel(file_path, index=False)
        return f"DataFrame written successfully to {file_path} as Excel."

# Tool for writing DataFrame to JSON file
class JSONWriteTool(BaseTool):
    name = "JSONWriteTool"
    description = "Writes pandas DataFrame to a JSON file."

    def _run(self, dataframe, file_path):
        dataframe.to_json(file_path, orient='records')
        return f"DataFrame written successfully to {file_path} as JSON."

# Example DataFrame for testing
data = {'Name': ['Sash', 'Gupta'], 'Age': [28, 31]}
df = pd.DataFrame(data)

# Example
csv_tool = CSVWriteTool()
excel_tool = ExcelWriteTool()
json_tool = JSONWriteTool()

csv_tool.run(df, 'output.csv')
excel_tool.run(df, 'output.xlsx')
json_tool.run(df, 'output.json')