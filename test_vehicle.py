from vehicle import vehicle_details
def test_vehicle_details():
    expected_output = (
        "Vehicle Number: V1023\n"
        "Owner Name: Suresh\n"
        "Vehicle Type: Bike\n"
        "Year of Manufacture: 2025"
    )
    assert vehicle_details("V1023", "Suresh", "Bike", 2025) == expected_output