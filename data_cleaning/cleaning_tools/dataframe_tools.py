import pandas as pd
pd.options.mode.chained_assignment = None
import os



class TorontoCrimeDataCleaner:
    def __init__(self, min_year:int, max_year:int, columns_to_keep: list = None):
        """
        This is a class meant to manipulate datasets specifically for crime data from 
        the Toronto Police Service Data Catalogue.

        Pandas is imported at the same time.

        Use .csv_to_dataframe() to add dataframes to this class

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
            self.columns_to_keep = ['EVENT_UNIQUE_ID', 'OCC_YEAR', 'OCC_MONTH', 'OCC_DAY', 
                                    'OCC_DOW','OCC_HOUR', 'PREMISES_TYPE','HOOD_140', 
                                    'NEIGHBOURHOOD_140', 'LONG_WGS84', 'LAT_WGS84', 
            ]
        else: 
            self.columns_to_keep = [columns_to_keep]
        
        self.columns_to_keep.insert(1,"CRIME")

        # This will store all active dataframes
        self.df_dict = {}

        # This will store all removed dataframes that can be recovered
        self.removed_dict = {}

        # This will store all original file names to be used in mass_export
        self.original_file_name = {}

    def _normalize_traffic_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Toronto traffic collisions contain columns named differently, or have missing information which can be inferred"""

        print("Special column reformatting initiated for 'traffic_collision' crime type. ")
        # Replace relevant column names to match pipeline
        df.rename(columns={
            "EventUniqueId": "EVENT_UNIQUE_ID",
            "Month": "OCC_MONTH",
            "Day_of_Week": "OCC_DOW",
            "Year": "OCC_YEAR",
            "Hour": "OCC_HOUR",
            "Longitude": "LONG_WGS84",
            "Latitude": "LAT_WGS84",
            "Neighbourhood": "NEIGHBOURHOOD_140",
            "Atom": "HOOD_140"
        }, inplace=True)

        df["OCC_DAY"] = df["OccurrenceDate"].str.extract(r'\d{4}\/(\d{2})\/\d{2}')
        df["PREMISES_TYPE"] = "Outside"

        return df
        

    def _normalize_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Internal method to create missing columns, reduce columns down to wanted columns, and to remove rows with nan values"""

        # Create missing columns for 'OCC_Year', 'OCC_DAY', 'OCC_HOUR'

        print("Normalizing column data...")
        for column in ['OCC_Year', 'OCC_DAY', 'OCC_HOUR']:
            if column not in df.columns:
                df[column] = 0

        if "PREMISES_TYPE" not in df.columns:
            df["PREMISES_TYPE"] = "N/A"

        try:
            df = df[self.columns_to_keep]
            df.dropna(inplace=True)
            return df
        except Exception as err:
            print("**** FAILED CLEANING SEQUENCE ****")
            print(f"Error in _normalize_columns(): {err}")
            print("--------------------------")
    
    def _remove_whitespace(self, df: pd.DataFrame) -> pd.DataFrame:
        """Internal method to remove whitespace from object dtype columns"""
        print("Starting to clear whitespaces from object columns...")
        try:
            object_columns = list(df.dtypes.loc[df.dtypes == "object"].index)
            for column in object_columns:
                df[column] = df[column].str.strip()
            
            return df
        except Exception as err:
            print("**** FAILED CLEANING SEQUENCE ****")
            print(f"Error in _remove_whitespace(): {err}")
            print("--------------------------")


    def _dates_to_int(self, df: pd.DataFrame) -> pd.DataFrame:
        """Internal method to convert data types"""

        print("Converting appropriate date data to integers...")
        for column in ['OCC_YEAR','OCC_DAY','OCC_HOUR']:
            if column in df.columns:
                try:
                    df[column] = df[column].astype(int)
                except Exception as err:
                    print("**** FAILED CLEANING SEQUENCE ****")
                    print(f"Error in _dates_to_int(): {err}")
                    print("--------------------------")
            else:
                df[column] = 0
        return df

    def _filter_by_year(self, df: pd.DataFrame) -> pd.DataFrame:
        """Internal method to filter by year"""

        print(f"Filtering years from {self.min_year} to {self.max_year}...")
        try:
            df = df[(df['OCC_YEAR'] >= self.min_year) & (df['OCC_YEAR'] <= self.max_year)]
            return df
        except Exception as err:
            print("**** FAILED CLEANING SEQUENCE ****")
            print(f"Error in _filter_by_year(): {err}")
            print("--------------------------")
    
    def _create_datetime_column(self, df: pd.DataFrame) -> pd.DataFrame:
        """Internal method to create pd.to_datetime() object out of the different date columns"""

        print("Creating 'DATE' column out of date columns...")
        try:
            df['DATE'] = df['OCC_MONTH'] + " " + df['OCC_DAY'].astype(str) + " " + df['OCC_YEAR'].astype(str)
            df['DATE'] = pd.to_datetime(df['DATE'])
            return df
        except Exception as err:
            print("**** FAILED CLEANING SEQUENCE ****")
            print(f"Error in _create_datetime_column(): {err}")
            print("--------------------------")

    def _reformat_column_names(self, df: pd.DataFrame) -> pd.DataFrame:
        """Internal method to reorder the dataframes"""

        print("Reformatting column names...")

        new_column_names = [column.lower() for column in df.columns]
        df.columns = new_column_names
        return df
        
        

    def _clean_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Internal method to utilize all preceding cleaning tools"""

        print("Starting to clean the data...")
        if df['CRIME'].values[0] == "traffic_collision":
            df = self._normalize_traffic_data(df)
        
        df = self._normalize_columns(df)
        df = self._dates_to_int(df)
        df = self._remove_whitespace(df)
        df = self._filter_by_year(df)
        df = self._create_datetime_column(df)
        df = self._reformat_column_names(df)

        print("Successfully cleaned data!")
        return df

    def csv_to_dataframe(self, crime_type: str, path_of_csv: str, override = False):
        """
        Add Pandas DataFrame from csv to class and automatically clean the data. The added dataframe
        can be accessed by the using the name_of_dataframe as a dictionary key to the
        class variables `df_dict`. 

        Example: class_variable.df_dict['df1']

        Parameters
        --
        crime_type: str
            Give a name to the dataframe you want to store
            Use a name for the type of crime (ie. 'theft_under', 'homicide', 'auto_theft', etc...)

        path_of_csv: str
            Path of CSV file to add as Pandas DataFrame
        """

        if (crime_type in self.df_dict) and not (override):
            print("--------------------------")
            print(f'"{crime_type}" dataframe already exists in this object, so this data will be skipped.')
            print('If you would like to override this blocker, then set the "override" argument to True.')
            print("--------------------------")

        else:
            try:
                print("--------------------------")
                print(f'Adding "{crime_type}" data from filepath "{path_of_csv}" to new DataFrame')
                self.df_dict[crime_type] = pd.read_csv(path_of_csv)
                print("Successfully loaded CSV to Pandas Dataframe")
                self.df_dict[crime_type]["CRIME"] = crime_type
                self.df_dict[crime_type] = self._clean_dataframe(self.df_dict[crime_type])
                self.original_file_name[crime_type] = os.path.basename(path_of_csv).replace(".csv", "")
                print(f'Successfully added "{crime_type}" data from filepath "{path_of_csv}" to new DataFrame!')
                print("--------------------------")

            except Exception as err:
                print(f'Error in csv_to_dataframe(): {err}')

    def csv_dict_to_dataframes(self, crime_path_dictionary: dict, override = False):
        """
        Perform a batch operation of the csv_to_dataframe() method above.
        Parameters
        --
        crime_path_dictionary: dict
            Dictionary object containing the str crime_type as key and the path_of_csv as the value.
            Example: {
                'assault': 'user/datasets/assault.csv',
                'homicide': 'user/datasets/homicide.csv',
                ...
            }
        """
        successful_list = []
        failed_list = []
        for crime_type, path_of_csv in crime_path_dictionary.items():
            path_exists = os.path.exists(path_of_csv)
            if path_exists:
                print(f'"{path_of_csv}" exists')
            else:
                print("********************************")
                print(f'"{path_of_csv}" does not exist.')
                print(f'Removing {crime_type} from dictionary')
                failed_list.append(crime_type)
        
        for crime_type in failed_list:
            del crime_path_dictionary[crime_type]

        for crime_type, path_of_csv in crime_path_dictionary.items():
            try:
                self.csv_to_dataframe(crime_type=crime_type, path_of_csv=path_of_csv, override=override)
                successful_list.append(crime_type)
            except:
                failed_list.append(crime_type)
        
        print(f"Successfully created the dataframe: {successful_list}")
        print(f"Failed to create the dataframes: {failed_list}")
        

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

    
    def merge_all_dataframes(self, merged_df_name:str = 'all_data') -> pd.DataFrame:
        """
        Merge all dataframes added to the class and return the resulting dataframe. 
        NOTE: Adds "_merged" suffix to end of df name
        """

        new_merged_df_name = merged_df_name + "_merged"

        if len(self.df_dict.keys()) < 2:
            print("Sorry, you need to have more than 1 dataframe added through .csv_to_dataframe()")
        else:
            self.df_dict[new_merged_df_name] = pd.concat([self.df_dict[df] for df in self.df_dict.keys() if "_merged" not in df]).reset_index(drop=True)
            self.df_dict[new_merged_df_name].drop_duplicates(subset="EVENT_UNIQUE_ID".lower(), inplace=True)
            self.original_file_name[new_merged_df_name] = new_merged_df_name
            return self.df_dict[new_merged_df_name]
        
    def merge_selective_dataframes(self, merging_df_list: list, merged_df_name: str = "partial_data") -> pd.DataFrame:
        """
        Merge dataframes passed to this method as a list and add to the class and return the resulting dataframe.
        NOTE: Adds "_selective_merged" suffix to end of df name
        """
        def rename_merged_df_name(df_name:str):
            """Recursive renaming. This will prevent overwriting selectively merged dataframes. 
            This method can only create up to 999 using the same base name"""
            if df_name in self.df_dict:
                num_suffix = int(df_name[-3:]) + 1

                # Cancel recurssion after num_suffix reaches 1000
                if num_suffix == 1000:
                    print("I don't know how you created so many selectively merged files... but maybe consider removing a few...")
                    return "end_of_the_line_merged"
                df_name = f'{df_name[:-3]}{num_suffix:03d}'
                rename_merged_df_name(df_name)
            else:
                return df_name

        # Use recursive naming method to remove any duplicate dataframe names
        new_merged_df_name = merged_df_name + "_selective_merge_001"
        new_merged_df_name = rename_merged_df_name(new_merged_df_name)

        final_merging_list = []

        for df_name in merging_df_list:
            if df_name in self.df_dict:
                final_merging_list.append(df_name)
            else:
                print(f'"{df_name}" is not a recognized dataframe name in this object.')

        if len(final_merging_list) < 2:
            print(f"Sorry, you need to have more than 1 dataframe to merge.")
            print(f'List that was passed: {final_merging_list}')
        else:
            self.df_dict[new_merged_df_name] = pd.concat([self.df_dict[df] for df in final_merging_list]).reset_index(drop=True)
            self.df_dict[new_merged_df_name].drop_duplicates(subset="EVENT_UNIQUE_ID".lower(), inplace=True)
            self.original_file_name[new_merged_df_name] = new_merged_df_name
            return self.df_dict[new_merged_df_name]

        
    def export_all_cleaned(self, folder_name: str = "cleaned_data", file_prefix: str = "", file_suffix: str = "_cleaned"):
        """
        Export all dataframes as cleaned CSVs, including all merged files created before calling this method.
        """

        folder_name = folder_name + f'_{self.min_year}_{self.max_year}'
        os.makedirs(folder_name, exist_ok=True)

        for name, dataframe in self.df_dict.items():
            file_name = file_prefix + self.original_file_name[name] + file_suffix + "_" + str(self.min_year) + "_" + str(self.max_year) + ".csv"
            file_save_path = os.path.join(folder_name, file_name)
            dataframe.to_csv(file_save_path, index=False)

            print(f'Successfully saved {file_name}!')

    def export_selective_cleaned(self, df_list: list, folder_name: str = "cleaned_data", file_prefix: str = "", file_suffix: str = "_cleaned"):
        """
        Export selective dataframes as cleaned CSVs.
        """

        folder_name = folder_name + f'_{self.min_year}_{self.max_year}'
        os.makedirs(folder_name, exist_ok=True)

        final_df_list = []

        for df_name in final_df_list:
            if df_name in self.df_dict:
                final_df_list.append(df_name)
            else:
                print(f'"{df_name}" is not a recognized dataframe name in this object.')

        if len(final_df_list) < 1:
            print("None of the df_names provided in df_list matched any dataframe names in the class object...")
            print("No exporting happened.")

        for df_name in final_df_list:
            file_name = file_prefix + self.original_file_name[df_name] + file_suffix + "_" + str(self.min_year) + "_" + str(self.max_year) + ".csv"
            file_save_path = os.path.join(folder_name, file_name)
            self.df_dict[df_name].to_csv(file_save_path, index=False)
            print(f'Successfully saved {file_name}!')

    
def main():
    pass

if __name__ == '__main__':
    main()
