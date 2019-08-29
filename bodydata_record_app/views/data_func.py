from bodydata_record_app.models import WorkoutModel, DietModel, BodyModel
from django.contrib.auth import get_user_model

def get_data(name, date):
    """三つのデータを取得"""
    workout_data = WorkoutModel.objects.filter(author=name, date__icontains=date).all()
    diet_data = DietModel.objects.filter(author=name, date__icontains=date).all()
    body_data = BodyModel.objects.filter(author=name, date__icontains=date).all()
    return {'workout_data': workout_data, 'diet_data': diet_data, 'body_data': body_data}


def save_calorie_data(body_data):
    """
    ハリスベネディクト方程式で基礎代謝を算出

    運動強度依存定数を掛けることでメンテナンスカロリーを算出

    メンテナンスカロリーを基準に減量期・増量期のカロリーを算出
    """
    user = get_user_model()
    for data in body_data:
        user_data = user.objects.get(username=data.author)
        data.maintenance_calorie = round(user_data.workoutdegree * (13.4 * data.weight + 4.8 * user_data.height -
                                                                    5.68 * user_data.age + 88.4), 1)
        # 減量期・増量期のカロリーは目安
        data.cutting_calorie = data.maintenance_calorie - 500
        data.increasing_calorie = data.maintenance_calorie + 250
        data.save()



