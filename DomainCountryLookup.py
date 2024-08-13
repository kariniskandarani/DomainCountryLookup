
import pandas as pd
import pycountry as py

#Read csv file
mock_data_csv = pd.read_csv('/content/MOCK_DATA.csv')

#Convert csv to json file
mock_data_csv.to_json('/content/MOCK_DATA.json.gz', indent = 1, orient='records')

# Read json file
mock_data_json = pd.read_json('/content/MOCK_DATA.json.gz')

#Split the email field into user and domain
split_email = mock_data_json['email'].str.split('@', expand=True)
mock_data_json['user'] = split_email[0]
mock_data_json['domain'] = split_email[1]

# Function to extract the country code from the domain
def get_country_code(domain):
    # Extract the top-level domain (TLD) from the domain
    tld = domain.split('.')[-1]

    # Check if the TLD matches any country code in pycountry
    try:
        country = py.countries.get(alpha_2=tld.upper())
        return country.alpha_2
    except:
        return None

# Apply the function to the 'domain' column and create a new 'country' column
mock_data_json['country'] = mock_data_json['domain'].apply(get_country_code)

#Update the existing json file and add the user, domain and country columns
mock_data_json.to_json('/content/MOCK_DATA.json.gz', orient='records', lines=True, compression='gzip')

mock_data_json
