import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

#Read in data, create spread column
data = pd.read_csv('Final_Thesis_DF.csv')
data['TOTAL'] = data.PTS_home + data.PTS_away
data = data.drop(['PTS_home', 'PTS_away', 'SEASON'], axis = 1)

#Perform 80-20 train/test split
y = data['TOTAL'].values
scaled_dataframe = data.drop(['TOTAL'], axis = 1).values
x_train, x_test, y_train, y_test = train_test_split(scaled_dataframe, y, train_size = 0.8)

#Define neural network
over_under_model = keras.Sequential()
over_under_model.add(layers.Dense(50, input_dim=28, activation='relu'))
over_under_model.add(layers.Dense(100, activation='relu'))
over_under_model.add(layers.Dense(50, activation='relu'))
over_under_model.add(layers.Dense(1, activation='linear'))
over_under_model.compile(loss='mean_squared_error', optimizer='adam')

#Train neural network
over_under_model.fit(
    x_train,
    y_train,
    epochs=50,
    shuffle=True,
    verbose=2
)

#Run testing set
test_error_rate = over_under_model.evaluate(x_test, y_test, verbose=0)
predictions = over_under_model.predict(x_test)

df = pd.DataFrame()
df['Real'] = y_test
df['Predicted'] = predictions
print(df)
print('Test MSE: ', test_error_rate)

#Save model
#over_under_model.save('over_under.h5', save_format='h5')