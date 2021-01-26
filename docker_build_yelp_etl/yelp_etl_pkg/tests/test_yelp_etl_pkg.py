import pytest

import yelp_etl_pkg.Xtract_data as Xtract_data
import yelp_etl_pkg.Xform_dataStructs as Xform_dataStructs
import yelp_etl_pkg.helper as helper

def test_transformations():
    configFilePath = "data/Yelp_data_Set/config.properties"
    config = helper.loadConfigProps(configFilePath)
    data_path = config['S3_PATH_INFO']['TEST_PATH']

    df_users, df_r, df_business_ctr, df_ba = Xtract_data.extract_data(data_path)
    df_f = Xtract_data.create_base_ds(df_users, df_r, df_business_ctr, df_ba)

    # Checking the count of Keys: 'User - Id', 'Business - Id', 'Review - Id'
    assert(df_f['User - Id'].nunique() == 71949)
    assert(df_f['Business - Id'].nunique() == 5773)
    assert(df_f['Review - Id'].nunique() == 285764)
