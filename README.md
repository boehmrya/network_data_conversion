
## Steps to Convert Weekly Excel file

1. paste last week's js object into the past_week.js file
2. run python simple http server by executing this command: python -m SimpleHTTPServer 8000
3. open output.html at http://localhost:8000/output.html (in chrome incognito)
4. copy json, enter into weekly_data.json
5. move next week's xlsx file into the network_data directory, and rename it next_week.xlsx
6. run the script merge_weekly_data.py, by executing this command: python3 merge_weekly_data.py (outputs weekly_merged_data.json)
7. open output.html at http://localhost:8000/output.html, inspect element on the body tag
8. in the inspector, open the console, right click the object, click store as global variable (outputs variable temp1)
9. write copy(temp1) to copy object to clipboard, hit enter
10. paste object into next_week.js, assign to variable data_states_metrics
