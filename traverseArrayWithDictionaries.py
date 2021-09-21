
students = [
    {
        "firstName" : "Alan",
        "lastName" : "Gonzalez",
        "id" : 123,
        "hobbies": ["read", "write", "sing"]
    },
    {
        "firstName" : "Julieta",
        "lastName" : "Salazar",
        "id" : 456,
        "hobbies": ["read", "program"]
    },
    {
        "firstName" : "Martha",
        "lastName" : "Ruiz",
        "id" : 789,
        "hobbies": ["movies", "video games", "program"]
    }
]

for element in students:
    print( element["firstName"] )
    for hobby in element["hobbies"]:
        print( hobby )


