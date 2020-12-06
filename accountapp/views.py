from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorations import account_required
from accountapp.forms import AccountUpdateForm
from articleapp.models import Article


has_ownership = [login_required, account_required]


# 함수에 사용하는 데코레이터를 클래스형 뷰 안의 함수에 사용할 수 있도록 해주는 것
# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
# 메소드 데코레이터의 첫번째 파라미터에는 여러가지의 데코레이터를 넣을 수 있다.
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # reverse와 reverse_lazy => 클래스 base 뷰에서는 reverse_lazy를 사용해야 한다.
    success_url = reverse_lazy('home')
    template_name = "accountapp/create.html"


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    # reverse와 reverse_lazy => 클래스 base 뷰에서는 reverse_lazy를 사용해야 한다.
    success_url = reverse_lazy('accountapp:home')
    context_object_name = 'target_user'
    template_name = "accountapp/update.html"


@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    context_object_name = 'target_user'
    template_name = "accountapp/delete.html"
