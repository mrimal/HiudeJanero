# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:29:16 2017

@author: mpr
"""

import pandas as pd
import os


def csv_export(listname, filename):
    """
    This gives us the lists we have created with addresses that passed and
    failed as csvs. This can be improved by just defining csvexport(list) to
    give us csv for any file. This would be one place where the code would
    change in the final version.
    """
    final_table = pd.DataFrame(listname, index=None)
    print(final_table)
    file = filename + '.csv'
    filepath = os.path.join("output", file)
    final_table.to_csv(filepath, encoding='utf-8')
