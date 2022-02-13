from utils.lib import *
from utils.functions import *
from utils.model import *
from utils.connect_mysql import *
import time

# Get statistics of wind turbine sensor readings
statistics = get_statistics()

# Get dataset from turbine
path = 'data/' + turbine + '.csv'
df = pd.read_csv(path)

# Apply min max scaling
df = apply_maxmin(df, features, statistics)

# Get split index to handle missing data ranges
split_index = get_split_index(df)

# Apply split index
X_test, y_test = apply_split_index(df, features, split_index)

# Loading the model and weights
model = load_cnn_model(model_name, version)

# # prediction
# y_hat = model.predict(X_test)
# y_hat = y_hat.reshape(y_hat.shape[0], )
# df_final = pd.DataFrame({'y_hat': y_hat, 'y_test': y_test})
#
# # Evaluation
# df_final['difference'] = df_final['y_hat'] - df_final['y_test']
# df_final["abs_difference"] = abs(df_final['y_hat'] - df_final['y_test'])
# print("Difference " + str(df_final["difference"].mean()))
# print("Absolute difference " + str(df_final["abs_difference"].mean()))
# print("Mean squared error " + str(np.sqrt(mean_squared_error(df_final['y_test'].values, df_final['y_hat'].values))))
#
# # Adding data_time column back
# df_final = add_datetime(df, df_final, split_index)

# Connecting to MySQL DB
db = connect_db()

i = 0
for X_test_i, y_test_i in zip(X_test, y_test):
    X_test1 = np.array(X_test_i)
    X_test1 = X_test1.reshape(1, 144, 4, 1)

    y_hat1 = model.predict(X_test1)
    insert_db(db, str(y_hat1[0][0]), str(y_test_i), str(float(y_hat1[0][0])-float(y_test_i)))
    print(y_hat1[0][0], y_test_i, float(y_hat1[0][0])-float(y_test_i))

    time.sleep(10)
    i += 1
    if i > 5:
        break


