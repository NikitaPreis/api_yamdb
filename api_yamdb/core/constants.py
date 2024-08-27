MIN_SCORE = 1
MAX_SCORE = 10
MAX_LENGTH_NAME_FIELD = 256
MESSAGE_VALIDATION_YEAR_ERROR = 'Проверьте год выпуска'
RATING_DEFAULT_VALUE = 0
ADMIN = 'admin'
MODERATOR = 'moderator'
USER = 'user'
USER_ROLES_CHOICES = (
    (USER, 'пользователь'),
    (MODERATOR, 'модератор'),
    (ADMIN, 'администратор'),
)
EMAIL_MAX_LENGTH = 254
USERNAME_MAX_LENGTH = 150
ROLE_MAX_LENGTH = max(len(role[0]) for role in USER_ROLES_CHOICES)
OBJECTS_PER_PAGE = 20
CSV_FILE_PATH = 'static/data/'
EMPTY_DICT_IN_DEFAULT_VALUES = {}
SUCCESSFULL_IMPORT = 'Успешный импорт из файла '
SUCCESSFULL_IMPORT_FINISH = 'Импорт завершен!'
