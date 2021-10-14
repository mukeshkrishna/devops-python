"""
Task-1
create a function which returns the sum of all the element provided to
it as an arguement. The arguement list will be dynamic

*args == non keyword arguments Eg: 1,2,34,"krish" etc -- represented as tuple
**kwargs == keyword arguments Eg: "key":value -- represented as dictionary
"""
def sumOfElements(*elements):
    sum = 0
    for element in elements:
        sum = sum + element
    return sum

"""
create a function in which the arguements are users and their marks and return three value. User with maximum mark, Average_marks, Users below failing marks. Below is sample of output.
("Raul": 99),("avg_marks","55"),["Hidan", "Goku", "Timon", "Sasuke", "Saitama"]

"""
def studentsTraverse(**students):
    totalMarks = 0 
    largest = 0
    largest_key = ""
    fail_list = list()
    for key,value in students.items():
        totalMarks = totalMarks + value
        if(largest<value):
            largest = value
            largest_key = key
        if(value<50):
            fail_list.append(key)
    # Get the largest score
    print("Highest Score by {0}:{1}".format(largest_key,students.get(largest_key)))
    # get the average score
    print(totalMarks/len(students))
    # Failed students list
    print("Failed Student List: {0}".format(fail_list))

a_dict = [
    {
        "name": "gara",
        "power": "some sand related jutsu",
        "powerlevel": 199,
        "frieds": [
            {
                "name": "Naruto",
                "friend_points": 28,
                "enemies": ["Saitama"] 
            },
            {
                "name": "Boruto",
                "friend_points": 18,
                "enemies": ["Saitama"]
            }
        ]
    },
    {
        "name": "Alex",
        "power": "some titans powers",
        "powerlevel": 1199,
        "frieds": [
            {
            "name": "Soniya",
            "friend_points": 128,
            "enemies": ["Saitama"] 
            }
        ]
    },
    {
        "name": "King",
        "power": "some titans powers",
        "powerlevel": 1199,
        "frieds": [
            {
            "name": "Saitama",
            "friend_points": 128,
            "enemies": ["Naruto", "gara", "boruto"] 
            }
        ]
    }
    
]

def traverseDict():
    for i in a_dict:
        print(i,end="\n")

if(__name__=="__main__"):
    args = (1,2,3,4)
    print("TASK-1:")
    print("Sum of elements = {0}".format(sumOfElements(*args)))
    kwargs = {"mukesh": 80,"gokul":90,"pragathi":95,"ravi":98,"santha":99,"krish":30,"raju":40 }
    print("---------------------------------------------")
    print("TASK-2:")
    studentsTraverse(**kwargs)
    print("TASK-3")
    print("----------------------------------------------")
    traverseDict()
    