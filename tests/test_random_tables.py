# test load_table function 
import randomtable2026 as rt

def test_column_names():
    #Arrange 
    data_path="data/example-table.csv" 
    expected_output=['Weather', 'Time of Day', 'Enviroment', 'Enviromental Hazard', 'NPC']
    #Act 
    table=rt.load_table(data_path)
    output=table.columns.to_list()
    #Assert 
    assert output == expected_output


def test_catagories():
    #Arrange 
    data_path="data/example-table.csv"
    expected_output= ['Weather', 'Time of Day', 'Enviroment', 'Enviromental Hazard', 'NPC']
    #Act 
    actual_output=rt.catagories(filepath=data_path)
    #Assert 
    assert actual_output == expected_output
