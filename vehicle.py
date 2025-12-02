import pytest
def vehicle_details(number, name, type, year):
    result = (
        f"Vehicle Number: {number}\n"
        f"Owner Name: {name}\n"
        f"Vehicle Type: {type}\n"
        f"Year of Manufacture: {year}"
    )
    return result
if __name__ == "__main__":
    #Sample Output
    number = "V1023"
    name = "Suresh"
    type = "Bike"
    year = 2025
    print(vehicle_details(number, name, type, year))