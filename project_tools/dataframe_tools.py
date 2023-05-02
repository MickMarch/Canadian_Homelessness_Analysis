import pandas as pd
pd.options.mode.chained_assignment = None
import os



class TorontoCrimeDataCleaner:
    def __init__(self, min_year:int, max_year:int, columns_to_keep: list = None):
        """
        This is a class meant to manipulate datasets specifically for crime data from 
        the Toronto Police Service Data Catalogue.

        Pandas is imported at the same time.

        Use .add_dataframe_from_csv() to add dataframes to this class

        Parameters
        --
        min_year: int
            Integer year value of earliest year in filtered range
        
        max_year: int
            Integer year value of latest year in filtered range

        columns_to_keep: list
            List of column names to keep. If none provided, a hardcoded list will be the default.
        """
        
        # Sets range of years, and corrects user error if values are input in the wrong order
        if min_year < max_year: 
            self.min_year = min_year
            self.max_year = max_year
        else:
            print("min_year was larger than max_year. The mistake has been corrected.")
            self.min_year = max_year
            self.max_year = min_year


        # Establishes columns to use for every dataframe entered
        if not columns_to_keep:
            self.columns_to_keep = [
                'OCC_YEAR', 'OCC_MONTH', 'OCC_DAY', 'OCC_DOW',
                'OCC_HOUR', 'PREMISES_TYPE', 'MCI_CATEGORY',
                'HOOD_140', 'NEIGHBOURHOOD_140', 'LONG_WGS84', 'LAT_WGS84'
            ]
        else: 
            self.columns_to_keep = [columns_to_keep]

        # This will store all active dataframes
        self.df_dict = {}

        # This will store all removed dataframes that can be recovered
        self.removed_dict = {}

        # This will store all original file names to be used in mass_export
        self.original_file_name = {}

    def _drop_unneeded(self, df: pd.DataFrame):
        """Internal method to reduce columns down to wanted columns, and to remove rows with nan values"""
        try:
            df = df[self.columns_to_keep]
            df.dropna(inplace=True)
            return df
        except Exception as err:
            print(f"Error in _drop_unneeded(): {err}")

    def _convert_column_types(self, df: pd.DataFrame):
        """Internal method to convert data types"""
        try:
            df[['OCC_YEAR','OCC_DAY','OCC_HOUR']] = df[['OCC_YEAR','OCC_DAY','OCC_HOUR']].astype(int)
            return df
        except Exception as err:
            print(f"Error in _convert_column_types(): {err}")

    def _filter_by_year(self, df: pd.DataFrame):
        """Internal method to filter by year"""
        try:
            df = df[(df['OCC_YEAR'] >= self.min_year) & (df['OCC_YEAR'] <= self.max_year)]
            return df
        except Exception as err:
            print(f"Error in _filter_by_year(): {err}")
    
    def _create_datetime_column(self, df: pd.DataFrame):
        """Internal method to filter by year"""
        try:
            df['OCC_DATE_TIME'] = df['OCC_MONTH'] + " " + df['OCC_DAY'].astype(str) + " " + df['OCC_YEAR'].astype(str) + " " + df['OCC_HOUR'].astype(str) + ":00:00"
            df['OCC_DATE_TIME'] = pd.to_datetime(df['OCC_DATE_TIME'])
            return df
        except Exception as err:
            print(f"Error in _create_datetime_column(): {err}")

    def _clean_dataframe(self, df: pd.DataFrame):
        """Internal method to utilize all preceding cleaning tools"""
        df = self._drop_unneeded(df)
        df = self._convert_column_types(df)
        df = self._filter_by_year(df)
        df = self._create_datetime_column(df)
        return df

    def add_dataframe_from_csv(self, name_of_dataframe: str, path_of_csv: str):
        """
        Add Pandas DataFrame from csv to class and automatically clean the data. The added dataframe
        can be accessed by the using the name_of_dataframe as a dictionary key to the
        class variables `df_dict`. 

        Example: class_variable.df_dict['df1']

        Parameters
        --
        name_of_dataframe: str
            Give a name to the dataframe you want to store

        path_of_csv: str
            Path of CSV file to add as Pandas DataFrame
        """

        # TODO Add catch for already existing dataframes, especially by file name
        try:
            self.df_dict[name_of_dataframe] = self._clean_dataframe(pd.read_csv(path_of_csv))
            self.original_file_name[name_of_dataframe] = os.path.basename(path_of_csv).replace(".csv", "")

        except Exception as err:
            print(f'Error in add_dataframe_from_csv(): {err}')

    def remove_df(self, df_name, permanent:bool=False):
        """
        Deletes dataframe from class. Can be recovered unless permanent argument is True.
        """
        if df_name in self.df_dict:
            if not permanent:
                self.removed_dict[df_name] = self.df_dict[df_name].copy()
                del self.df_dict[df_name]
                print(f'Dataframe "{df_name}" has been removed.')
                print(f'It can be recovered using the .recover_df("{df_name}")')
            else:
                del self.df_dict[df_name]
            
            print(f'Successfully deleted "{df_name}" from Dataframe dictionary')
        
        else:
            print(f'Error: "{df_name}" not found in Dataframe dictionary.')

    def recover_df(self, df_name):
        """
        Recoveres deleted dataframe if it wasn't a permanent deletion
        """
        if df_name in self.removed_dict:
            self.df_dict[df_name] = self.removed_dict[df_name].copy()
            del self.removed_dict[df_name]

            print(f'Successfully recovered "{df_name}"!')
        else:
            print(f'Error: "{df_name}" not able to be recovered.')

    def list_all_dataframes(self, show_recoverable=False):
        """
        Display all dataframes within the class object.
        """
        if (
            len(self.df_dict.keys()) == 0 and not show_recoverable
            ) or (
            len(self.df_dict.keys()) == 0 and len(self.removed_dict.keys()) == 0
            ):
            print("There are no dataframes to display.")

        elif len(self.df_dict.keys()) == 0 and show_recoverable:
            recoverable_df_list = [df for df in self.removed_dict.keys()]
            print("------Active Dataframes------")
            print([])
            print("------Recoverable Dataframes------")
            print(recoverable_df_list)

        elif len(self.df_dict.keys()) > 0 and not show_recoverable:
            active_df_list = [df for df in self.df_dict.keys()]
            print("------Active Dataframes------")
            print(active_df_list)

        elif len(self.df_dict.keys()) > 0 and show_recoverable:
            recoverable_df_list = [df for df in self.removed_dict.keys()]
            active_df_list = [df for df in self.df_dict.keys()]
            print("------Active Dataframes------")
            print(active_df_list)
            print("------Recoverable Dataframes------")
            print(recoverable_df_list)

    
    def merged_df(self, merged_df_name = 'all_data_merged'):
        """
        Merge all dataframes added to the class and return the resulting dataframe
        """

        if len(self.df_dict.keys()) < 2:
            print("Sorry, you need to have more than 1 dataframe added through .add_dataframe_from_csv()")
        else:
            self.df_dict[merged_df_name] = pd.concat([self.df_dict[df] for df in self.df_dict.keys()]).reset_index(drop=True)
            self.original_file_name[merged_df_name] = merged_df_name
            return self.df_dict[merged_df_name]
        
    def export_all_cleaned(self, folder_name: str = "cleaned_data", file_prefix: str = "", file_suffix: str = "_cleaned"):
        """
        Export all dataframes as cleaned CSVs, including a merged file
        """

        os.makedirs(folder_name, exist_ok=True)

        for name, dataframe in self.df_dict.items():
            file_name = file_prefix + self.original_file_name[name] + file_suffix + "_" + str(self.min_year) + "_" + str(self.max_year) + ".csv"
            file_save_path = os.path.join(folder_name, file_name)
            dataframe.to_csv(file_save_path)

            print(f'Successfully saved {file_name}!')

            



    
def main():
    TorontoCrimeDataCleaner()

if __name__ == '__main__':
    main()



