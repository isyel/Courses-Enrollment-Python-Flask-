
from application.models import User

def course_list():
    classes = list( User.objects.aggregate(*[
        {
            '$lookup': {
                'from': 'enrollment', 
                'localField': 'user_id', 
                'foreignField': 'user_id', 
                'as': 'r_one'
            }
        }, {
            '$unwind': {
                'path': '$r_one', 
                'includeArrayIndex': 'r_one_id', 
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$lookup': {
                'from': 'course', 
                'localField': 'r_one.courseID', 
                'foreignField': 'courseID', 
                'as': 'r_two'
            }
        }, {
            '$match': {
                'user_id': 1
            }
        }, {
            '$sort': {
                'courseID': 1
            }
        }
    ]))
    return classes