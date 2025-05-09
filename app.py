from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

# Load survey data from the uploaded CSV file
def load_csv_data(file_path):
    with open(file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]
    return data

# Load data at startup from the uploaded file path
survey_data = load_csv_data('survey_results.csv') # may need to specify the correct path

# Route to display all responses
@app.route('/')
def all_responses():
    return jsonify(survey_data)

# Route to get a specific response by row number (0-indexed)
@app.route('/response/<int:response_id>')
def get_response(response_id):
    if 0 <= response_id < len(survey_data):
        return jsonify(survey_data[response_id])
    else:
        return jsonify({"error": "Response ID out of range"}), 404

# Route to display the count of responses by "Current status"
@app.route('/status_counts')
def status_counts():
    # Count occurrences of each unique value in the "Current status" column
    status_counts = Counter(row['Current status'] for row in survey_data if 'Current status' in row)
    return jsonify(status_counts)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5555)