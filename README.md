
## Steps to Convert Weekly Excel file

1. past last week's js object into the past_week.js file
2. run python simple http server by executing this command: python -m SimpleHTTPServer 8000
3. open output.html at http://localhost:8000/output.html
4. copy json, enter into weekly_data.json
5. run the script merge_weekly_data.py, by executing this command: python3 merge_weekly_data.py (outputs weekly_merged_data.json)
6. open output.html at http://localhost:8000/output.html, inspect element on the body tag
7. in the inspector, open the console, right click the object, click store as global variable (outputs variable temp1)
8. write copy(temp1) to copy object to clipboard, hit enter
9. paste object into next_week.js, assign to variable data_states_metrics
