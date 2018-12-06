import json
import csv

def get_contents(contents, columns):
    return map(lambda x: unicode(contents[x]).encode('utf-8'), columns)

# Get users with more than 20 reviews
users_over_20 = set()

user_columns = ['user_id', 'name', 'review_count']
with open('users_over_20.csv', 'wB+') as fout:
    csv_file = csv.writer(fout)
    csv_file.writerow(user_columns)
    with open('yelp_academic_dataset_user.json', 'rB') as fin:
        for line in fin:
            contents = json.loads(line)
            if contents['review_count'] >= 20:
                users_over_20.add(contents['user_id'])
                csv_file.writerow(get_contents(contents, user_columns))

# Get business names and categories
business_columns = ['business_id', 'name', 'latitude', 'longitude', 'attributes', 'categories']
with open('businesses.csv', 'wB+') as fout:
    csv_file = csv.writer(fout)
    csv_file.writerow(business_columns)
    with open('yelp_academic_dataset_business.json', 'rB') as fin:
        for line in fin:
            contents = json.loads(line)
            csv_file.writerow(unicode_to_utf8(get_contents(contents, business_columns)))

# Get reviews for relevant users
review_columns = ['user_id', 'business_id', 'stars']
with open('reviews.csv', 'wB+') as fout:
    csv_file = csv.writer(fout)
    csv_file.writerow(review_columns)
    with open('yelp_academic_dataset_review.json', 'rB') as fin:
        for line in fin:
            contents = json.loads(line)
            if contents['user_id'] in users_over_20:
                csv_file.writerow(get_contents(contents, review_columns))

