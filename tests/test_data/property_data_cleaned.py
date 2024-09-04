property_data_cleaned = {
    # Basic Information
    "abbreviatedAddress": "88 S Cypress Ave",
    "address": {"city": "Columbus", "state": "OH", "streetAddress": "88 S Cypress Ave", "zipcode": "43222"},
    "county": "Franklin County",
    "parcelNumber": "010030174",
    "mlsId": "224027480",
    "mlsName": "Columbus and Central Ohio Regional MLS",
    "latitude": 39.957043,
    "longitude": -83.02873,
    "zpid": 33842768,
    # Descriptions and Status
    "description": "Come see this beautifully maintained 3-bedroom home, offering ample space to entertain. It features a fully fenced lot and a two-car garage. Nestled in the heart of the vibrant Franklinton neighborhood, you'll be close to all the new bars and restaurants, with easy access to the highway and a central location. Don't miss this opportunity to be at the center of all the exciting development!",
    "homeStatus": "FOR_SALE",
    "homeType": "SINGLE_FAMILY",
    "homeInsights": None,
    "price": 275000,
    "lastSoldPrice": 196000,
    "datePostedString": "2024-08-07",
    "dateSoldString": "2019-03-12",
    "roofType": None,
    "structureType": None,
    "stories": 2,
    # Measurements and Units
    "livingArea": 1260,
    "livingAreaUnits": "Square Feet",
    "lotAreaValue": 3920.4,
    "lotAreaUnits": "Square Feet",
    "yearBuilt": 1920,
    # ResoFacts
    "resoFacts": {
        "bathrooms": 2,
        "bedrooms": 3,
        "architecturalStyle": "2",
        "basement": "Full",
        "cooling": ["Central Air"],
        "heating": ["Forced Air", "Natural Gas"],
        "laundryFeatures": ["1st Flr Laundry"],
        "levels": "Two",
        "parking": 2,
        "parkingFeatures": ["2 Car Garage", "Detached"],
        "flooring": ["Carpet", "Vinyl"],
        "constructionMaterials": ["Aluminum Siding"],
        "sewer": ["Public Sewer"],
        "windowFeatures": ["Insulated Windows"],
        "associationFee": None,
    },
    # Attribution Information
    "attributionInfo": {
        "agentName": "Justin Taber",
        "agentPhoneNumber": "614-917-7842",
        "brokerName": "Associates Realty",
        "brokerPhoneNumber": "614-942-5840",
    },
    # Images
    "hiResImageLink": "https://photos.zillowstatic.com/fp/5051c23127e6d5b2d180f57946883014-p_f.jpg",
    # Schools
    "schools": [
        {
            "name": "Avondale Elementary School",
            "distance": 0.2,
            "grades": "PK-5",
            "rating": 3,
            "link": "https://www.greatschools.org/ohio/columbus/521-Avondale-Elementary-School/",
        },
        {
            "name": "Starling PK-8",
            "distance": 0.5,
            "grades": "PK-8",
            "rating": 3,
            "link": "https://www.greatschools.org/ohio/columbus/547-Dana-Avenue-Elementary-School/",
        },
        {
            "name": "West High School",
            "distance": 2.5,
            "grades": "9-12",
            "rating": 2,
            "link": "https://www.greatschools.org/ohio/columbus/632-West-High-School/",
        },
    ],
    # Price History
    "priceHistory": [
        {"date": "2019-03-12", "event": "Sold", "price": 196000},
        {"date": "2019-02-04", "event": "Pending sale", "price": 199900},
    ],
    # Tax Information
    "mostRecentTaxIncreaseRate": 0.14254391,
    "mostRecentTaxPaid": 958.8,
    "taxAssessedValue": 203300,
    "taxAssessedYear": 2023,
    "propertyTaxRate": 1.43,
    "avgTaxRateIncrease": 2.708,
    "avgTaxValue": 24102.1,
    "avgTaxPaid": 685.84,
    "taxAnnualAmount": 959,
    # Estimates
    "zestimate": None,
    "rentZestimate": None,
}

property_data_flattened = {
    # Basic Information
    "streetAddress": "88 S Cypress Ave",
    "city": "Columbus",
    "state": "OH",
    "zipcode": "43222",
    "county": "Franklin County",
    "parcelNumber": "010030174",
    "mlsId": "224027480",
    "mlsName": "Columbus and Central Ohio Regional MLS",
    "latitude": 39.957043,
    "longitude": -83.02873,
    "zpid": 33842768,
    # Descriptions and Status
    "description": "Come see this beautifully maintained 3-bedroom home, offering ample space to entertain. It features a fully fenced lot and a two-car garage. Nestled in the heart of the vibrant Franklinton neighborhood, you'll be close to all the new bars and restaurants, with easy access to the highway and a central location. Don't miss this opportunity to be at the center of all the exciting development!",
    "homeStatus": "FOR_SALE",
    "homeType": "SINGLE_FAMILY",
    "homeInsights": None,
    "price": 275000,
    "lastSoldPrice": 196000,
    "datePostedString": "2024-08-07",
    "dateSoldString": "2019-03-12",
    "roofType": None,
    "structureType": None,
    "stories": 2,
    # Measurements and Units
    "livingArea": 1260,
    "livingAreaUnits": "Square Feet",
    "lotAreaValue": 3920.4,
    "lotAreaUnits": "Square Feet",
    "yearBuilt": 1920,
    # ResoFacts
    "bathrooms": 2,
    "bedrooms": 3,
    "architecturalStyle": "2",
    "basement": "Full",
    "cooling": ["Central Air"],
    "heating": ["Forced Air", "Natural Gas"],
    "laundryFeatures": ["1st Flr Laundry"],
    "levels": "Two",
    "parking": 2,
    "parkingFeatures": ["2 Car Garage", "Detached"],
    "flooring": ["Carpet", "Vinyl"],
    "constructionMaterials": ["Aluminum Siding"],
    "sewer": ["Public Sewer"],
    "windowFeatures": ["Insulated Windows"],
    "associationFee": None,
    # Attribution Information
    "agentName": "Justin Taber",
    "agentPhoneNumber": "614-917-7842",
    "brokerName": "Associates Realty",
    "brokerPhoneNumber": "614-942-5840",
    # Images
    "hiResImageLink": "https://photos.zillowstatic.com/fp/5051c23127e6d5b2d180f57946883014-p_f.jpg",
    # Schools
    "schools": [
        {
            "name": "Avondale Elementary School",
            "distance": 0.2,
            "grades": "PK-5",
            "rating": 3,
            "link": "https://www.greatschools.org/ohio/columbus/521-Avondale-Elementary-School/",
        },
        {
            "name": "Starling PK-8",
            "distance": 0.5,
            "grades": "PK-8",
            "rating": 3,
            "link": "https://www.greatschools.org/ohio/columbus/547-Dana-Avenue-Elementary-School/",
        },
        {
            "name": "West High School",
            "distance": 2.5,
            "grades": "9-12",
            "rating": 2,
            "link": "https://www.greatschools.org/ohio/columbus/632-West-High-School/",
        },
    ],
    # Price History
    "priceHistory": [
        {"date": "2019-03-12", "event": "Sold", "price": 196000},
        {"date": "2019-02-04", "event": "Pending sale", "price": 199900},
    ],
    # Tax Information
    "mostRecentTaxIncreaseRate": 0.14254391,
    "mostRecentTaxPaid": 958.8,
    "taxAssessedValue": 203300,
    "taxAssessedYear": 2023,
    "propertyTaxRate": 1.43,
    "avgTaxRateIncrease": 2.708,
    "avgTaxValue": 24102.1,
    "avgTaxPaid": 685.84,
    "taxAnnualAmount": 959,
    # Estimates
    "zestimate": None,
    "rentZestimate": None,
}
