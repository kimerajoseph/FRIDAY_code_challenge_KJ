#=======================================================
# tests with pytest
#=======================================================

import pytest
# import main python script
import process_addresses

def test_always_passes():
    assert True

def test_always_fails():
    assert True


@pytest.fixture
def sample_address_list():
    return ["Winterallee 3","Musterstrasse 45","Blaufeldweg 123B","Am Bächle 23","Auf der Vogelwiese 23 b",
            "4, rue de la revolution","200 Broadway Av","Calle Aduana, 29","Calle 39 No 1540","200 kimera avenue 34" ]

# ================================================================================================
# Test the type of object returned. Expected is dictionary
# ================================================================================================
def test_object_type_of_processed_address(sample_address_list):
    for address in sample_address_list:
        assert type(process_addresses.process_address(address)) is dict

# ================================================================================================
# Test the data type of key,value pairs in the returned dictionary. Expected type is string
# ================================================================================================
def test_data_type_of_key_values_of_processed_address_dict(sample_address_list):
    for address in sample_address_list:
        processed_data = process_addresses.process_address(address)
        for key,value in processed_data.items():
            assert type(key) is str and type(value) is str

# ================================================================================================
# Test the number of key,value pairs in the returned dictionary. Expected number is 2
# ================================================================================================
def test_number_key_values_pairs_of_processed_address_dict(sample_address_list):
    for address in sample_address_list:
        processed_data = process_addresses.process_address(address)
        expected_key_value_pairs = 0
        for key,value in processed_data.items():
            expected_key_value_pairs += 1
        assert expected_key_value_pairs == 2

