# Dependencies 
import pandas as pd

# Set path for csv
csv_path = "election_data_1.csv"

# Read the CSV
poll_data = pd.read_csv(csv_path)
poll_data.head()

# Put data into data frame
poll_df = poll_data[["Voter ID", "County", "Candidate"]]

# count total votes
total_votes = poll_df['Voter ID'].count()
total_votes

# List candidates who received votes and total amount of votes
poll_test = poll_df
candidates = poll_test.groupby('Candidate')
count_candidate = candidates['Candidate'].count()
count_candidate

# Percentage of votes for each candidate
percent_of_votes = (count_candidate/total_votes)*100
percent_of_votes

# Winner of the election
#This doesnt work
#count_candidate['Candidate'].max()

# Generate Output Summary
# NEED TO FIX
output = (
    f"Election Results\n"
    f"-----------------\n"
    f"Total Votes: {total_votes}\n"
    f"-----------------\n"
    #print(dataframe)
    f"-----------------\n"
    f"Winner: {winner}\n")

# Print output
print(output)

# Export to txt
data_file_output = "data_output.txt"
with open(data_file_output, "w") as txt_file:
    txt_file.write(output)

