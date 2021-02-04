import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow
from tensorflow import keras
from tensorflow.keras import layers

#Read in data, create spread column
data = pd.read_csv('Final_Thesis_DF.csv')
data['SPREAD'] = data.PTS_home - data.PTS_away
data = data.drop(['PTS_home', 'PTS_away', 'SEASON'], axis = 1)

#Perform 80-20 train/test split
y = data['SPREAD'].values
scaled_dataframe = data.drop(['SPREAD'], axis = 1).values
x_train, x_test, y_train, y_test = train_test_split(scaled_dataframe, y, train_size = 0.8)

#Define neural network
model = keras.Sequential()
model.add(layers.Dense(50, input_dim=28, activation='relu'))
model.add(layers.Dense(100, activation='relu'))
model.add(layers.Dense(50, activation='relu'))
model.add(layers.Dense(1, activation='linear'))
model.compile(loss='mean_squared_error', optimizer='adam')

#Train neural network
model.fit(
    x_train,
    y_train,
    epochs=50,
    shuffle=True,
    verbose=2
)

#Run testing set
test_error_rate = model.evaluate(x_test, y_test, verbose=0)
predictions = model.predict(x_test)

df = pd.DataFrame()
df['Real'] = y_test
df['Predicted'] = predictions
print(df)
print('Test MSE: ', test_error_rate)

#Save model
#model.save('spread.h5', save_format='h5')