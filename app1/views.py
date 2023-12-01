from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import RequirementsInfometion
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

# # Create your views here.
# class Index(TemplateView):
#     # 一覧するモデルを指定 -> `object_list`で取得可能
#     template_name = "index.html"

class List(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    model = RequirementsInfometion

class Detail(DetailView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    model = RequirementsInfometion

class Create(CreateView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    model = RequirementsInfometion

    # 編集対象にするフィールド
    fields = ["registrationFormRadioButton", 
              "outputDestinationJtbChackBox",
              "outputDestinationTravelChackBox",
              "outputDestinationPamphletChackBox",
              "departurePoint",
              "adultNum",
              "departureDateSettingRadio",
              "absoluteSettingStartDate",
              "absoluteSettingEndDate",
              "relativeSettings1StartList",
              "relativeSettings1EndList",
              "relativeSettings2StartDayTxt",
              "relativeSettings2EndDayTxt"
              ]

class Update(UpdateView):
    model = RequirementsInfometion

    # 編集対象にするフィールド
    fields = ["registrationFormRadioButton", 
              "outputDestinationJtbChackBox",
              "outputDestinationTravelChackBox",
              "outputDestinationPamphletChackBox",
              "departurePoint",
              "adultNum",
              "departureDateSettingRadio",
              "absoluteSettingStartDate",
              "absoluteSettingEndDate",
              "relativeSettings1StartList",
              "relativeSettings1EndList",
              "relativeSettings2StartDayTxt",
              "relativeSettings2EndDayTxt"
              ]