from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
import sys

#Runs over/under model
def predictSpread(t1, t2):

    # load model
    model = load_model('spread.h5')

    # create offense/defense dictionaries of current team stats
    offense_dict = {}
    offense_dict['Wizards'] = [.478, .737, .389, 27.3, 42.8]
    offense_dict['Warriors'] = [.448, .78, .353, 26.1, 43.9]
    offense_dict['Raptors'] = [.441, .81, .369, 24.8, 43.2]
    offense_dict['Celtics'] = [.468, .739, .366, 22.6, 45]
    offense_dict['Bulls'] = [.478, .805, .385, 25.4, 44.8]
    offense_dict['Suns'] = [.468, .815, .361, 26.2, 42.7]
    offense_dict['Pistons'] = [.427, .794, 34.4, 24.4, 42.6]
    offense_dict['Pacers'] = [.476, .741, .356, 26.3, 42]
    offense_dict['Nuggets'] = [.479, .748, .373, 27.3, 44.2]
    offense_dict['Heat'] = [.486, .774, .372, 26.6, 42.4]
    offense_dict['Mavericks'] = [.453, .74, .335, 22.7, 44.8]
    offense_dict['Clippers'] = [.486, .836, .441, 25.1, 42.3]
    offense_dict['Timberwolves'] = [.439, .743, .34, 23.8, 44.5]
    offense_dict['Knicks'] = [.445, .747, .343, 21.5, 46.5]
    offense_dict['Trail Blazers'] = [.438, .81, .374, 21.7, 43.9]
    offense_dict['Hawks'] = [.438, .805, .342, 24.4, 49.8]
    offense_dict['76ers'] = [.474, .766, .36, 25.3, 46.8]
    offense_dict['Kings'] = [.473, .719, .374, 25.1, 42.1]
    offense_dict['Rockets'] = [.46, .743, .351, 22.7, 42.8]
    offense_dict['Hornets'] = [.445, .736, .367, 28.7, 44.8]
    offense_dict['Cavaliers'] = [.449, .667, .359, 24.2, 44.3]
    offense_dict['Nets'] = [.491, .812, .4, 26.3, 46.6]
    offense_dict['Thunder'] = [.446, .719, .33, 22.2, 44.7]
    offense_dict['Bucks'] = [.485, .734, .403, 25.9, 47.6]
    offense_dict['Grizzlies'] = [.452, .765, .333, 27.2, 45.3]
    offense_dict['Lakers'] = [.488, .754, .391, 25.5, 48.6]
    offense_dict['Spurs'] = [.442, .791, .353, 25.1, 46]
    offense_dict['Jazz'] = [.465, .684, .401, 23.3, 49.6]
    offense_dict['Magic'] = [.426, .795, .318, 21.1, 46.5]
    offense_dict['Pelicans'] = [.464, .715, .327, 22.4, 47.5]
    d_df = pd.read_csv('d2021 - Sheet1.csv')
    defense_dict = d_df.set_index('TEAM').T.to_dict('list')

    # Assembles data in correct order to run through model
    def assembleFeatures(o_dict, d_dict):
        l1 = o_dict[t1]
        l2 = o_dict[t2]
        l3 = d_dict[t1]
        l4 = d_dict[t2]
        l1.extend(l2)
        l3.extend(l4)
        l1.extend(l3)
        d_ar = np.array(l1)
        r_ar = pd.DataFrame(d_ar)
        return r_ar.transpose()

    data = assembleFeatures(offense_dict, defense_dict)
    x = model.predict(data)
    return x[0][0]

if __name__ == "__main__":
    teams = sys.argv[1:]
    print(predictSpread(teams[0], teams[1]))