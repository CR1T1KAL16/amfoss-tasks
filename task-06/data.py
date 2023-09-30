
# import csv
# import datetime
# from scraper import scrape_livescore, scrape_result
# import os

# def append_result_to_csv():
#     try:
#         first = scrape_livescore()
#         result = scrape_result()
#         current_date = datetime.datetime.now()
#         date_string = current_date.strftime('%Y-%m-%d')

#         if not os.path.isfile('cricket_scores.csv'):
#             with open('cricket_scores.csv', 'w', newline='') as csv_file:
#                 csv_writer = csv.writer(csv_file)
#                 csv_writer.writerow(['Date', 'First', 'Result'])

#         with open('cricket_scores.csv', 'a', newline='') as csv_file:
#             csv_writer = csv.writer(csv_file)
#             csv_writer.writerow([date_string, first, result])

#         print("Result appended to the CSV file.")
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")

# if __name__ == "__main__":
#     append_result_to_csv()
#     print("Result appended to the CSV file.")

