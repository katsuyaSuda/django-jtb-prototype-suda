from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView

from .models import RequirementsInfometion
from .forms import RequirementsInfometionForm

# # Create your views here.
# class Index(TemplateView):
#     # 一覧するモデルを指定 -> `object_list`で取得可能
#     template_name = "index.html"

class List(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    model = RequirementsInfometion
    template_name = "app1/requirementsinfometion_list.html"

class Create(CreateView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    model = RequirementsInfometion
    form_class = RequirementsInfometionForm
    template_name = "app1/requirementsinfometion_form.html"
    success_url = "/"

    # 編集対象にするフィールド
    # fields = ["registrationFormRadioButton", 
    #           "outputDestinationJtbChackBox",
    #           "outputDestinationTravelChackBox",
    #           "outputDestinationPamphletChackBox",
    #           "departurePoint",
    #           "adultNum",
    #           "departureDateSettingRadio",
    #           "absoluteSettingStartDate",
    #           "absoluteSettingEndDate",
    #           "relativeSettings1StartList",
    #           "relativeSettings1EndList",
    #           "relativeSettings2StartDayTxt",
    #           "relativeSettings2EndDayTxt"
    #           ]