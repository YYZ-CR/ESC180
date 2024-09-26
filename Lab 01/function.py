def greet_instructor(course, greeting):
    if course == 'Praxis':
        return greeting+'Carrick'
    elif course == 'CIV':
        return greeting+'Bentz'

if __name__ == "__main__":
    course = input('Enter course: ')
    greeting = input('Enter greeting: ')
    print(greet_instructor(course, greeting))