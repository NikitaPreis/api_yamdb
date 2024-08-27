from pandas import read_csv
from sqlalchemy import create_engine

from core.constants import (CSV_FILE_PATH, EMPTY_DICT_IN_DEFAULT_VALUES,
                            SUCCESSFULL_IMPORT, SUCCESSFULL_IMPORT_FINISH)


import_csv_arguments = {
    'titles_csv': ('titles.csv', 'reviews_titles',
                   {'description': '', }),
    'category_csv': ('category.csv', 'reviews_categories',
                     EMPTY_DICT_IN_DEFAULT_VALUES),
    'genre_csv': ('genre.csv', 'reviews_genres',
                  EMPTY_DICT_IN_DEFAULT_VALUES),
    'genre_title_csv': ('genre_title.csv', 'reviews_titles_genre',
                        EMPTY_DICT_IN_DEFAULT_VALUES),
    'comments_csv': ('comments.csv', 'reviews_comments',
                     EMPTY_DICT_IN_DEFAULT_VALUES),
    'review_csv': ('review.csv', 'reviews_reviews',
                   EMPTY_DICT_IN_DEFAULT_VALUES),
    'users_csv': ('users.csv', 'reviews_users',
                  EMPTY_DICT_IN_DEFAULT_VALUES),
}


def import_csv(engine, csv_file, table_name, default_values={}):
    data = read_csv(csv_file)

    for column, default_value in default_values.items():
        if column not in data.columns:
            data[column] = default_value

    data.to_sql(table_name, engine, if_exists='replace', index=False)


engine = create_engine('sqlite:///db.sqlite3')


for csv_file, table_name, default_values in import_csv_arguments.values():
    import_csv(engine, CSV_FILE_PATH + csv_file, table_name, default_values)
    print(SUCCESSFULL_IMPORT + csv_file)

print(SUCCESSFULL_IMPORT_FINISH)
