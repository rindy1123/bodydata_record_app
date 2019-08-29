from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from bodydata_record_app.models import WorkoutModel, DietModel, BodyModel

class CreateWorkout(CreateView):
    """筋トレデータ作成"""
    template_name = 'workout_create.html'
    model = WorkoutModel
    fields = ('name', 'weight', 'reps', 'set', 'author')
    success_url = reverse_lazy('home')


class CreateDiet(CreateView):
    """食事データ作成"""
    template_name = 'diet_create.html'
    model = DietModel
    fields = ('calorie', 'name', 'protein', 'carb', 'fat', 'author')
    success_url = reverse_lazy('home')


class CreateBody(CreateView):
    """身体データ作成"""
    template_name = 'body_create.html'
    model = BodyModel
    fields = ('weight', 'percent_body_fat', 'muscle_mass', 'author')
    success_url = reverse_lazy('home')


class DeleteWorkout(DeleteView):
    """筋トレデータ削除"""
    template_name = 'delete.html'
    model = WorkoutModel
    success_url = reverse_lazy('home')


class DeleteDiet(DeleteView):
    """食事データ削除"""
    template_name = 'delete.html'
    model = DietModel
    success_url = reverse_lazy('home')


class DeleteBody(DeleteView):
    """身体データ削除"""
    template_name = 'delete.html'
    model = BodyModel
    success_url = reverse_lazy('home')


class UpdateWorkout(UpdateView):
    """筋トレデータ編集"""
    template_name = 'workout_update.html'
    model = WorkoutModel
    fields = ('name', 'weight', 'reps', 'set')
    success_url = reverse_lazy('home')


class UpdateDiet(UpdateView):
    """食事データ編集"""
    template_name = 'diet_update.html'
    model = DietModel
    fields = ('calorie', 'name', 'protein', 'carb', 'fat')
    success_url = reverse_lazy('home')


class UpdateBody(UpdateView):
    """身体データ編集"""
    template_name = 'body_update.html'
    model = BodyModel
    fields = ('weight', 'percent_body_fat', 'muscle_mass')
    success_url = reverse_lazy('home')
