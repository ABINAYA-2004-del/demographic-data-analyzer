import pandas as pd

def calculate_demographic_data(print_data=True):
    # Manually creating a DataFrame with demographic data
    data = {
        "age": [39, 50, 38, 53, 28],
        "workclass": [
            "State-gov", 
            "Self-emp-not-inc", 
            "Private", 
            "Private", 
            "Private"
        ],
        "fnlwgt": [77516, 83311, 215646, 234721, 338409],
        "education": [
            "Bachelors", 
            "Bachelors", 
            "HS-grad", 
            "11th", 
            "Bachelors"
        ],
        "education-num": [13, 13, 9, 7, 13],
        "marital-status": [
            "Never-married", 
            "Married-civ-spouse", 
            "Divorced", 
            "Married-civ-spouse", 
            "Married-civ-spouse"
        ],
        "occupation": [
            "Adm-clerical", 
            "Exec-managerial", 
            "Handlers-cleaners", 
            "Handlers-cleaners", 
            "Prof-specialty"
        ],
        "relationship": [
            "Not-in-family", 
            "Husband", 
            "Not-in-family", 
            "Husband", 
            "Wife"
        ],
        "race": ["White", "White", "White", "Black", "Black"],
        "sex": ["Male", "Male", "Male", "Male", "Female"],
        "capital-gain": [2174, 0, 0, 0, 0],
        "capital-loss": [0, 0, 0, 0, 0],
        "hours-per-week": [40, 13, 40, 40, 40],
        "native-country": [
            "United-States", 
            "United-States", 
            "United-States", 
            "United-States", 
            "Cuba"
        ],
        "salary": ["<=50K", "<=50K", "<=50K", "<=50K", "<=50K"]
    }

    df = pd.DataFrame(data)

    # Calculate various statistics
    race_count = df['race'].value_counts()
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = (df[higher_education]['salary'] == '>50K').mean() * 100
    lower_education = ~higher_education
    lower_education_rich = (df[lower_education]['salary'] == '>50K').mean() * 100
    min_work_hours = df['hours-per-week'].min()
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100
    country_earning = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100
    highest_earning_country = country_earning.idxmax()
    highest_earning_country_percentage = country_earning.max()
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()
    top_IN_occupation = top_IN_occupation[0] if not top_IN_occupation.empty else "None"

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

if __name__ == "__main__":
    calculate_demographic_data()
