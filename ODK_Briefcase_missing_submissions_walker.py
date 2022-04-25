import os
from pathlib import Path
import shutil
from itertools import chain
import pandas as pd
import numpy as np
import datetime as dt
import argparse
import pyodbc
#path_parts = Path(path).parts

#=============#
## Forms dir ##
#=============#
def set_formdirs(path):
    """Return a list of form survey directories paths in a given storage path.
        Args:
          path: A directory input path.
        Returns:
          A list of form survey directories name.
    """
    form_dirs = []
    for directory in os.listdir(os.path.expanduser(path)):
        form_dirs.append(directory)
    return form_dirs

def list_forms(form_dirs):
    """List form survey forms directories from a path.
        Args:
          forms_dir: A directory path set from prior function.
    """
    for form in range(0,len(form_dirs)):
        print(form+1,"- ",form_dirs[form])

#=====================#
## Fetch Submissions ##
#=====================#
def fetch_missing_submissions(path, form_dirs):
    """Fetch submission directories that have one file
        Args:
          path: Directories path.
          forms_dir: List of directories
        Returns:
          submissions_count: A dictionary directory of each form as a key, and the count subdirs as a numeric value . {'form': int count}
          submissions_mis_list: A list, each element is a dictionary of the missing submissions. [{'form_name':'v','submission_id':'v','files_count':v}]
          submissions_mis_dic: A dictionary having a form name as a key, and a list of missing submissions as the value. {'form_name':[]}
          submissions_mis_paths: A list of absolute paths of missing submissions. [path(s)]
    """

    #=====================#
    ## Forms submissions ##
    #=====================#
    submissions_count = dict()
    submissions_names = dict()

    for form_dir in form_dirs:
        submission = os.listdir(os.path.join(path,form_dir+'\instances')) # Each submission name
        submissions_names.setdefault(form_dir, []).append(submission) # Saving submissions in a dictionary in form of name, submission as k,v
        submissions_count[form_dir] = len(submission) # Dictionary adding form and number (len) of submissions as k,v

    #========================#
    ## Submissions contents ##
    #========================#
    submissions_mis_list = [] # Used Later to be converted to pd df
    submissions_mis_dic = dict() # Used to delete submissions for specific key
    submissions_mis_paths = []

    for form_key, value in submissions_names.items():
        submissions_names_unpacked = list(chain(*submissions_names[form_key]))
        for i in range(0,len(submissions_names_unpacked)):
            contents = os.listdir(Path(path,form_key,'instances',submissions_names_unpacked[i]))
            if len(contents) == 1:
                submissions_mis_list.append({'form_name':form_key,
                                              'submissions_id':submissions_names_unpacked[i],
                                              'files_count':len(contents)})
                submissions_mis_dic.setdefault(form_key, []).append(submissions_names_unpacked[i])
                submissions_mis_paths.append(Path(path,form_key,'instances',submissions_names_unpacked[i]))
    return submissions_count, submissions_mis_list, submissions_mis_dic, submissions_mis_paths

def list_missing_submissions(path, form_dirs, mis_sub_lst, print_flag):
    if print_flag:
        for ele in mis_sub_lst:
            print("Form: {} \nSubmission id: {} \nFile Count: {}\n".format(ele['form_name'],
                                                                           ele['submissions_id'],
                                                                           ele['files_count'])
                 )
    else:
        print("Select form you'd want list missing submissions from:")
        list_forms(form_dirs)
        input_choice = input("Enter a number from 1 to {}: ".format(len(form_dirs)))
        for ele in mis_sub_lst:
            if(ele['form_name'] == form_dirs[int(input_choice)-1]):
                print("Form: {} \nSubmission id: {} \nFiles Count {}:\n".format(ele['form_name'],
                                                                                ele['submissions_id'],
                                                                                ele['files_count'])
                     )

#======================#
## Delete submissions ##
#======================#

def del_submissions(path, form_dirs, mis_sub_paths, mis_sub_dic):
    """ Delete missing submissions from all forms or a specific form.
        Args:
          path: Directories path.
          forms_dir: List of directories
          mis_sub_paths: A list of absolute paths of missing submissions. [path(s)]
          mis_sub_dic: A dictionary having a form name as a key, and a list of missing submissions as the value. {'form_name':[]}
    """
    print("1- Delete missing submissions from all forms \n2- Delete missing submissions from specific form")
    del_option = input("Enter 1 or 2: ")

    # Delete All forms
    if int(del_option) == 1:
        print("Are you sure you want to delete {} missing submissions from all forms?".format(len(mis_sub_paths)))
        cnf_flag = input('y/n: ')
        if cnf_flag.lower() == 'y':
            for sub_path in mis_sub_paths:
                shutil.rmtree(sub_path)
            print("Deleted {} missing submissions from all forms".format(len(mis_sub_paths)))
        elif cnf_flag.lower() == 'n':
            print("Nothing is deleted.")
        else:
            print("Enter Y or N (case insensitive)")

    # Delete specific form
    elif int(del_option) == 2:
        print("Select form you'd want to del missing submissions from:")
        list_forms(form_dirs)
        #form_dirs_list = set_formdirs(path)
        input_choice = input("Enter a number from 1 to {}: ".format(len(form_dirs)))
        #print('choice form is: ', form_dirs[int(input_choice)-1])
        for form_key, sub_values in mis_sub_dic.items():
            if(form_key == form_dirs[int(input_choice)-1]):
                for sub in sub_values:
                    sub_path = Path(path, form_key,'instances',sub)
                    shutil.rmtree(sub_path)
                print("Deleted {} missing submission".format(len(sub_values)))
            else:
                print("Nothing deleted")
                #shutil.rmtree(sub_path)

#=================#
## Forms Summary ##
#=================#

def forms_summary(submissions_count, submissions_mis_dic):
    """ List a summary about all forms. Count of total submissions and count missing submissions.
        Args:
          submissions_count: A dictionary directory of each form as a key, and the count subdirs as a numeric value . {'form': int count}
          submissions_mis_dic: A dictionary having a form name as a key, and a list of missing submissions as the value. {'form_name':[]}
        Returns:
          (void) A print of Pandas dataframe having 3 columns [form_name, total_submissions_count, total_missing_count]
    """
    submissions_mis_count = {}
    for key, value in submissions_mis_dic.items():
        submissions_mis_count[key] = len(value)
    forms_cnt_df = pd.DataFrame.from_dict(submissions_count, orient='index', columns=['total_cnt']).rename_axis('form_name').reset_index()
    forms_mis_df = pd.DataFrame.from_dict(submissions_mis_count, orient='index', columns=['missing_cnt']).rename_axis('form_name').reset_index()
    forms_mrg_df = pd.merge(forms_cnt_df, forms_mis_df, how='outer',on = 'form_name').fillna(0)
    forms_mrg_df.index += 1
    pd.set_option("max_colwidth", 100)
    print(forms_mrg_df)
"""
#===================#
## Update database ##
#===================#

def append_database(mis_sub_lst):
    \""" Append to database forms that are missing. If the date of query is already inside the table, the query won't append.
        Args:
          mis_sub_lst: A list, each element is a dictionary of the missing submissions. [{'form_name':'v','submission_id':'v','files_count':v}]
          submissions_mis_dic: A dictionary having a form name as a key, and a list of missing submissions as the value. {'form_name':[]}
    \"""

    ## Convert list to dataframe ##
    mis_sub_df = pd.DataFrame(mis_sub_lst)
    mis_sub_df['form_missing_sub_cnt'] = mis_sub_df.groupby('form_name')['submissions_id'].transform('nunique')
    mis_sub_df.reset_index()

    ## Convert int from 64 to 32 for SQL Server comptability ##
    mis_sub_df['files_count'] = mis_sub_df['files_count'].astype(np.int32)
    mis_sub_df['form_missing_sub_cnt'] = mis_sub_df['form_missing_sub_cnt'].astype(np.int32)

    ## DB Connection ##
    connectionString = pyodbc.connect('DRIVER={SQL Server};SERVER=;DATABASE=;Trusted_Connection=yes') # Enter connection string here
    cursor = connectionString.cursor()
    max_date = pd.read_sql("SELECT max(query_date) FROM ", connectionString) # Enter table here

    if max_date.loc[0].item() != dt.datetime.now().strftime("%Y-%m-%d"):
        row_counter = 0
        for index, row in mis_sub_df.iterrows():
            #print(row['form_name'],'\n',row['submissions_id'],'\n',float(row['files_count']))
            cursor.execute(\"""
            INSERT INTO dbo.tbl_moda_py_missing_submissions(form_name, submission_id, files_count, form_missing_submissions_cnt,query_date, query_datetime)
            VALUES (?,?,?,?,?,?)\""",
            row['form_name'],
            row['submissions_id'],
            row['files_count'],
            row['form_missing_sub_cnt'],
            dt.datetime.now().strftime("%Y-%m-%d"),
            dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                          )
            cursor.commit()
            row_counter += 1
        print("{} records inserted into database".format(row_counter))
    else:
        print('Records exist already with same date')
"""

## Boolean convertor ##

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def main():
    parser = argparse.ArgumentParser(description='Recursively counting missing submissions for each form')
    parser.add_argument('path', type=str, help='Path directory for ODKBreifcase forms dir i.e "C:\odkBriefcaseStorage\odkBriefcaseStorage\ODK Briefcase Storage\forms" ')
    parser.add_argument('--list_forms_names', type=str2bool, nargs='?', const=True, default=False, help='List forms names that were pulled in a given dir')
    parser.add_argument('--list_missing_submissions_verbose', type=str, nargs='?', const=True, default=False, help='List submissions forms to command line')
    parser.add_argument('--list_forms_summary', type=str2bool, nargs='?', const=True, default=False, help='List forms summary (total sub count & missing sub count) to command line')
    parser.add_argument('--del_missing_submissions', type=str2bool, nargs='?', const=True, default=False, help='Delete submissions for specific or all forms')
    parser.add_argument('--append_db', type=str2bool, nargs='?', const=True, help='Appends new records to db')

    args, _ = parser.parse_known_args()
    input_path = args.path
    path = os.path.abspath(input_path)

    ## Calling functions ##

    # Set directory
    form_dirs = set_formdirs(path)

    # List forms
    if args.list_forms_names:
        list_forms(form_dirs)
        exit()

    # Fetch missing submissions
    sub_count_dic, mis_sub_lst, mis_sub_dic, mis_sub_paths = fetch_missing_submissions(path, form_dirs)

    # List missing submissions
    if str(args.list_missing_submissions_verbose).lower() in ('yes', 'true', 't', 'y', '1'):
        list_missing_submissions_verbose = True
        list_missing_submissions(path, form_dirs, mis_sub_lst, list_missing_submissions_verbose)
        exit()
    elif str(args.list_missing_submissions_verbose).lower() == 'form':
        list_missing_submissions_verbose = False
        list_missing_submissions(path, form_dirs, mis_sub_lst, list_missing_submissions_verbose)
        exit()

    # List forms summary
    if args.list_forms_summary:
        forms_summary(sub_count_dic, mis_sub_dic)
        exit()

    # Delte missing submissions
    if args.del_missing_submissions:
        del_submissions(path, form_dirs, mis_sub_paths, mis_sub_dic)
        exit()

    # Append to database
    if args.append_db == False:
        exit()
    elif args.append_db == True:
        #append_database(mis_sub_lst)
        print("Please implement 'append_database()' function")
if __name__ == '__main__':
    main()
