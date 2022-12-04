#%%
import pandas as pd
from typing import Type, List, TypeVar

class User:
    
    def __init__(self, uid, pw, acc_lvl=None) -> None:
        self.user_id = uid
        self.password = pw
        self.access_level = acc_lvl

    def __eq__(self, __o: object) -> bool:
        if (self.user_id == __o.user_id) and (self.password == __o.password):
            return True
        else:
            return False


class System:

    def __init__(self) -> None:
        self.user_list = []
        self.database = DataBase()
        self.user_interface = None
    
    def sign_up(self, uid, pw, acc_lvl):
        user = User(uid, pw, acc_lvl)
        self.user_list.append(user)
        return None

    def sign_in(self, uid, pw):
        user = User(uid, pw)
        for exist_user in self.user_list:
            if exist_user == user:
                user.access_level = exist_user.access_level
                print('Successfully Logged In')
                return True
        print('Incorrect User Name or Password')
        return False

        

class DataBase:
    def __init__(self) -> None:
        self.__data_list = {}
    
    def add(self):
        pass

    def delete(self):
        pass



class Data:

    def __init__(self, df: pd.DataFrame = pd.DataFrame()) -> None:
        self.__data = df.copy()
        
        if type(self.__data.DerectionTime_O[0]) == str:
            self.__data.DerectionTime_O = pd.to_datetime(self.__data.DerectionTime_O, format='%d/%m/%Y %H:%M')
            self.__data.DerectionTime_D = pd.to_datetime(self.__data.DerectionTime_D, format='%d/%m/%Y %H:%M')
    
    def sort(self, col_name_list: list, ascending_list: list):
        """sort data

        Args:
            col_name_list (list): column names to sort by
            ascending_list (list): True for ascending and False for descending

        Returns:
            Data
        """
        assert len(col_name_list) == len(ascending_list), 'Length not match for input arguments'
        res = self.__data.sort_values(col_name_list, ascending=ascending_list)
        return Data(res)

    def search(self, filter_dict: dict):

        # f1: list[int]
        f1 = filter_dict.get('VehicleType', None)
        # f2: tuple(datetime1, datetime2)
        f2 = filter_dict.get('DerectionTime_O', None)
        # f3: str
        f3 = filter_dict.get('Gantry_O', None)
        # f4: tuple(datetime1, datetime2)
        f4 = filter_dict.get('DerectionTime_D', None)
        # f5: str
        f5 = filter_dict.get('Gantry_D', None)
        # f6: tuple(int1, int2)
        f6 = filter_dict.get('TripLength', None)
        # f7: list[str]
        f7 = filter_dict.get('TripEnd', None)

        if (f3 is not None) and (f3 not in set(self.__data.Gantry_O)):
            return (0, 'Gantry_O', f3)
        
        if (f5 is not None) and (f5 not in set(self.__data.Gantry_D)):
            return (0, 'Gantry_D', f5)

        res = self.__data.copy()
        if f1 is not None:
            res = res[res.VehicleType.isin(f1)]

        if f3 is not None:
            res = res[res.Gantry_O == f3]
        
        if f5 is not None:
            res = res[res.Gantry_D == f5]

        if f6 is not None:
            res = res[(f6[0] <= res.TripLength) & (res.TripLength <= f6[1])]
        
        if f7 is not None:
            res = res[res.TripEnd.isin(f7)]

        return (1, Data(res))

    def download(self):
        pass

    def head(self, max_row: int = 10):
        return self.__data.head(max_row)
    
    def get(self):
        return self.__data
#%%
df = pd.read_csv('/Users/michael/Documents/Myles/Study/PythonLearning/DataStructureAndAlgorithms/Project/TDCS_M06A_20190830_080000.csv')

d1 = Data(df)
col_name_list = ['VehicleType', 'DerectionTime_O']
ascending_list = [True, False]
d1.sort(col_name_list, ascending_list).head()

filter_dict = {
    'VehicleType': [5, 31], 
    'Gantry_O': '03F3307N',
    'TripLength': (5, 20),
    'TripEnd': ['Y']
}
test = d1.search(filter_dict)[1]
test.get()
# %%
