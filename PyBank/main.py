# Set dependencies
import pandas as pd

# Set path for csv
csv_path = "budget_data_1.csv"

# Read the CSV
bank_data = pd.read_csv(csv_path)
bank_data.head()

# Put data into data frame
bank_df = bank_data[["Date", "Revenue"]]

# Count months
months_df = bank_df.groupby('Date')
count = months_df['Date'].count().sum()

# change in monthly rev
bank_df['difference'] = bank_df['Revenue'].diff()

# Total amount of revenue gained
total = bank_df['Revenue'].sum()
total

# average change each month
average = (bank_df['Revenue'].sum())/41
average

# Greatest increase
increase = bank_df['difference'].max()
increase

# Greatest decrease
decrease = bank_df['difference'].min()
decrease

# Generate Output Summary
output = (
    f"Financial Analysis\n"
    f"-----------------\n"
    f"Total Months: {count}\n"
    f"Total Revenue: ${total}\n"
    f"Average Revenue Change: ${average}\n"
    f"Greatest Increase in Revenue: (${increase})\n"
    f"Greatest Decrease in Revenue: (${decrease})\n")

# Print output
print(output)

# Export to txt
data_file_output = "data_output.txt"
with open(data_file_output, "w") as txt_file:
    txt_file.write(output)


