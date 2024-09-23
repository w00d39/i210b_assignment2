Description
The script performs the following steps:

Read the CSV File:

Opens the pokemon_data.csv file in read mode.
Reads the contents of the file.
Splits the contents into lines.
Splits each line by commas to create a list of columns.
Extract Header and Indices:

Extracts the header row to find the indices of the attack, defense, and speed columns.
Extract Columns:

Extracts the attack, defense, and speed columns using the indices found in the header.
Converts the extracted values to integers.
Sort Columns:

Sorts the attack, defense, and speed columns in ascending order.

Calculate Mean:
Calculates the mean for attack, defense, and speed.
Rounds the mean values to 2 decimal places.
Prints the mean values.

Calculate Median:
Calculates the median for attack, defense, and speed.
For even-length lists, the median is the average of the two middle values.
For odd-length lists, the median is the middle value.
Prints the median values.

Calculate Range:
Calculates the range for attack, defense, and speed.
The range is the difference between the maximum and minimum values.
Prints the range values.

