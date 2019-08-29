from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from bodydata_record_app.models import WorkoutModel, DietModel, BodyModel
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.contrib.auth.password_validation import validate_password, password_validators_help_texts
from django.core.exceptions import ValidationError

from bodydata_record_app.views.data_func import get_data, save_calorie_data
# Create your views here.


def signupfunc(request):
    """会員登録設定"""
    if request.method == 'POST':
        user = get_user_model()  # 独自のユーザーモデルを取得
        requested_name = request.POST['username']
        requested_pass = request.POST['password']
        requested_email = request.POST['email']
        requested_age = request.POST['age']
        requested_height = request.POST['height']
        requested_workout_degree = request.POST['workoutdegree']
        # パスワードのバリデーション
        error_msg = {}
        try:
            validate_password(requested_pass)
        except ValidationError:
            error_msg['error_pw_msgs'] = password_validators_help_texts()
            return render(request, 'signup.html', error_msg)
        user.objects.create_user(requested_name, requested_email, requested_pass,
                                 age=requested_age, height=requested_height, workoutdegree=requested_workout_degree)
        return redirect('login')
    else:
        return render(request, 'signup.html')


def loginfunc(request):
    """ログイン設定"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': '該当するユーザーが存在しません'})
    else:
        return render(request, 'login.html')


def logoutfunc(request):
    """ログアウト設定"""
    logout(request)
    return redirect('login')


@login_required
def homefunc(request):
    """
    ホーム画面設定

    日付を変更した場合(POST)と直接ホーム画面に訪問した場合(GET)
    """
    # 日付を変更した場合
    if request.method == 'POST':
        changed_date = request.POST['date']
        login_name = request.user.get_username()
        dict_data = get_data(login_name, changed_date)
        save_calorie_data(dict_data['body_data'])
        return render(request, 'home.html', dict_data)
    # GETで今日の日付のデータを表示
    else:
        today = timezone.localtime(timezone.now()).date()
        login_name = request.user.get_username()
        dict_data = get_data(login_name, today)
        save_calorie_data(dict_data['body_data'])
        return render(request, 'home.html', dict_data)


@login_required
def timeline_workoutfunc(request):
    """タイムラインで筋トレデータを表示"""
    workout = WorkoutModel.objects.order_by('-date').all()
    paginator = Paginator(workout, 5)
    page = request.GET.get('page')
    workout_data = paginator.get_page(page)
    return render(request, 'timeline_workout.html', {'workout_data': workout_data})


@login_required
def timeline_dietfunc(request):
    """タイムラインで食事データを表示"""
    diet = DietModel.objects.order_by('-date').all()
    paginator = Paginator(diet, 5)
    page = request.GET.get('page')
    diet_data = paginator.get_page(page)
    return render(request, 'timeline_diet.html', {'diet_data': diet_data})


@login_required
def timeline_bodyfunc(request):
    """タイムラインで身体データを表示"""
    body = BodyModel.objects.order_by('-date').all()
    paginator = Paginator(body, 5)
    page = request.GET.get('page')
    body_data = paginator.get_page(page)
    return render(request, 'timeline_body.html', {'body_data': body_data})


@login_required
def home_change_datefunc(request):
    """日付変更画面を表示"""
    return render(request, 'change_date.html')



