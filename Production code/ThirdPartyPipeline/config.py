
# data
TRAINING_DATA_FILE = r"C:\Users\shrikanth\Desktop\Course - Deploying Machine Learning Model\Demo Notebooks\Dataset\houseprice.csv"
PIPELINE_NAME = r'C:\Users\shrikanth\Desktop\Course - Deploying Machine Learning Model\Demo Notebooks\Model files\Scikit-Learn Pipeline\lasso_regression'

TARGET = 'SalePrice'

# input variables
FEATURES = ['MSSubClass', 'MSZoning', 'Neighborhood',
            'OverallQual', 'OverallCond', 'YearRemodAdd',
            'RoofStyle', 'MasVnrType', 'BsmtQual',
            'BsmtExposure', 'GrLivArea', 'FireplaceQu',
            'HeatingQC', 'CentralAir', '1stFlrSF',
            'BsmtFullBath', 'KitchenQual', 'Fireplaces',
            'GarageType', 'GarageFinish', 'GarageCars',
            'PavedDrive', 'LotFrontage', 'YrSold']

# this variable is to calculate the temporal variable,
# must be dropped afterwards
DROP_FEATURES = 'YrSold'

# numerical variables with NA in train set
NUMERICAL_VARS_WITH_NA = ['LotFrontage']

# categorical variables with NA in train set
CATEGORICAL_VARS_WITH_NA = ['MasVnrType', 'BsmtQual', 'BsmtExposure',
                            'FireplaceQu', 'GarageType', 'GarageFinish']

TEMPORAL_VARS = 'YearRemodAdd'

# variables to log transform
NUMERICALS_LOG_VARS = ['LotFrontage', '1stFlrSF', 'GrLivArea']

# categorical variables to encode
CATEGORICAL_VARS = ['MSZoning', 'Neighborhood', 'RoofStyle', 'MasVnrType',
                    'BsmtQual', 'BsmtExposure', 'HeatingQC', 'CentralAir',
                    'KitchenQual', 'FireplaceQu', 'GarageType', 'GarageFinish',
                    'PavedDrive']
