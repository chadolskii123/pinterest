from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorations import profile_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

has_ownership = [profile_required, login_required]


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    # success_url 로는 추가적인 파라미터를 넘겨줄 수가 없음, get_success_url 함수를 오버라이드 해서 사용해야 함.
    # success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        # 폼에 담겨오는 값을 commit 없이 받아옴
        temp_profile = form.save(commit=False)
        # 요청을 보낸 유저를 확인하고 그 유저의 프로파일에 값을 저장해줌.
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        # 추가적인 파라미터를 넘겨줄 때는 kwargs에 값을 담아서 넘겨줘야 한다.
        # self.object = profile
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    # success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'

    def form_valid(self, form):
        # 폼에 담겨오는 값을 commit 없이 받아옴
        temp_profile = form.save(commit=False)
        # 요청을 보낸 유저를 확인하고 그 유저의 프로파일에 값을 저장해줌.
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        # 추가적인 파라미터를 넘겨줄 때는 kwargs에 값을 담아서 넘겨줘야 한다.
        # self.object = profile
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
